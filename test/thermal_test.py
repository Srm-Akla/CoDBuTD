#!/usr/bin/env python

"""
CV2 video capture example from Pure Thermal 1
"""

try:
    import cv2
except ImportError:
    print("ERROR python-opencv must be installed")
    exit(1)

class OpenCvCapture(object):
    """
    Encapsulate state for capture from Pure Thermal 1 with OpenCV
    """

    def __init__(self):
        # capture from the LAST camera in the system
        # presumably, if the system has a built-in webcam it will be the first

        self.cv2_cap = cv2.VideoCapture(4)
        self.cv2_cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))

    def show_video(self):
        """
        Run loop for cv2 capture from lepton
        """

        #cv2.namedWindow("lepton", cv2.WINDOW_NORMAL)
        print("Running, ESC or Ctrl-c to exit...")
        while True:
            ret, img = self.cv2_cap.read()

            if ret == False:
                print("Error reading image")
                break

            rotate_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            cv2.imshow("lepton.jpg", cv2.resize(rotate_img, (640, 480)))
            #print("LOOP:", i)

    def exit(self):
        cv2.destroyAllWindows()
        exit(0)

if __name__ == '__main__':
    OpenCvCapture().show_video()

