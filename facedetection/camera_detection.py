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
    faces = detector(re_frame)
    for face in faces:
        landmarks= predictor



    cv2.imshow("camera", re_frame)

    key= cv2.waitKey(1)
    if key == 27:
        break
# giải phóng camera
cap.release()
cv2.destroyAllWindows()
