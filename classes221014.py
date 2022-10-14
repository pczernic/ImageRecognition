import numpy as np
import cv2

image = np.zeros((1024, 1024, 3), np.uint8)
image = image + 255

# start_point = (1024, 0)
# end_point = (0, 1024)
# color = (0, 255, 0)  # green
# thickness = 15
# image = cv2.line(image, start_point, end_point, color, thickness)
# cv2.imshow('Line', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
# points = np.array([[1024, 0], [500, 400], [400, 800], [0, 540], [200, 200]], np.int32)
# point = points.reshape((-1, 1, 2))
# image = cv2.polylines(image, [points], True, (255, 0, 0), 15)
# cv2.imshow('Polygon', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# image = cv2.rectangle(image, [100, 100], [200, 200], [0, 0, 255], 5)
# image = cv2. circle(image, [512, 512], 100, [0, 255, 255], 5)
# image = cv2. ellipse(image, [512, 512], [300, 200], 0, 0, 270, [255, 0, 0], 50)
#
# font = cv2.FONT_HERSHEY_SIMPLEX  # font for logo
# image = cv2.putText(image, 'My text', [512, 512], font, 5, (255, 255, 255))

# image = cv2. circle(image, [512, 512], 100, [255, 0, 0], -1)
image = cv2. ellipse(image, [512, 512], [300, 200], 0, 0, 270, [255, 0, 0], 50, lineType=-1)
font = cv2.FONT_HERSHEY_SIMPLEX
image = cv2.putText(image, 'OpenCV', [512, 1000], font, 2, (0, 0, 0), 3)
cv2.imshow('OpenCV Logo', image)
cv2.waitKey(4000)
cv2.destroyAllWindows()
