import pyrebase
import serial

config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": "",
    "serviceAccount": ""
}
# initialisating pyrebase
print("Firebase initializing\n")
firebase = pyrebase.initialize_app(config)

# initialisating Database
db = firebase.database()

ser=serial.Serial("/dev/ttyUSB0", 115200)

def stream_handler(message):
    #send data updated, lets grab the new data
    try:
        data = db.child("canbus").child("send").get().val()
        print("Data from database: ", data, "\n") 
        print("Writing data to serial device.\n")
        ser.write(data.encode())
        print("Write successful, updating recv with 1")
        db.child("canbus").child("recv").set("1")
    except:
        print("Something went wrong, updating recv with -1\n")
        db.child("canbus").child("recv").set("-1")

send_stream = db.child("canbus").child("send").stream(stream_handler)
