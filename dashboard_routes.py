from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from config.database import equipment_collection, rentals_collection, customers_collection

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/summary", methods=["GET"])
@jwt_required()
def summary():
    eq_stats = {
        "total":       equipment_collection.count_documents({}),
        "available":   equipment_collection.count_documents({"status": "available"}),
        "rented":      equipment_collection.count_documents({"status": "rented"}),
        "maintenance": equipment_collection.count_documents({"status": "maintenance"}),
    }
    rental_stats = {
        "total":    rentals_collection.count_documents({}),
        "active":   rentals_collection.count_documents({"status": "active"}),
        "returned": rentals_collection.count_documents({"status": "returned"}),
    }
    customers_total = customers_collection.count_documents({})
    revenue_cursor = rentals_collection.aggregate([
        {"$group": {"_id": None, "total": {"$sum": "$total_cost"}}}
    ])
    total_revenue = round(next(revenue_cursor, {}).get("total", 0), 2)
    recent_rentals = []
    for r in rentals_collection.find().sort("created_at", -1).limit(5):
        r["_id"] = str(r["_id"])
        recent_rentals.append(r)
    return jsonify({
        "equipment": eq_stats,
        "rentals": rental_stats,
        "customers": customers_total,
        "total_revenue": total_revenue,
        "recent_rentals": recent_rentals,
    })