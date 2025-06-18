import cv2

# --- CONFIGURATION ---
# For DroidCam USB (virtual camera), set DEVICE_INDEX to the correct index.
# Usually 1 or 2, but may be 0 if no other cameras are present.
# If you see only a green screen, make sure the DroidCam Windows client is running and streaming video.

DEVICE_INDEX = 0  # Change to 1, 2, etc. if needed

cap = cv2.VideoCapture(DEVICE_INDEX) # Open the video source to grap frames from
window_title = "DroidCam Virtual Camera (USB)"

if not cap.isOpened():
    print("Error: Could not open video source.\n"
          "- Try changing DEVICE_INDEX.\n"
          "- Make sure DroidCam client is running and streaming video.\n"
          "- Check that the DroidCam virtual camera driver is installed and enabled.")
    exit(1)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. If you see a green window, the virtual camera is open but not streaming video.")
        break

    cv2.imshow(window_title, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
