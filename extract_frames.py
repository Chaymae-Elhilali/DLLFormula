from datetime import timedelta
import cv2
import numpy as np
import os

SAVING_FRAMES_PER_SECOND = 10

def format_timedelta(td):
    """Utility function to format timedelta objects in a cool way (e.g 00:00:20.05) 
    omitting microseconds and retaining milliseconds"""
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return (result + ".00").replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")

def get_saving_frames_durations(cap, saving_fps):
    """A function that returns the list of durations where to save the frames"""
    s = []
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    if frame_count == 0 or fps == 0:
        return s

    clip_duration = frame_count / fps

    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s

def main(video_file):
    filename, _ = os.path.splitext(video_file)
    filename += "-opencv"
    if not os.path.isdir(filename):
        os.mkdir(filename)

    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        print("Error opening video file:", video_file)
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    saving_frames_per_second = min(fps, SAVING_FRAMES_PER_SECOND)
    saving_frames_durations = get_saving_frames_durations(cap, saving_frames_per_second)

    count = 0
    while True:
        is_read, frame = cap.read()
        if not is_read:
            break

        frame_duration = count / fps
        frame2= frame

        try:
            closest_duration = saving_frames_durations[0]
        except IndexError:
            break

        if frame_duration >= closest_duration:
            frame_duration_formatted = format_timedelta(timedelta(seconds=frame_duration))
            cv2.imwrite(os.path.join(filename, f"frame{frame_duration_formatted}.jpg"), frame)
            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass

        count += 1

    cap.release()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please provide a video file as an argument.")
    else:
        video_file = sys.argv[1]
        main(video_file)
