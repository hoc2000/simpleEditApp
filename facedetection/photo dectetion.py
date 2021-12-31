import cv2.cv2 as cv2
import dlib
from math import hypot

image = cv2.imread("sample/pewdiepie.png")
image_resize=cv2.resize(image,(800,800))
nose_image = cv2.imread("sample/dog_nose.png")

image_gray= cv2.cvtColor(image_resize,cv2.COLOR_BGR2GRAY)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

faces= detector(image_gray)
for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
    # cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)

    landmarks = predictor(image_gray, face)
    top_nose = (landmarks.part(29).x, landmarks.part(29).y)
    center_nose = (landmarks.part(30).x, landmarks.part(30).y)
    left_nose = (landmarks.part(31).x, landmarks.part(31).y)
    right_nose = (landmarks.part(35).x, landmarks.part(35).y)

    # tính độ dài
    nose_width = int(hypot(left_nose[0] - right_nose[0],
                           left_nose[1] - right_nose[1]) *6)
    # tính hệ số cho height bằng cách lấy độ dài ảnh chia cho width
    nose_height = int(nose_width)

    top_left = (int(center_nose[0] - nose_width / 2),
                int(center_nose[1] - nose_height / 2))
    bottom_right = (int(center_nose[0] + nose_width / 2),
                    int(center_nose[1] + nose_height / 2))

    # cv2.rectangle(re_frame,(int(center_nose[0]-nose_width/2),
    #                         int(center_nose[1]-nose_height/2)),
    #                         (int(center_nose[0]+nose_width/2),
    #                          int(center_nose[1]+nose_height/2)),
    #                     (0.255,0),2)

    nose_dog = cv2.resize(nose_image, (nose_width, nose_height))
    nose_gray = cv2.cvtColor(nose_dog, cv2.COLOR_BGR2GRAY)
    _, nose_mask = cv2.threshold(nose_gray, 25, 255, cv2.THRESH_BINARY_INV)

    nose_area = image_resize[top_left[1]:top_left[1] + nose_height,
                top_left[0]:top_left[0] + nose_width]
    nose_are_no_nose = cv2.bitwise_and(nose_area, nose_area, mask=nose_mask)
    final_nose = cv2.add(nose_are_no_nose, nose_dog)

    image_resize[top_left[1]:top_left[1] + nose_height,
    top_left[0]:top_left[0] + nose_width] = final_nose

    # print(landmarks)
    # for n in range(0, 68):
    #     x = landmarks.part(n).x
    #     y = landmarks.part(n).y
    #     cv2.circle(image_resize, (x, y), 4, (255, 0, 0), -1)

cv2.imshow("lmao",image_resize)
cv2.waitKey()
cv2.destroyAllWindows()