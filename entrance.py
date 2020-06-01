import RPi.GPIO as GPIO
import time

relay = [21, 20, 16, 13, 19, 26]
GPIO.setmode(GPIO.BCM)
for i in relay :
    GPIO.setup(i, GPIO.OUT)



def slotOpen(slot) : 
    GPIO.output(relay[slot], True)
    print("slot " + str(slot+1) + " open")
    return "true"

def slotClose(slot) : 
    GPIO.output(relay[slot], False)
    print("slot " + str(slot+1) + " close")
    return "true"


# slotOpen(0)
# time.sleep(3)
# slotClose(0)