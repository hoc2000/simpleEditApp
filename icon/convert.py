import cv2.cv2 as cv2

# Đọc ảnh
image = cv2.imread("snapchat-removebg-preview.png",-1)
# cv2.imshow("Anh", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
alpha = image[:,:,3]
binary = ~alpha

image_normal= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image_rs= cv2.resize(binary,dsize=(60,60))


cv2.imwrite('SNAPCHHAT.png',image_rs)

cv2.waitKey(0)