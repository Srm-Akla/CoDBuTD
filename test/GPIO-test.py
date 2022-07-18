import RPi.GPIO as GPIO
import cv2
import thermal_test

#Power, 3.3V    # Red,    Pin 1
pinRecord = 17  # Brown,  Pin 6
pinPicture = 27 # Orange, Pin 7
pinLED = 22     # Yellow, Pin 8


# Initiates GPIO during boot
def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pinRecord, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(pinPicture, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(pinLED, GPIO.OUT)


def listen():
    pictureCaptured = 0
    print("Entered 'listen'")

    while True:
        #if pinPicture == GPIO.HIGH:
        if cv2.waitKey(1) & GPIO.input(pinRecord) == GPIO.HIGH:
            print("CAMERA OFF")
            thermal_test.OpenCvCapture().exit()
            GPIO.output(pinLED, GPIO.HIGH)

        if cv2.waitKey(1) & GPIO.input(pinPicture) == GPIO.HIGH: # PC-test
            thermal_test.OpenCvCapture().show_video()
            print("CAMERA ON")
            GPIO.output(pinLED, GPIO.LOW)


if __name__ == '__main__':
    init()
    listen()

    GPIO.cleanup()
