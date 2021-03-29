import pyrebase
import serial
import sys

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
# initialisatiing pyrebase
print("Firebase initializing\n")
firebase = pyrebase.initialize_app(config)

# initialisatiing Database
db = firebase.database()

ser=serial.Serial("/dev/ttyACM0",115200)


def stream_handler(message):

    try: 
        #data = db.child("test").child("send").get().val()
        data = db.child("servo").child("send").get().val()
        print("Data from database: ", data, "\n")
        print("Writing data to serial device.\n")
        ser.write(data.encode())
        ser.write('\n'.encode())
        print("Write successful, updating recv with 1")
        db.child("servo").child("recv").set(1)
    except:
        print("Something went wrong, updating recv with -1\n")
        print("Unexpected error:", sys.exc_info()[0])
        db.child("servo").child("recv").set(-1)

send_stream = db.child("servo").child("send").stream(stream_handler)
~                                                                                  