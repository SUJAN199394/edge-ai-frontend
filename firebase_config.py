import pyrebase

# Your web app's Firebase configuration
firebaseConfig = {
    "apiKey": "AIzaSyAQg-WSlysNTUvt9DAUAtCm6YhGZHEQYOI",
    "authDomain": "edge-ai-project-af14a.firebaseapp.com",
    "databaseURL": "https://edge-ai-project-af14a-default-rtdb.firebaseio.com",  # ✅ Add this line
    "projectId": "edge-ai-project-af14a",
    "storageBucket": "edge-ai-project-af14a.appspot.com",  # ✅ Fix the storage bucket
    "messagingSenderId": "786410910724",
    "appId": "1:786410910724:web:50319fbd5274b443917151"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

