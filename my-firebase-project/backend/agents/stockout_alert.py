from utils.db import db
import time

def check_stockouts():
    while True:
        # Query low stock (quantity < 5)
        low_stock = db.collection('inventory').where('quantity', '<', 5).stream()
        
        for doc in low_stock:
            data = doc.to_dict()
            print(f"ALERT: Stockout of {data['product_id']} in {data['branch_id']}")
        
        time.sleep(300)  # Check every 5 minutes

if __name__ == "__main__":
    check_stockouts()