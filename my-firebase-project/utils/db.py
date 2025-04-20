import firebase_admin # type: ignore
from firebase_admin import credentials, firestore # type: ignore

# Initialize Firebase Emulator
firebase_admin.initialize_app(options={
    "projectId": "inventory-mas-mvp-4ac2e",  # Use the project ID from .firebaserc
})

db = firestore.client()