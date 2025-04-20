#auth.py
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase Admin SDK with emulator support
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    "projectId": "inventory-mas-mvp-4ac2e",  # Replace with your Firebase project ID
})

# Use the Firebase Auth Emulator
import os
os.environ["FIREBASE_AUTH_EMULATOR_HOST"] = "localhost:9099"

def sign_in_with_email_and_password(email, password):
    try:
        # Authenticate the user using the emulator
        user = auth.get_user_by_email(email)
        return {"localId": user.uid, "email": user.email}
    except Exception as e:
        print(f"Error: {e}")
        return None