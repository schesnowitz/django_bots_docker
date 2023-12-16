from ultralytics import YOLO
import cv2
import cvzone
import math

model = YOLO("./yolo_weights/yolov8l.pt")


camera_url = "https://s58.nysdot.skyvdn.com:443/rtplive/TA_182/playlist.m3u8"


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

cap = cv2.VideoCapture(camera_url)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 740)
# cap.set(3, 1280)
# cap.set(4, 720)
# vwidth  = cap.get(3)
# vheight = cap.get(4)
# print(vwidth, vheight)
model = YOLO("./yolo_weights/yolov8x.pt")
# mask = cv2.imread("./images/1.png")
mask = cv2.imread("Chittengango/images/the_mask.png")

resize = cv2.resize(mask, (512, 288))
while True:
    success, video = cap.read()
    video_mask = cv2.bitwise_and(video, resize)
    # print(video_mask)
    results = model(video_mask, stream=True)

    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
# draw rectangle around object
            # cv2.rectangle(video, (x1, y1), (x2, y2), color=(255, 0, 255), thickness=1)
            # print(x1, y1, x2, y2)

            w, h = x2 - x1, y2 - y1
            print(len(boxes))
# get confidence
            confidence = math.ceil((box.conf[0]*100))/100
            # print(confidence)
# get class
            cls = int(box.cls[0])

# cvzone rectangle
            cvzone.cornerRect(video, (x1, y1, w, h), t=1)
# confidence text
            cvzone.putTextRect(video, f"{classNames[cls] } {confidence} ", pos=(
                x1, y1-15), scale=0.8, thickness=1)

# confidence and class name text

    # cv2.imwrite("image.jpg", video)
    cv2.imshow("Video", video)
    cv2.imshow("video_mask", video_mask)
    cv2.waitKey(1)
