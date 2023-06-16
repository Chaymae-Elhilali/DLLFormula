#made with the help of chatgpt

import os
import cv2

def save_cropped_images(chemin_img, chemin_labels, chemin_boxes):
    # Create the output directory if it doesn't exist
    if not os.path.exists(chemin_boxes):
        os.makedirs(chemin_boxes)

    # Load the list of frames from chemin
    frame_files = os.listdir(chemin_img)
    bbox_files = os.listdir(chemin_labels)

    # Sort the frames by name (if necessary)
    frame_files.sort()
    bbox_files.sort()

    # Iterate over each frame
    for frame_file, bbox_file in zip(frame_files, bbox_files):
        frame_path = os.path.join(chemin_img, frame_file)
        bbox_path = os.path.join(chemin_labels, bbox_file)

        # Load the frame image
        frame = cv2.imread(frame_path)

        # Get the bounding box data for the current frame
        with open(chemin_labels, 'r') as bbox_file:
            bbox_data = bbox_file.readlines()

        # Iterate over each bounding box
        for i, bbox_line in enumerate(bbox_data):
            # Parse the bounding box data
            class_label, mean_x, mean_y, mean_width, mean_height = map(float, bbox_line.strip().split())

            # Calculate the top-left and bottom-right coordinates of the bounding box
            x1 = int(mean_x - mean_width / 2)
            y1 = int(mean_y - mean_height / 2)
            x2 = int(mean_x + mean_width / 2)
            y2 = int(mean_y + mean_height / 2)

            # Crop the bounding box region from the frame
            cropped = frame[y1:y2, x1:x2]

            # Generate the output filename
            output_filename = f"{os.path.splitext(frame_file)[0]}_{i}.jpg"
            output_path = os.path.join(chemin_boxes
        , output_filename)

            # Save the cropped image
            cv2.imwrite(output_path, cropped)

        print(f"Cropped images for {frame_file} saved.")

    print("All frames processed.")


# Specify the paths
chemin_img = "/content/datasets/Formula-detector-7/test/images"
chemin_labels = "/content/datasets/Formula-detector-7/test/labels"
chemin_boxes = "/content/datasets/Formula-detector-7/test/boxes"
os.makedirs(chemin_boxes)

# Call the function to save cropped images
save_cropped_images(chemin_img, chemin_labels, chemin_boxes)
