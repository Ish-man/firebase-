import serial
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase
cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project-id.firebaseio.com'
})

# Initialize Serial Port
ser = serial.Serial('COM1', 9600)  # Change 'COM1' to your serial port

# Main loop to read data from serial and send to Firebase
while True:
    try:
        # Read data from serial
        data = ser.readline().decode().strip()
        
        # Send data to Firebase
        ref = db.reference('/data')
        ref.push(data)
        
        print("Data sent to Firebase:", data)
    except KeyboardInterrupt:
        print("Exiting program")
        break
    except Exception as e:
        print("Error:", e)

# Close Serial Port
ser.close()
