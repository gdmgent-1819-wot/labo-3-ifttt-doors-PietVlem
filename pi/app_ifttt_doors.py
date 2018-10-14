import requests
from sense_emu import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

sensehat = SenseHat()

def joystickUp(event):
    if event.action == ACTION_RELEASED:
        r = requests.post("https://maker.ifttt.com/trigger/front_door_opened/with/key/gT3jmnxkbXltZXqq7UhWFERRtyyZ6Ddru90SFtB1rya?")
    
def joystickDown(event):
    
    if event.action == ACTION_RELEASED:
        r = requests.post("https://maker.ifttt.com/trigger/front_door_closed/with/key/gT3jmnxkbXltZXqq7UhWFERRtyyZ6Ddru90SFtB1rya?")

def joystickLeft(event):
    
    if event.action == ACTION_RELEASED:
        r = requests.post("https://maker.ifttt.com/trigger/back_door_opened/with/key/gT3jmnxkbXltZXqq7UhWFERRtyyZ6Ddru90SFtB1rya?")

def joystickRight(event):
    
    if event.action == ACTION_RELEASED:
        r = requests.post("https://maker.ifttt.com/trigger/back_door_closed/with/key/gT3jmnxkbXltZXqq7UhWFERRtyyZ6Ddru90SFtB1rya?")

def joystickMiddle(event):
    if event.action == ACTION_RELEASED:

     temp = "{}°C".format(sensehat.get_temperature())
     hum = "{}%".format(sensehat.get_humidity())
     press = "{}.Ombar".format(sensehat.get_pressure())

     r = requests.post("https://maker.ifttt.com/trigger/sensors/with/key/gT3jmnxkbXltZXqq7UhWFERRtyyZ6Ddru90SFtB1rya?",
                     data = {
                       "value1" : temp,
                       "value2" : hum,
                       "value3" : press          
                           })

     print(temp, hum, press)

sensehat.stick.direction_up = joystickUp
sensehat.stick.direction_down = joystickDown
sensehat.stick.direction_left = joystickLeft
sensehat.stick.direction_right = joystickRight
sensehat.stick.direction_middle = joystickMiddle

pause()