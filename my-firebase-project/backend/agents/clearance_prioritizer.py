import firebase_admin
from firebase_admin import credentials, firestore
import os
from datetime import datetime, timedelta

# Use the Firestore Emulator
os.environ["FIRESTORE_EMULATOR_HOST"] = "localhost:8080"

# Initialize Firebase Admin SDK
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    "projectId": "demo-project-id"  # Replace with your Firebase project ID
})

db = firestore.client()

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