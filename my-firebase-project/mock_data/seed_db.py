from utils.db import db
from datetime import datetime, timedelta

# Add mock branches
branches = [
    {"branch_id": "branch_ny", "location": "New York"},
    {"branch_id": "branch_la", "location": "Los Angeles"}
]
for branch in branches:
    db.collection('branches').document(branch['branch_id']).set(branch)

# Add mock inventory with last_sale_date
inventory = [
    {"product_id": "product_001", "branch_id": "branch_ny", "quantity": 10, "last_sale_date": datetime.now() - timedelta(days=40)},
    {"product_id": "product_002", "branch_id": "branch_la", "quantity": 5, "last_sale_date": datetime.now() - timedelta(days=20)},
    {"product_id": "product_003", "branch_id": "branch_ny", "quantity": 0, "last_sale_date": datetime.now() - timedelta(days=50)},
]

for item in inventory:
    db.collection('inventory').add(item)