try:
    import RPi.GPIO as GPIO
    import cv2
    import subprocess
    from time import sleep
except ImportError:
    print("Trouble importing, did you install the packages or do files exist?")
    exit(1)

class gpio:
    def __init__(self):
        #Power, 3.3V    # Red,    Pin 1
        self.pinStop = 17  # Brown,  Pin 6
        self.pinStart = 27 # Orange, Pin 7
        self.pinLED = 22     # Yellow, Pin 8
        self.process_status = 0

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pinStop, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pinStart, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pinLED, GPIO.OUT)
        GPIO.output(self.pinLED, GPIO.LOW)
    
    def turn_on(self):
        self.process_status = 1
        #self.thermal_proc = subprocess.Popen(["python3", "/home/pi/thesis-2022/tiav/src/thermal.py"])
        self.depth_proc = subprocess.Popen(["python3", "/home/pi/thesis-2022/tiav/src/depth.py"])
        #self.color_proc = subprocess.Popen(["python3", "color.py"])
        print("{}-----CAMERA ON-----{}".format("\033[1;92m","\033[0m"))
        GPIO.output(self.pinLED, GPIO.LOW)

    def turn_off(self):
        self.process_status = 0
        #self.thermal_proc.terminate()
        self.depth_proc.terminate()
        #self.color_proc.terminate()
        print("{}-----CAMERA OFF-----{}".format("\033[1;92m","\033[0m"))
        GPIO.output(self.pinLED, GPIO.HIGH)

    def listen(self):
        print("{}-----LISTENING-----{}".format("\033[1;96m","\033[0m"))
        GPIO.output(self.pinLED, GPIO.HIGH)
        while True:
            sleep(0.1)
            #if pinPicture == GPIO.HIGH:
            if (cv2.waitKey(1)) & (GPIO.input(self.pinStart) == GPIO.HIGH) & (self.process_status == 0): # PC-test
                self.turn_on()

            if (cv2.waitKey(1)) & (GPIO.input(self.pinStop) == GPIO.HIGH) & (self.process_status == 1):
                self.turn_off()

