from ultralytics import YOLO
import cv2
import cvzone
import math



capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)
model = YOLO("./yolo_weights/yolov8l.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush", "eye glasses"
              ]





while True:
  success, img = capture.read()
  results = model(img, stream=True)
  for result in results:
    boxes = result.boxes
    for box in boxes:
      x1, y1, x2, y2 = box.xyxy[0]
      x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

      confidence = math.ceil((box.conf[0]*100))/100

      # print(x1, y1, x2, y2)
      print(confidence)
      cls = int(box.cls[0])
      print(classNames[cls])
      cvzone.putTextRect(img, f"{classNames[cls]} {confidence}", (x1, y1-35), scale=1, thickness=1)
      # box.xywh

      cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
  cv2.imshow('Image', img)
  cv2.waitKey(1)




# result = model('Images/trucklot.png', show=True)
# cv2.waitKey(0)


