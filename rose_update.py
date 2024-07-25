import cv2
import numpy as np

image = cv2.imread('red.jpg')
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 100, 100])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(image_hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(image_hsv, lower_red2, upper_red2)

combined_mask = cv2.bitwise_or(mask1, mask2)

cv2.imshow('Maske', combined_mask)
cv2.waitKey(0) #150 220 80 #150,255,255

mor_bgr = np.array([255, 0, 255])
image[combined_mask != 0] = mor_bgr
cv2.imshow('Yeni Mor Gul', image)
cv2.waitKey(0)
cv2.destroyAllWindows()







