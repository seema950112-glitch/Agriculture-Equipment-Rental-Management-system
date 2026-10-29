from datetime import datetime

def rental_schema(data):
    start = data.get("start_date", "")
    end   = data.get("end_date", "")
    daily = float(data.get("daily_rate", 0))

    total_days = 1
    if start and end:
        try:
            d1 = datetime.strptime(start, "%Y-%m-%d")
            d2 = datetime.strptime(end,   "%Y-%m-%d")
            total_days = max(1, (d2 - d1).days)
        except Exception:
            total_days = 1

    return {
        "rental_id":      data.get("rental_id", ""),
        "customer_id":    data.get("customer_id", ""),
        "customer_name":  data.get("customer_name", ""),
        "equipment_id":   data.get("equipment_id", ""),
        "equipment_name": data.get("equipment_name", ""),
        "start_date":     start,
        "end_date":       end,
        "total_days":     total_days,
        "daily_rate":     daily,
        "total_cost":     round(daily * total_days, 2),
        "advance_paid":   float(data.get("advance_paid", 0)),
        "status":         data.get("status", "active"),
        "notes":          data.get("notes", ""),
        "created_at":     datetime.utcnow().isoformat(),
        "updated_at":     datetime.utcnow().isoformat(),
    }