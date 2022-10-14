import cv2
import matplotlib.pyplot as plt


try:
    from cv2 import cv2
except ImportError:
    pass


# openCV RGB -> BRG

print(f'OpenCV version: {cv2.__version__}')

imageFirst = cv2.imread(r"C:\Users\admin1\Desktop\DSC_0143.JPG")  # if second arg is 0 you read grayscale img, cv2.IMREAD_COLOR
# cv2.namedWindow('First window', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('First window', imageFirst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()  # destroy all windows, or destroyWindow


# imgRGB = cv2.cvtColor(imageFirst, cv2.COLOR_BGR2RGB)  # convert
#
# plt.figure()
# plt.imshow(imgRGB)
# plt.show()

capture = cv2.VideoCapture(0)
while True:
    statement, frame = capture.read()
    cv2.imshow('Live stream', frame)
    if cv2.waitKey(0):
        break


