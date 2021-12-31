import cv2.cv2 as cv2
import numpy as np
from scipy.interpolate import UnivariateSpline

# Read the image
image = cv2.imread('sample/shop.jpg')


# greyscale filter
def greyscale(img):
    greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return greyscale
def bright(img, beta_value):
    img_bright = cv2.convertScaleAbs(img, beta=beta_value)
    return img_bright
a2 = bright(image, 60)
a1 = greyscale(image)
a3 = bright(image, -60)
def sharpen(img):
    kernel = np.array([[-1, -1, -1],
                       [-1, 9.5, -1],
                       [-1, -1, -1]])
    img_sharpen = cv2.filter2D(img, -1, kernel)
    return img_sharpen
a4 = sharpen(image)

def oldtime(img):
    img_sepia = np.array(img, dtype=np.float64)  # converting to float to prevent loss
    img_sepia = cv2.transform(img_sepia, np.matrix([[0.272, 0.534, 0.131],
                                                    [0.349, 0.686, 0.168],
                                                    [0.393, 0.769,
                                                     0.189]]))  # multipying image with special sepia matrix
    img_sepia[np.where(img_sepia > 250)] = 255  # normalizing values greater than 255 to 255
    img_sepia = np.array(img_sepia, dtype=np.uint8)
    return img_sepia


a5 = oldtime(image)
def pencil_sketch_grey(img):
    # inbuilt function to create sketch effect in colour and greyscale
    sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1)
    return sk_gray


a6 = pencil_sketch_grey(image)
def pencil_sketch_col(img):
    # inbuilt function to create sketch effect in colour and greyscale
    sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1)
    return sk_color


a7 = pencil_sketch_col(image)
def HDR(img):
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return  hdr

a8 = HDR(image)

def LookupTable(x, y):
  spline = UnivariateSpline(x, y)
  return spline(range(256))

#summer effect
def Summer(img):
    increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    blue_channel, green_channel,red_channel  = cv2.split(img)
    red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
    sum= cv2.merge((blue_channel, green_channel, red_channel ))
    return sum

a9=Summer(image)
# cv2.imshow("he",a9)
# cv2.waitKey()
# cv2.destroyAllWindows()

#winter effect
def Winter(img):
    increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    blue_channel, green_channel,red_channel = cv2.split(img)
    red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
    win= cv2.merge((blue_channel, green_channel, red_channel))
    return win

a10=Winter(image)
def dodge(x,y):
    return cv2.divide(x,255-y,scale=256)

#beuriful sketch lmao
image_invert=cv2.bitwise_not(greyscale(image))
img_smooth= cv2.GaussianBlur(image_invert,(21,21),sigmaX=0,sigmaY=0)


final_image =dodge(greyscale(image),img_smooth)
cv2.imshow("sketch",final_image)
cv2.waitKey()
cv2.destroyAllWindows()




