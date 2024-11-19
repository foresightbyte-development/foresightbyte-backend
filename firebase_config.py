import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, auth

cred = credentials.Certificate("foresightbyte-0001-firebase-adminsdk-xhp8j-e929ce6d44.json")
firebase_app_1 = firebase_admin.initialize_app(cred)




print('HAAAAAAAAAAAAAAAAAAAAAAAAA')