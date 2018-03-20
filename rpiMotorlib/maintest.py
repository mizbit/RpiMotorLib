
import rpiMotorlib
import time 

def main():
    """main function loop"""
    # These are the four GPIO pins we will
    # use to drive the stepper motor, in the order
    # they are plugged into the controller board. So,
    # GPIO 18 is plugged into Pin 1 on the stepper motor.
    GpioPins = [18, 23, 24, 25]
    # Declare an named instance of class pass a name
    mymotortest = rpiMotorlib.BYJMotor("NotorTwo")
    # Call motorRun function pass it (Gpiopins . wait , steps, counterclockwise, verbose)
    # wait, type=float, default=0.001, help="Time to wait (in seconds) between steps. Default time is 0.001"
    # steps, type=int, default=500, help="Number of steps to take. Default is 500, which is roughtly one revolution."
    # counterclockwise, help="Turn stepper counterclockwise default=False
    # verbose, help="Write pin actions", default=False
    
    mymotortest.motorRun(GpioPins,.01,512, False, True,"full")
    time.sleep(5)
    mymotortest.motorRun(GpioPins,.001,512, False, True,"half")
    time.sleep(5)
    mymotortest.motorRun(GpioPins,.01,512, False, True,"wave")
    time.sleep(5)
    mymotortest.motorRun(GpioPins,.01, 250, False, False,"half")
    time.sleep(5)
    mymotortest.motorRun(GpioPins,.5, 2, True, True,"half")
    time.sleep(5)
    mymotortest.motorRun(GpioPins,.001,2000,False,False,"half")
    time.sleep(5)
    mymotortest.motorRun(GpioPins)
# ===================MAIN===============================

if __name__ == '__main__':
    print("start test")
    main()
    print("end test")

# =====================END===============================
