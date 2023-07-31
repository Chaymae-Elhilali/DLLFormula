import sys
import cv2

def save_frame_from_video(video_path, timing, output_path):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Video file not found or cannot be opened.")
        return
    
    # Calculate frame rate of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Calculate the frame number corresponding to the specified timing
    frame_number = int(timing * fps)
    
    # Set the video capture to the specified frame number
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    
    # Read the frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame at the specified timing.")
        return
    
    # Save the frame as an image
    cv2.imwrite(output_path, frame)
    
    # Release the video capture object
    cap.release()
    print(f"Frame at time {timing:.2f} seconds saved as {output_path}.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python save_frame.py video_path timing output_image_path")
    else:
        video_path = sys.argv[1]
        timing = float(sys.argv[2])
        output_image_path = sys.argv[3]
        save_frame_from_video(video_path, timing, output_image_path)
