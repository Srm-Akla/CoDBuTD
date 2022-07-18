# File for thermal camera
try:
    import cv2
    import numpy as np
    import datetime
    import time
    import subprocess
except ImportError:
    print("Error importing, Are the packages installed properly?")
    exit(1)

class Thermal:
    def __init__(self):
        self.channel = subprocess.run(["bash", "/home/pi/thesis-2022/tiav/src/get_channel.sh"], capture_output=True)
        self.webcam = cv2.VideoCapture(int(self.channel.stdout.decode("utf-8")[-2:-1]))
        self.current_time = datetime.datetime.now()
        print("{}Thermal Camera{} -- {}".format("\033[1;91m","\033[0m", self.current_time))

    def capture(self):
        try:
            for _ in range(2000):
                self.datetime = datetime.datetime.now()
                self.timestamp = self.datetime.strftime("%d-%m-%Y_%H-%M-%S-%f")
                #print("Time {}".format(datetime.datetime.now()))
                self.ret, self.frame = self.webcam.read()
                #print("Getting image {}".format(datetime.datetime.now()))
                if self.ret == False:
                    print("Error, cant capture image!")
                #print("Rotating image {}".format(datetime.datetime.now()))
                self.rotate_frame = cv2.rotate(self.frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
                #print("Writing image {}".format(datetime.datetime.now()))
                cv2.imwrite("/home/pi/thesis-2022/tiav/datasets/bird/Thermal/Thermal_{}.png".format(self.timestamp), self.rotate_frame)
        finally:
            print("{}Thermal Camera Finished{} -- {}".format("\033[1;91m","\033[0m", self.current_time))
            exit(0)


    def exit(self):
        exit(0)

if __name__ == "__main__":
    Thermal().capture()
