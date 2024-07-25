import cv2
import numpy as np

image = cv2.imread('red.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([140, 30, 30])
upper_red2 = np.array([179, 255, 255])

mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
combined_mask = mask1 + mask2

purple_color = 160
hsv_image[..., 0] = np.where(combined_mask == 255, purple_color, hsv_image[..., 0])

new_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
new_image[combined_mask == 0] = [0, 0, 0]

cv2.imshow("Orijinal Image", image)
cv2.imshow("Sonuc Mask", combined_mask)
cv2.imshow("mor_gul",new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


