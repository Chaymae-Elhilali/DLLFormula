import os
import cv2
import sys

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
        H, W, _ = frame.shape

        # Get the bounding box data for the current frame
        with open(bbox_path, 'r') as bbox_file:
            bbox_data = bbox_file.readlines()

        # Iterate over each bounding box
        for i, bbox_line in enumerate(bbox_data):
            try:
                # Parse the bounding box data
                bbox_values = bbox_line.strip().split()
                class_label = bbox_values[0]
                mean_x, mean_y, mean_width, mean_height = map(float, bbox_values[1:])

                # Calculate the top-left and bottom-right coordinates of the bounding box
                x1 = int((mean_x - (mean_width / 2)) * W)
                y1 = int((mean_y - (mean_height / 2)) * H)
                x2 = int((mean_x + (mean_width / 2)) * W)
                y2 = int((mean_y + (mean_height / 2)) * H)

                # Crop the bounding box region from the frame
                cropped = frame[y1:y2, x1:x2]

                # Generate the output filename
                output_filename = f"{os.path.splitext(frame_file)[0]}_{i}.jpg"
                output_path = os.path.join(chemin_boxes, output_filename)

                # Save the cropped image
                if cropped.shape[0] > 0 and cropped.shape[1] > 0:
                    cv2.imwrite(output_path, cropped)

            except ValueError:
                print(f"Error parsing line {i+1} in the bounding box file: {bbox_line}")

        print(f"Cropped images for {frame_file} saved.")

    print("All frames processed.")

if len(sys.argv) != 2:
    print("Usage: python3 label.py <folderName>")
    sys.exit(1)

folder_name = sys.argv[1]
chemin_img = os.path.join("/content/DLLFormula/data/output_frames", folder_name)
chemin_labels = os.path.join("/content/DLLFormula/datasets/runs/detect/", folder_name + "_labels")
chemin_boxes = os.path.join("/content/DLLFormula/datasets/runs/boxes/", folder_name)
os.makedirs(chemin_boxes, exist_ok=True)

# Call the function to save cropped images
save_cropped_images(chemin_img, chemin_labels, chemin_boxes)
