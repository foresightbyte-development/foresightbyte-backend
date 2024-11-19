import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, auth

cred = credentials.Certificate("serviceAccountKey.json")
firebase_app = firebase_admin.initialize_app(cred)



db = firestore.client()


