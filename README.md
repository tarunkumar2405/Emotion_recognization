Emotion Recognition from IP Camera Feed

This project demonstrates real-time facial emotion recognition using an IP camera feed. The facial_emotion_recognition library is utilized to analyze frames and identify emotions, displaying the results directly on the video feed.

Features

Real-time emotion recognition.

Integration with IP camera feed.

Display of detected emotions on the video feed.

Lightweight implementation using the facial_emotion_recognition library.

Prerequisites

To run this project, ensure you have the following installed:

Python 3.6 or higher.

Required Python libraries:

facial_emotion_recognition

opencv-python

numpy

imutils

An IP camera with a valid stream URL.

Installation

Clone or download this repository to your local machine.

git clone https://github.com/your-repo/emotion-recognition-ip-camera.git
cd emotion-recognition-ip-camera

Install the required libraries:

pip install facial_emotion_recognition opencv-python numpy imutils

Usage

Set up your IP camera and note its stream URL. For instance, if you’re using an IP webcam app on your phone, the URL might look like:

http://192.168.1.34:8080/shot.jpg

Update the url variable in the script with your camera's URL:

url = 'http://192.168.1.34:8080/shot.jpg'

Run the script:

python emotion_recognition.py

Press Esc to exit the application.

Code Overview

Dependencies

facial_emotion_recognition: For detecting facial emotions.

opencv-python: For video processing and frame handling.

numpy: For numerical operations.

imutils: For easier frame manipulation.

urllib.request: For accessing the IP camera stream.

Main Script

Initialize Emotion Recognition:

er = EmotionRecognition(device='cpu')

Access IP Camera Feed:

imgPath = urllib.request.urlopen(url)
imgNp = np.array(bytearray(imgPath.read()), dtype=np.uint8)
frame = cv2.imdecode(imgNp, -1)

Process and Display Emotion:

frame = er.recognise_emotion(frame, return_type='BGR')
cv2.putText(frame, "Emotion: ", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
cv2.imshow("Frame", frame)

Clean Up:

cam.release()
cv2.destroyAllWindows()

Customization

Emotion Label Placement: Adjust the coordinates in cv2.putText to change where the emotion label appears.

Camera Feed Resolution: Resize the frame for consistent dimensions using OpenCV functions, such as cv2.resize.

Device Selection: Use GPU for better performance by setting device='cuda' in EmotionRecognition.

Troubleshooting

Camera Connection Issues: Ensure the IP camera is on the same network and its URL is accessible.

Dependency Errors: Verify that all required libraries are installed and compatible with your Python version.

Emotion Recognition Accuracy: Ensure proper lighting and clear visibility of faces in the camera feed.

Future Enhancements

Support for multiple faces in a single frame.

Integration with cloud storage to save detected emotions for further analysis.

Enhanced visualization with graphical overlays.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

The facial_emotion_recognition library for providing an easy-to-use emotion detection solution.

OpenCV for powerful image and video processing capabilities.

Community resources and tutorials that inspired this implementation.


