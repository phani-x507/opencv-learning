import cv2
import matplotlib.pyplot as plt

cb_img =  cv2.imread('./checkerboard_color.png')
coke_img = cv2.imread('./coca-cola-logo.png')

plt.imshow(cb_img)
plt.title('matplotlib imshow')
plt.show()

window1 = cv2.namedWindow("w1")
cv2.imshow(window1,cb_img)
cv2.waitKey(5000)
cv2.destroyWindow(window1)