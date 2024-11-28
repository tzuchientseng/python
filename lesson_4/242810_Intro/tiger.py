import cv2
# OpenCV: intel 開發, 目的在取代 Photoshop
img = cv2.imread('tiger.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow(img)
