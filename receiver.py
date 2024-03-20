import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase
cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project-id.firebaseio.com'
})

# Reference to the Firebase database
ref = db.reference('/data')

# Function to handle new data added to Firebase
def handle_new_data(event):
    data = event.data
    print("New data:", data)

# Listen for new data added to Firebase
ref.listen(handle_new_data)

# Keep the program running
input("Press Enter to exit...\n")
