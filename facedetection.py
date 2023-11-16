import cv2
from picamera2 import Picamera2
import numpy as np

# Initialize Picamera2
picam2 = Picamera2()
config = picam2.create_video_configuration(main={"format": "XRGB8888", "size": (640, 480)})
picam2.configure(config)
picam2.start()

# Load the face detector
# Replace the path below with the actual path to your haarcascade_frontalface_default.xml file
face_detector = cv2.CascadeClassifier('/home/raspberryuser/haarcascade_frontalface_default.xml')

# Create an OpenCV window
cv2.namedWindow("Face Detection", cv2.WINDOW_NORMAL)

while True:
    # Capture frame-by-frame
    im = picam2.capture_array()
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(grey, 1.3, 5)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("Face Detection", im)

    # Break the loop with the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture and close windows
picam2.stop()
cv2.destroyAllWindows()
