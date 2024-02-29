import cv2
import os

# Path to your video file
video_path = 'logan_throwingLeft_4k-60.mp4'

# Directory where you want to save the frames
frames_dir = 'facial_reck_image'
os.makedirs(frames_dir, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(video_path)

frame_count = 0
while True:
    # Read frame by frame
    success, frame = cap.read()
    if not success:
        break  # No more frames or error

    # Save each frame to the directory
    frame_path = os.path.join(frames_dir, f"frame_{frame_count:04d}.jpg")
    cv2.imwrite(frame_path, frame)
    frame_count += 1

cap.release()  # Release the video capture object

print(f"Extracted {frame_count} frames and saved to {frames_dir}")
