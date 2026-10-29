from datetime import datetime

EQUIPMENT_CATEGORIES = [
    "Tractor", "Harvester", "Plough", "Seeder", "Sprayer",
    "Irrigation", "Cultivator", "Thresher", "Other"
]

def equipment_schema(data):
    return {
        "equipment_id":  data.get("equipment_id", ""),
        "name":          data.get("name", ""),
        "category":      data.get("category", ""),
        "brand":         data.get("brand", ""),
        "model":         data.get("model", ""),
        "year":          data.get("year", datetime.now().year),
        "daily_rate":    float(data.get("daily_rate", 0)),
        "status":        data.get("status", "available"),
        "description":   data.get("description", ""),
        "image_url":     data.get("image_url", ""),
        "created_at":    datetime.utcnow().isoformat(),
        "updated_at":    datetime.utcnow().isoformat(),
    }