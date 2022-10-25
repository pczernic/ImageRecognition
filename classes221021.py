import cv2 as cv2
import numpy as np


points = []


def draw_rectangle(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDBLCLK:
        points = [(x, y)]
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        points.append((x, y))
    print(points)

    if np.size(points, 0) == 2:
        cv2.rectangle(img, points[0], points[1], (0, 255, 0), 2)
    else:
        print('Not enough points.')


image_path = 'openCVlogo.png'
img = cv2.imread(image_path)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(20) and 0xFF == 27:
        break

cv2.destroyAllWindows()


