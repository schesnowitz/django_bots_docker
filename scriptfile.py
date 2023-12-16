from ultralytics import YOLO
import cv2
# large
# model = YOLO("./yolo_weights/yolov8l.pt")
# medium
model = YOLO("./yolo_weights/yolov8m.pt")
# nano
# model = YOLO("./yolo_weights/yolov8n.pt")
result = model('Images/trucklot.png', show=True)
cv2.waitKey(0)


