import cv2.cv2 as cv2
import dlib

camera_id = 'sample/woman.mp4'
# mở camera
cap = cv2.VideoCapture(camera_id)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

dim = (1200, 700)

while (1):
    # đọc từng frame
    _, frame = cap.read()

    re_frame = cv2.resize(frame, dim)
    gray = cv2.cvtColor(re_frame, cv2.COLOR_BGR2GRAY)
    # detector face
    faces = detector(gray)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(re_frame,(x1,y1),(x2,y2),(0,255,0),3)

        landmarks = predictor(gray, face)
        print(landmarks)
        for n in range (0,68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(re_frame, (x, y), 4, (0, 0, 255), -1)

    cv2.imshow("camera", re_frame)

    key= cv2.waitKey(1)
    if key == 27:
        break
# giải phóng camera
cap.release()
cv2.destroyAllWindows()
