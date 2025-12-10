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

window2 = cv2.namedWindow('w2')
cv2.imshow(window2,coke_img)
cv2.waitKey(0) #It acts like infinite waiting until any key pressed.
cv2.destroyWindow(window2)

window3 = cv2.namedWindow('w3')
cv2.imshow(window3,cb_img)
while True:
    if cv2.waitKey(1) == ord("q"): # in this way we can assign specific key to quit windows
        cv2.destroyWindow(window3)
        break

cv2.destroyAllWindows()
 
 
