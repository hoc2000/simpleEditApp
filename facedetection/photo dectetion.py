import cv2.cv2 as cv2
import dlib

image = cv2.imread("sample/pewdiepie.png")

image_gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

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
    print(landmarks)
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.circle(image, (x, y), 4, (0, 0, 255), -1)

cv2.imshow("lmao",image)
cv2.waitKey()
cv2.destroyAllWindows()