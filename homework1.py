import numpy as np
import cv2


image = np.zeros((1024, 1024, 3), np.uint8)
image += 255

image = cv2.ellipse(image, (490, 160), (120, 120), 120, 0, 300, (0, 0, 255), -1)  # red
image = cv2.circle(image, (490, 160), 50, (255, 255, 255), -1)
image = cv2.ellipse(image, (352, 400), (120, 120), 0, 0, 300, (0, 255, 0), -1)  # green
image = cv2.circle(image, (352, 400), 50, (255, 255, 255), -1)
image = cv2.ellipse(image, (623, 400), (120, 120), 300, 0, 300, (255, 0, 0), -1)  # blue
image = cv2.circle(image, (623, 400), 50, (255, 255, 255), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
image = cv2.putText(image, "OpenCV", (250, 650), font, 4, (0, 0, 0), 4, cv2.LINE_AA)

cv2.imshow('OpenCV Logo', image)
cv2.imwrite('openCVlogo.png', image)
cv2.waitKey(000)
cv2.destroyAllWindows()

