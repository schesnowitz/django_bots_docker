import cv2.cv2 as cv2
import pickle

image_path = "Chittengango\image.png"
img = cv2.imread(image_path)

x1, y1 = 50, 50
start_point = (x1, y1)
x2, y2 = 80, 80
end_point = (x2, y2)
color = (454, 323)
thickness = 1

width, height = x2 - x1, y2 - y1
# print(width, height)


try:
    with open("chittengango_pickle", 'rb') as f:
        position_list = pickle.load(f)
except:
    position_list = []

    
def mouse_click(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        position_list.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, position in enumerate(position_list):
            x1, y1 = position
            if x1 < x < x1 + width and y1 < y < y1 + height:
                position_list.pop(i)

    with open("chittengango_pickle", 'wb') as f:
        pickle.dump(position_list, f)

# def get_mouse_input():
#   cv2.setMouseCallback("Image")

while True:
    img = cv2.imread(image_path)

    for position in position_list:
        cv2.rectangle(
            img, position, (position[0] + width, position[1] + height), color, thickness)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouse_click)
    cv2.waitKey(1)
