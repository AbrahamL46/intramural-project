import cv2

video = cv2.VideoCapture("videos/abrahamtrainingtest.mov")

while True:
    success, frame = video.read()

    if not success:
        break

    cv2.imshow("Test Video", frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()