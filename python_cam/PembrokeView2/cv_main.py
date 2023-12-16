import cv2
import cvzone
import numpy as np
import pickle

x1, y1 = 53, 50
start_point = (x1, y1)
x2, y2 = 80, 80
end_point = (x2, y2)
color = (454, 323)
thickness = 2


width, height = x2 - x1, y2 - y1
def video_looper():
	if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
		cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

def check_for_parking_space(processed_image):
  space_counter = 0
  for position in position_list:
    x, y = position
    
    cropped_image = processed_image[y:y + height, x:x + width]     
# show individual parking spaces    		
    # cv2.imshow(str(x*y), cropped_image)

# get the pixel count
    pixel_counter = cv2.countNonZero(cropped_image)
    count = cv2.countNonZero(cropped_image)


    if count < 900:
        color = (0, 255, 0)
        thickness = 2
        space_counter += 1
        print(space_counter)
    else:
        color = (0, 0, 255)
        thickness = 2
        
    cv2.rectangle(img, position, (position[0] + width, position[1] + height), color, thickness)
    cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,
                        thickness=2, offset=0, colorR=(0, 0, 255))

  cvzone.putTextRect(img, f'Free: {space_counter}/{len(position_list)}', (100, 50), scale=3,
                           thickness=5, offset=20, colorR=(0,200,0))

location = "PembrokeView2"    
with open(f"{location}_parking_data", 'rb') as f:
    position_list = pickle.load(f)

video_source = "https://s58.nysdot.skyvdn.com:443/rtplive/TA_191/playlist.m3u8"
cap = cv2.VideoCapture(video_source)
brightness_factor = 80 
while True:
  # video_looper()

  success, img = cap.read()
  img = cv2.add(img, np.full_like(img, brightness_factor, dtype=np.uint8))
# blur image
  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  img_blur = cv2.GaussianBlur(img_gray, (3, 3), 1)
# convert image to binary
  img_threshold = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
  img_median = cv2.medianBlur(img_threshold, 5)
  kernel = np.ones((3, 3), np.uint8)
  img_dilate = cv2.dilate(img_median, kernel, iterations=1)   

  check_for_parking_space(img_dilate)

  # the view of each parking spot
  # for position in position_list:
  #   cv2.rectangle(img, position, (position[0] + width, position[1] + height), (255,0,255), 2) 


  cv2.imshow("Image", img)
  cv2.imshow("imgThreshold", img_dilate)
  cv2.waitKey(1)