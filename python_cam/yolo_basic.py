from ultralytics import YOLO
import cv2
# large
# model = YOLO("./yolo_weights/yolov8l.pt")
# medium
model = YOLO("./yolo_weights/yolov8l.pt")
# nano
print("Hag")

# model = YOLO("./yolo_weights/yolov8n.pt")
results = model.predict('https://s58.nysdot.skyvdn.com:443/rtplive/TA_182/playlist.m3u8', show=True)


result = results[0]
box = result.boxes[0]

print("Object type:", box.cls)
print("Coordinates:", box.xyxy)
print("Probability:", box.conf)



cv2.waitKey(0)


