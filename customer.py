from datetime import datetime

def customer_schema(data):
    return {
        "name":         data.get("name", ""),
        "email":        data.get("email", ""),
        "phone":        data.get("phone", ""),
        "address":      data.get("address", ""),
        "id_number":    data.get("id_number", ""),
        "farm_size":    data.get("farm_size", ""),
        "created_at":   datetime.utcnow().isoformat(),
        "updated_at":   datetime.utcnow().isoformat(),
    }