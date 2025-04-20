import streamlit as st # type: ignore
from utils.auth import auth # type: ignore
from utils.db import db

# Initialize Firebase
auth = auth()
db = db()

# Login UI
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = auth.sign_in_with_email_and_password(email, password)
    user_role = db.collection('users').document(user['localId']).get().to_dict().get('role')

    if user_role == "superadmin":
        st.session_state.logged_in = True
    else:
        st.error("Access denied.")

if st.session_state.get('logged_in'):
    st.title("Superadmin Dashboard")
    
    # Query stockouts
    if st.button("Show Stockouts"):
        stockouts = db.collection('alerts').where('type', '==', 'stockout').stream()
        for alert in stockouts:
            st.write(alert.to_dict())
    
    # Query clearance priorities
    if st.button("Show Clearance Priorities"):
        clearance_items = db.collection('inventory').where('quantity', '>', 0).stream()
        for item in clearance_items:
            st.write(item.to_dict())