import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flow import app

cred = credentials.Certificate("otto-8275b-firebase-adminsdk-1zc00-0b4f43d44a.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection("Meisan").document("question")

def update_data_2_firebase(question: str, answer: str, command: str):

    data = {
        "question": question,
        "answer": answer,
        "command": command
            }
    doc_ref.set(data, merge=True)
    print("Done updating to Firebase")
