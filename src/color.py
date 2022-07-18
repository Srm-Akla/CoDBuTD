
try:
    import cv2
    import pyrealsense2.pyrealsense2 as rs
    import numpy as np
    import datetime
except ImportError:
    print("Trouble importing, did you install the packages?")
    exit(1)

class Color:
    def __init__(self):
        self.current_time = datetime.datetime.now()
        print("{}Color Camera{} -- {}".format("\033[1;95m","\033[0m", self.current_time))
        # Configure depth and color streams
        self.pipeline = rs.pipeline()
        self.config = rs.config()

        self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        self.pipeline.start(self.config)

    def capture(self):
        try:
            for _ in range(100):

                # Wait for a coherent pair of frames: color
                self.frames = self.pipeline.wait_for_frames()
                self.color_frame = self.frames.get_color_frame()

                # Convert images to numpy arrays
                self.color_image = np.asanyarray(self.color_frame.get_data())
                #print(self.color_image)

                self.datetime = datetime.datetime.now()
                self.timestamp = self.datetime.strftime("%d-%m-%Y_%H-%M-%S-%f")
                # Show images
                #cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
                cv2.imwrite('/home/pi/thesis-2022/tiav/datasets/Color/Color_{}.png'.format(self.timestamp), self.color_image)

        finally:
            print("{}Color Camera Finished{}".format("\033[1;95m","\033[0m"))
            # Stop streaming
            self.pipeline.stop()

if __name__ == "__main__":
    Color().capture()
