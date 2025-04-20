from utils.db import db
from datetime import datetime, timedelta

def prioritize_clearance():
    # Find items with no sales in 30 days
    thirty_days_ago = datetime.now() - timedelta(days=30)
    slow_moving = db.collection('inventory') \
        .where('last_sale_date', '<', thirty_days_ago) \
        .where('quantity', '>', 0) \
        .stream()

    for doc in slow_moving:
        data = doc.to_dict()
        print(f"Clearance needed: {data['product_id']} in {data['branch_id']}")

if __name__ == "__main__":
    prioritize_clearance()