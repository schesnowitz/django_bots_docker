from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import *


capture = cv2.VideoCapture("./Videos/cars.mp4")
# can't set size for video feed
# capture.set(3, 1280)
# capture.set(4, 720)
model = YOLO("./yolo_weights/yolov8n.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "dining table", "toilet", "tv monitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush", "eye glasses"
              ]


# read in the image mask
mask = cv2.imread("./Images/carmask.png")
# place line for cars to cross over 
line_limit = [150, 500, 690, 500]
# Tracker 
tracker = Sort(max_age=20 , min_hits=3 , iou_threshold=0.3)
car_count = []
while True:
  success, img = capture.read()
  image_region = cv2.bitwise_and(img, mask)
  results = model(image_region, stream=True)
  detections = np.empty((0, 5))


  for result in results:
    boxes = result.boxes
    for box in boxes:
      x1, y1, x2, y2 = box.xyxy[0]
      x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

      confidence = math.ceil((box.conf[0]*100))/100

      cls = int(box.cls[0])

      objClass = classNames[cls]

      if objClass == "car" or objClass == "truck" and confidence > 0.30:
        # cvzone.putTextRect(img, f"{objClass} {confidence}", (x1, y1-35), scale=1, thickness=1)


        # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        currentArray = np.array([x1, y1, x2, y2, confidence])
        detections = np.vstack((detections, currentArray))


        tracker_results = tracker.update(detections)    
        cv2.line(img, (line_limit[0], line_limit[1]), (line_limit[2], line_limit[3]), (0,0,255), 5)  

        for result in tracker_results:
          x1, y1, x2, y2, id = result
          x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
          print(result)
          w, h = x2 - x1, y2  - y1
          # cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt = 2, colorR=(255, 0, 0)) 
          cvzone.putTextRect(img, f"{objClass} {int(id)}", (x1, y1-35), scale=1, thickness=1)


          centerX, centerY = x1+w//2, y1+h//2

          cv2.circle(img, (centerX, centerY), 5, (0,0,255), cv2.FILLED)

          if line_limit[0] < centerX < line_limit[2] and line_limit[1] - 30 < centerY < line_limit[1] + 30:

            if car_count.count(id) == 0:
              car_count.append(id)
            print(car_count)
  cvzone.putTextRect(img, f"Count {len(car_count)}", (50, 50))

  cv2.imshow('Image', img)
  # cv2.imshow('image_region', image_region)
  cv2.waitKey(1)

 


# result = model('Images/trucklot.png', show=True)
# cv2.waitKey(0)


