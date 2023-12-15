import cv2
from PIL import Image
from util import get_limits

warna = [0, 255, 255]  # yellow in BGR colorspace
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Membalikkan frame secara horizontal
    frame = cv2.flip(frame, 1)

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=warna)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
