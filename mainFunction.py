from machine import Pin
import time
#from checkIRBreak import checkIRBreak


def checkIRBreak(irPin):
    #declared prior to main function execution
    state = irPin.value()
    if state == 0:
        print("Ball in place.\n")
        return True
    else:
        print("Ball is not in place. Looking for ball...")
    
    return False

def runMotor():
    #turn motors on
    #servo motor rotates x degrees
    #ball drops
    #motors continue to run
    time.sleep(10)
    #motor turn off
    
def checkBlocked():
    #run us code, if blocked, turn motors off
    #cannot run concurrently without multithreading
    return False
    
irPin = Pin(5, Pin.IN, Pin.PULL_UP)
usSensorEcho = Pin(6,Pin.IN)
usSensorTrig = Pin(7,Pin.IN)



while True:
    #checkIRBreak(irPin)
    if checkIRBreak(irPin):
        if not checkBlocked(usSensor):
            runMotor()
    else:
        print("not blocked")
    time.sleep(1)
    
