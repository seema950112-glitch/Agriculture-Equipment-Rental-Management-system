from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config.database import init_db
from routes.auth_routes      import auth_bp
from routes.equipment_routes import equipment_bp
from routes.customer_routes  import customers_bp
from routes.rental_routes    import rentals_bp
from routes.dashboard_routes import dashboard_bp

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "agri-rental-secret-2024"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
app.config["JWT_ALGORITHM"] = "HS256"
app.config["JWT_DECODE_ALGORITHMS"] = ["HS256"]
app.config["PROPAGATE_EXCEPTIONS"] = True

CORS(app)
JWTManager(app)

app.register_blueprint(auth_bp,      url_prefix="/api/auth")
app.register_blueprint(equipment_bp, url_prefix="/api/equipment")
app.register_blueprint(customers_bp, url_prefix="/api/customers")
app.register_blueprint(rentals_bp,   url_prefix="/api/rentals")
app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")

@app.route("/")
def health():
    return {"status": "ok", "message": "Agri Rental API running"}

if __name__ == "__main__":
    init_db()
    print("🌾 Agriculture Equipment Rental API starting...")
    print("📡 Running on http://localhost:5000")
    app.run(debug=True, host="0.0.0.0", port=5000)