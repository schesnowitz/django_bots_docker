import cv2
import numpy as np

cap  = cv2.imread('https://s58.nysdot.skyvdn.com:443/rtplive/TA_191/playlist.m3u8')





# Define a brightness factor (adjust as needed)
brightness_factor = 50  # You can experiment with different values

while True:
    ret, frame = cap.read()
    
    # If we've reached the end of the video, exit the loop
    if not ret:
        break
    
    # Ensure that both frame and brightness_factor have the same data type (np.uint8)
    frame = frame.astype(np.uint8)
    brightness_factor = np.uint8(brightness_factor)
    
    # Add the brightness factor to each pixel
    brightened_frame = cv2.add(frame, brightness_factor)

    # Display the original and brightened frames
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Brightened Frame', brightened_frame)
    
    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video object and close windows
cap.release()
cv2.destroyAllWindows()
