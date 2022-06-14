import cv2
 #step 3.1
Ig = cv2.imread("Frame0064.png")

Blue = Ig.copy()
Green = Ig.copy()
Red = Ig.copy()

Blue[:, :, 1] = 0
Blue[:, :, 2] = 0
Green[:, :, 0] = 0
Green[:, :, 2] = 0
Red[:, :, 0] = 0
Red[:, :, 1] = 0
cv2.imshow("Red Channel:", Red)
cv2.imshow("Green Channel:", Green)
cv2.imshow("Blue Channel:", Blue)

cv2.waitKey(100000)


# #step3.2
# import cv2
#
# Ig = cv2.imread("Frame0064.png")
#
# cv2.waitKey(0)
# Ig_HSV = cv2.cvtColor(Ig, cv2.COLOR_BGR2HSV)
# cv2.imshow("RGB2HSV", Ig_HSV)
# cv2.waitKey(0)