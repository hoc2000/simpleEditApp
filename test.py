import cv2.cv2 as cv2
import numpy as np
from scipy.interpolate import UnivariateSpline

# Read the image
image = cv2.imread('sample/girl xinh.jpg')


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
    return hdr


a8 = HDR(image)


def LookupTable(x, y):
    spline = UnivariateSpline(x, y)
    return spline(range(256))


# summer effect
def Summer(img):
    increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    blue_channel, green_channel, red_channel = cv2.split(img)
    red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
    sum = cv2.merge((blue_channel, green_channel, red_channel))
    return sum


# winter effect
def Winter(img):
    increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    blue_channel, green_channel, red_channel = cv2.split(img)
    red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
    win = cv2.merge((blue_channel, green_channel, red_channel))
    return win


def Instant(img):
    red_img = np.full((682, 512, 3), (110, 120, 0), np.uint8)
    width = int(img.shape[1])
    height = int(img.shape[0])
    dim = (width, height)
    red = cv2.resize(red_img, dim)
    fused_img = cv2.addWeighted(img, 0.8, red, 0.2, 0.0)
    return fused_img


def dodge(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def glitch_add(img):
    foreg = cv2.imread("sample/glitch.jpg")
    width = int(img.shape[1])
    height = int(img.shape[0])
    dim = (width, height)
    fg=cv2.resize(foreg, dim)
    blend = cv2.addWeighted(img, 0.8, fg, 0.6, 0.0)
    crop_img = img[30:4, (width-4):(height-4)]
    return blend
photo =glitch_add(image)

cv2.imshow("test",photo)
cv2.waitKey()
cv2.destroyAllWindows()








# # linear
# def ColourQuantization(img, K=9):
#     Z = img.reshape((-1, 3))
#     Z = np.float32(Z)
#     criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
#     compactness, label, center = cv2.kmeans(Z, K, None, criteria, 1, cv2.KMEANS_RANDOM_CENTERS)
#     center = np.uint8(center)
#     res = center[label.flatten()]
#     res2 = res.reshape((img.shape))
#     return res2
#
#
# def Countours(img):
#     contoured_image = img
#     gray = cv2.cvtColor(contoured_image, cv2.COLOR_BGR2GRAY)
#     edged = cv2.Canny(gray, 200, 200)
#     contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2:]
#     cv2.drawContours(contoured_image, contours, contourIdx=-1, color=6, thickness=1)
#     return contoured_image
#
#
# coloured = ColourQuantization(image)
# contoured = Countours(coloured)
#
# edit=contoured
# final_image = glitch_add(image)
#
# cv2.imshow("sketch", final_image)
# cv2.waitKey()
# cv2.destroyAllWindows()
