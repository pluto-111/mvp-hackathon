import time
from utils.db import db

def monitor_inventory():
    # Listen for real-time changes in Firestore
    def on_snapshot(col_snapshot, changes, read_time):
        for change in changes:
            if change.type.name == 'MODIFIED':
                product = change.document.to_dict()
                print(f"Updated: {product['product_id']} in {product['branch_id']}")

    # Watch the 'inventory' collection
    inventory_ref = db.collection('inventory')
    inventory_watch = inventory_ref.on_snapshot(on_snapshot)

    # Keep the script running
    while True:
        time.sleep(1)

if __name__ == "__main__":
    monitor_inventory()