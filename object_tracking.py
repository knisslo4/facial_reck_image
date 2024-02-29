import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture('/clips/baseball_slowMo_hd-240.mp4')

while True:
    # Read video frame by frame
    ret, frame = cap.read()
    
    if not ret:
        break  # If no frame is read then break the loop

    # Show the frame
    cv2.imshow('Video Frame', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

def detect_baseball(frame):
    # Convert frame to HSV (Hue, Saturation, Value) color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define the color range for detecting the baseball
    # These values depend on the color of the baseball and lighting conditions
    lower_color = np.array([0, 0, 200])  # Example values
    upper_color = np.array([180, 25, 255])  # Example values
    
    # Threshold the HSV image to get only the colors of the baseball
    mask = cv2.inRange(hsv, lower_color, upper_color)
    
    # Optional: perform morphological operations to clean up the mask
    # mask = cv2.erode(mask, None, iterations=2)
    # mask = cv2.dilate(mask, None, iterations=2)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Find the largest contour, assuming it's the baseball
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)
        
        # Only proceed if the radius meets a minimum size
        if radius > 10:  # Example threshold
            # Draw the circle on the frame
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
    
    return frame

# Video capture
cap = cv2.VideoCapture('*baseball_tracking_slowMo_hd-240.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detect the baseball
    frame = detect_baseball(frame)
    
    # Show the frame
    cv2.imshow('Baseball Tracking', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
