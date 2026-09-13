import cv2

video = cv2.VideoCapture("videos/abrahamtrainingtest.mov")

#video information
fps = video.get(cv2.CAP_PROP_FPS)
width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("FPS:", fps)
print("Width:", width)
print("Height:", height)

while True:
    success, frame = video.read()

    if not success:
        break

    #draw rectangle
    cv2.rectangle(frame, (100, 100), (400, 300), (0, 255, 0), 2)

    #draw circle
    cv2.circle(frame, (250, 200), 10, (0, 0, 255), -1)

    cv2.imshow("Test Video", frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()