#!/usr/bin/python
import time
from sense_hat import SenseHat
from random import seed
from random import randint

import pyrebase

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
seed(1)

# initialisatiing pyrebase
print("Firebase initializing\n")
firebase = pyrebase.initialize_app(config)

# initialisatiing Database
db = firebase.database()


sense = SenseHat()
sense.clear()

pixels = [
    [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
	[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
	[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
	[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
	[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
	[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
	[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
	[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]  
]
# sense.clear()  
LEFT_PIXELS = [[0, 3], [0, 4]]
RIGHT_PIXELS = [[7, 3], [7, 4]]
LEFT_LIGHTS =[[0,5],[0,6]]
RIGHT_LIGHTS = [[7,5],[7,6]]
LEFT_BRAKE = [[0,0], [0,1]]
RIGHT_BRAKE = [[7,0], [7,1]]

REDLIGHTS = [[0, 7], [1, 7]]
ORGLIGHTS = [[2, 7], [3, 7]]
YELLIGHTS = [[4, 7], [5, 7]]
GRNLIGHTS = [[6, 7], [7, 7]]

BLACK = [0, 0, 0]
RED = [100, 0, 0]
ORANGE = [225, 128, 0]
YELLOW =[100, 100, 30]
GREEN =[0, 100, 0]
WHITE = [100, 100, 100]


msleep = lambda x: time.sleep(x / 1000.0)
def dispgas(servo):
    if (servo == '8'or servo =='9'):
        set_pixels(REDLIGHTS, RED)
        set_pixels(ORGLIGHTS, ORANGE)
        set_pixels(YELLIGHTS, YELLOW)
        set_pixels(GRNLIGHTS, GREEN)
        time.sleep(0.2)
        set_pixels(GRNLIGHTS, BLACK)
        time.sleep(0.2)
    elif (servo == '5'or servo =='6'):
        set_pixels(REDLIGHTS, RED)
        set_pixels(ORGLIGHTS, BLACK)
        set_pixels(YELLIGHTS, BLACK)
        set_pixels(GRNLIGHTS, BLACK)
        time.sleep(0.2)
        set_pixels(YELLIGHTS, BLACK)
        time.sleep(0.2)
    elif (servo == '3'or servo =='4'):
        set_pixels(REDLIGHTS, RED)
        set_pixels(ORGLIGHTS, ORANGE)
        set_pixels(YELLIGHTS, BLACK)
        set_pixels(GRNLIGHTS, BLACK)
        time.sleep(0.2)
        set_pixels(ORGLIGHTS, BLACK)
        time.sleep(0.2)
    elif (servo == '1'or servo =='2'):
        set_pixels(REDLIGHTS, RED)
        set_pixels(ORGLIGHTS, BLACK)
        set_pixels(YELLIGHTS, BLACK)
        set_pixels(GRNLIGHTS, BLACK)
        time.sleep(0.2)
        set_pixels(REDLIGHTS, BLACK)
        time.sleep(0.2)

def lightevent(dirr, act):
    if (dirr == "down"):
        if (act == "released"):
            db.child("canbus").child("send").set("b")
        if (act == "pressed"):
            db.child("canbus").child("send").set("B")
    if (dirr == "up"):
        if (act == "released"):
            db.child("canbus").child("send").set("p")
        if (act == "pressed"):
            db.child("canbus").child("send").set("P")
    if (dirr == "middle"):
        if (act == "pressed"):
            rnumb = randint(1, 9)
            db.child("servo").child("send").set(str(rnumb))
    if (dirr == "right"):
        if (act == "released"):
            set_pixels(RIGHT_LIGHTS, BLACK)
            db.child("canbus").child("send").set("r")
        if (act == "pressed"):
            set_pixels(RIGHT_LIGHTS, ORANGE)
            db.child("canbus").child("send").set("R")
    if (dirr == "left"):
        if (act == "released"):
            set_pixels(LEFT_LIGHTS, BLACK)
            db.child("canbus").child("send").set("l")
        if (act == "pressed"):
            set_pixels(LEFT_LIGHTS, ORANGE)
            db.child("canbus").child("send").set("L")
     

def set_pixels(pixels, col):
	for p in pixels:
		sense.set_pixel(p[0], p[1], col[0], col[1], col[2])

def check_canbus(canbus):
    if (canbus == "p"):
        set_pixels(LEFT_PIXELS, BLACK)
        set_pixels(RIGHT_PIXELS, BLACK)
        set_pixels(LEFT_BRAKE, BLACK)
        set_pixels(RIGHT_BRAKE, BLACK)
    if (canbus == "b"):
        set_pixels(LEFT_PIXELS,BLACK)
        set_pixels(RIGHT_PIXELS, BLACK)
        set_pixels(LEFT_BRAKE, BLACK)
        set_pixels(RIGHT_BRAKE, BLACK)
    if (canbus == "P"):
        set_pixels(LEFT_PIXELS, WHITE)
        set_pixels(RIGHT_PIXELS, WHITE)
        set_pixels(LEFT_BRAKE, WHITE)
        set_pixels(RIGHT_BRAKE, WHITE)
        
    if (canbus == "L"):
        set_pixels(LEFT_PIXELS, RED)
        set_pixels(LEFT_BRAKE, BLACK)
        set_pixels(RIGHT_BRAKE, BLACK)
        set_pixels(RIGHT_PIXELS, BLACK)
        time.sleep(0.2)
        set_pixels(LEFT_PIXELS, BLACK)
        time.sleep(0.2)

    if (canbus == "R"):
        set_pixels(LEFT_PIXELS, BLACK)
        set_pixels(RIGHT_PIXELS, RED)
        set_pixels(LEFT_BRAKE, BLACK)
        set_pixels(RIGHT_BRAKE, BLACK)
        time.sleep(0.2)
        set_pixels(RIGHT_PIXELS,BLACK)
        time.sleep(0.2)

    if (canbus == "B"):
        set_pixels(LEFT_PIXELS, BLACK)
        set_pixels(RIGHT_PIXELS, BLACK)
        set_pixels(LEFT_BRAKE, RED)
        set_pixels(RIGHT_BRAKE, RED)
       
while True:
    canbuss = db.child("canbus").child("send").get().val()
    servo = db.child("servo").child("send").get().val()
    
    check_canbus(canbuss)
    dispgas(servo)
    
    tempT = sense.get_temperature()
    tempT = round(tempT, 1)
    print("Temperature C", tempT)
    db.child("temp").set(tempT)
    
    
    
    humT = sense.get_temperature()
    humT = round(humT, 1)
    print("Humidity", humT)
    db.child("humidity").set(humT)
    
    
    for event in sense.stick.get_events():
        #print(event.direction, event.action)
        dirrect = event.direction
        action = event.action
        lightevent(dirrect,action)
        
        
        
