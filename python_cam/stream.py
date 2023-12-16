import cv2

# Create a VideoCapture object using the stream URL
# https://s58.nysdot.skyvdn.com:443/rtplive/TA_041/playlist.m3u8
video_source = "./Videos/cars.mp4"
cap = cv2.VideoCapture(video_source)

# Check if the VideoCapture object is opened successfully./cars.mp4"
if not cap.isOpened():
    print("Could not open video stream")
    exit()

# Create a loop to read the frames from the video stream
while True:
    ret, frame = cap.read()

    # Check if the frame is read successfully
    if not ret:
        break

    # Display the frame using the imshow() function
    cv2.imshow("Frame", frame)

    # Wait for a key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
cap.release()

# Close all windows
cv2.destroyAllWindows()