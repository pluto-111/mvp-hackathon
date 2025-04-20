from utils.db import db

def suggest_transfers():
    # Find stockouts and surplus
    stockouts = db.collection('alerts').where('type', '==', 'stockout').stream()
    
    for alert in stockouts:
        alert_data = alert.to_dict()
        product_id = alert_data['product_id']
        branch_id = alert_data['branch_id']
        
        # Find surplus in other branches
        surplus = db.collection('inventory') \
            .where('product_id', '==', product_id) \
            .where('quantity', '>', 20) \
            .stream()
        
        for doc in surplus:
            surplus_data = doc.to_dict()
            print(f"Transfer {product_id} from {surplus_data['branch_id']} to {branch_id}")

if __name__ == "__main__":
    suggest_transfers()