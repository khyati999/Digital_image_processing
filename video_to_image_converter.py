import cv2
import os


video_path = "./flowers.mp4"


output_folder = "frames"

try:
    
    os.makedirs(output_folder, exist_ok=True)

    cam = cv2.VideoCapture(video_path)

    fps = cam.get(cv2.CAP_PROP_FPS)

    frames_per_minute = int(fps * 60)    
    current_frame = 0

    while True:
        
        cam.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
        ret, frame = cam.read()

        if not ret:
            break

        frame_path = os.path.join(output_folder, f"frame{current_frame}.jpg")
        cv2.imwrite(frame_path, frame)

        current_frame += frames_per_minute

    cam.release()

    print("Frames captured successfully.")

except Exception as e:
    print(f"Error: {e}")
