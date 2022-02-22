import cv2.cv2 as cv2
import dlib
from math import hypot

image = cv2.imread("sample/cute_girl.jpg")
image_resize=cv2.resize(image,(800,800))
eye_image = cv2.imread("snapchat/left eye.png")
eye2_image=cv2.imread("snapchat/right eye.png")

image_gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

faces= detector(image_gray)
for face in faces:

    landmarks = predictor(image_gray, face)
    # top_nose = (landmarks.part(27).x, landmarks.part(29).y)
    center_eye1 = (landmarks.part(37).x, landmarks.part(37).y)
    left_eye1 = (landmarks.part(36).x, landmarks.part(36).y)
    right_eye1 = (landmarks.part(39).x, landmarks.part(39).y)

    # tính độ dài
    eye1_width = int(hypot(left_eye1[0] - right_eye1[0],
                           left_eye1[1] - right_eye1[1]) *2.4)
    # tính hệ số cho height bằng cách lấy độ dài ảnh chia cho width
    eye1_height = int(eye1_width*0.5)

    top_left_eye1 = (int(center_eye1[0] - eye1_width / 2),
                int(center_eye1[1] - eye1_height / 2))
    bottom_right_eye1 = (int(center_eye1[0] + eye1_width / 2),
                    int(center_eye1[1] + eye1_height / 2))


    eye1 = cv2.resize(eye_image, (eye1_width, eye1_height))
    eye1_gray = cv2.cvtColor(eye1, cv2.COLOR_BGR2GRAY)
    _, nose_mask = cv2.threshold(eye1_gray, 25, 255, cv2.THRESH_BINARY_INV)

    eye1_area = image[top_left_eye1[1]:top_left_eye1[1] + eye1_height,
                top_left_eye1[0]:top_left_eye1[0] + eye1_width]
    nose_are_no_nose = cv2.bitwise_and(eye1_area, eye1_area, mask=nose_mask)
    final_eye1 = cv2.add(nose_are_no_nose, eye1)

#mắt phải
    center_eye2 = (landmarks.part(44).x, landmarks.part(44).y)
    left_eye2 = (landmarks.part(42).x, landmarks.part(42).y)
    right_eye2 = (landmarks.part(45).x, landmarks.part(45).y)

    # tính độ dài
    eye2_width = int(hypot(left_eye2[0] - right_eye2[0],
                           left_eye2[1] - right_eye2[1]) *2.4)
    # tính hệ số cho height bằng cách lấy độ dài ảnh chia cho width
    eye2_height = int(eye2_width * 0.5)

    top_left_eye2 = (int(center_eye2[0] - eye2_width / 2),
                int(center_eye2[1] - eye2_height / 2))
    bottom_right = (int(center_eye2[0] + eye2_width / 2),
                    int(center_eye2[1] + eye2_height / 2))

    eye2 = cv2.resize(eye2_image, (eye2_width, eye2_height))
    eye2_gray = cv2.cvtColor(eye2, cv2.COLOR_BGR2GRAY)
    _, nose_mask = cv2.threshold(eye2_gray, 25, 255, cv2.THRESH_BINARY_INV)

    eye2_area = image[top_left_eye2[1]:top_left_eye2[1] + eye2_height,
                top_left_eye2[0]:top_left_eye2[0] + eye2_width]
    nose_are_no_nose = cv2.bitwise_and(eye2_area, eye2_area, mask=nose_mask)
    final_eye2 = cv2.add(nose_are_no_nose, eye2)





    image[top_left_eye1[1]:top_left_eye1[1] + eye1_height,
    top_left_eye1[0]:top_left_eye1[0] + eye1_width] = final_eye1

    image[top_left_eye2[1]:top_left_eye2[1] + eye2_height,
    top_left_eye2[0]:top_left_eye2[0] + eye2_width] = final_eye2


    # print(landmarks)
    # for n in range(0, 68):
    #     x = landmarks.part(n).x
    #     y = landmarks.part(n).y
    #     cv2.circle(image_resize, (x, y), 4, (255, 0, 0), -1)

cv2.imshow("lmao",image)
cv2.waitKey()
cv2.destroyAllWindows()