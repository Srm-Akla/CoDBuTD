# File for depth camera

try:
    import cv2
    import pyrealsense2.pyrealsense2 as rs
    import numpy as np
    import datetime
except ImportError:
    print("Error importing, Are the packages installed properly?")
    exit(1)

class Depth:
    def __init__(self):
        self.current_time = datetime.datetime.now()
        print("{}Depth Camera{} -- {}".format("\033[1;96m","\033[0m", self.current_time))

        self.pipeline = rs.pipeline()
        self.config = rs.config()

        self.config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        self.pipeline.start(self.config)

    def capture(self):
        # Wait for a coherent pair of frames: depth 
        try:
            for _ in range(5000):
                self.frames = self.pipeline.wait_for_frames()
                self.depth_frame = self.frames.get_depth_frame()
                self.color_frame = self.frames.get_color_frame()
                #print("Capturing frames {}".format(datetime.datetime.now()))

                # Convert images to numpy arrays
                self.depth_image = np.asanyarray(self.depth_frame.get_data())
                self.color_image = np.asanyarray(self.color_frame.get_data())
                #print("Numpy array {}".format(datetime.datetime.now()))

                # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
                self.depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(self.depth_image, alpha=0.03), cv2.COLORMAP_JET)
                #print("Colormap {}".format(datetime.datetime.now()))

                self.datetime = datetime.datetime.now()
                self.timestamp = self.datetime.strftime("%d-%m-%Y_%H-%M-%S-%f")
                cv2.imwrite('/home/pi/thesis-2022/tiav/datasets/bird/Depth/Depth_{}.png'.format(self.timestamp), self.depth_colormap)
                cv2.imwrite('/home/pi/thesis-2022/tiav/datasets/bird/Color/Color_{}.png'.format(self.timestamp), self.color_image)
        finally:
            print("{}Depth Camera Finished{} -- {}".format("\033[1;96m","\033[0m", self.current_time))
            self.pipeline.stop()

    def exit(self):
        exit(0)


if __name__ == "__main__":
    Depth().capture()
