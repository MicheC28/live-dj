import cv2
from deepface import DeepFace
import time



#hello - testing repo


# Load the face cascade classifier
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Open webcam
capture = cv2.VideoCapture(0)
if not capture.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = capture.read()
    if not ret:
        print("Failed to grab frame")
        break

    try:
        # Analyze the frame for emotion
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        dominant_emotion = result[0]['dominant_emotion'] if result else "No face"
    except ValueError as e:
        dominant_emotion = "No face detected"

    print(dominant_emotion)

    # Convert the frame to grayscale for face detection
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # faces = faceCascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles around detected faces
    # for (x, y, w, h) in faces:
        # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the dominant emotion
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(frame, dominant_emotion, (50, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Show the frame
    # cv2.imshow('Original Video', frame)

    # time.sleep(2)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

# Release the capture and destroy all OpenCV windows

# ret, frame = capture.read()
# if not ret:
#     print("Failed to grab frame")

# try:
#     # Analyze the frame for emotion
#     result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
#     dominant_emotion = result[0]['dominant_emotion'] if result else "No face"
# except ValueError as e:
#     dominant_emotion = "No face detected"

# print(dominant_emotion)


capture.release()
cv2.destroyAllWindows()
