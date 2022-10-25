import cv2

drawing = False  # true if mouse is pressed
ix, iy = -1, -1


# mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img, img_showed

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_showed = cv2.imread(img_path)
            cv2.rectangle(img_showed, (ix, iy), (x, y), (0, 255, 0), 3)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


img_path = r'C:\Users\admin1\Desktop\mmns\ImageRecognition\GG.jpg'
img = cv2.imread(img_path)
img_showed = img
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

while True:
    cv2.imshow('image', img_showed)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
