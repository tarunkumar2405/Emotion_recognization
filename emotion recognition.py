from facial_emotion_recognition import EmotionRecognition
import urllib.request
import cv2
import numpy as np
import imutils

er = EmotionRecognition(device='cpu')

url = 'http://192.168.1.35:8080/shot.jpg'

while True:
    imgPath = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgPath.read()), dtype=np.uint8)
    frame = cv2.imdecode(imgNp, -1)

    # Recognize emotions
    frame = er.recognise_emotion(frame, return_type='BGR')

    # Enlarge emotion labels for better visibility
    cv2.putText(frame, "Emotion: ", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
