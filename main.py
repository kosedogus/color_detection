import cv2
from utils import get_limits 
from PIL import Image

blue = [255, 0, 0]
cap = cv2.VideoCapture(0)
cap.set(10,0)
while True:
    ret, frame = cap.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, get_limits(blue)[0], get_limits(blue)[1])
    mask_ = Image.fromarray(mask)
    bounding_box = mask_.getbbox()
    if bounding_box:
        x, y, w, h = bounding_box
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()