.p#this code creates the folder with all the label files
#It includes detection so no need to use yolov8 command

import os
from roboflow import Roboflow
rf = Roboflow(api_key="6JdS3fk367XrDxgtvhiS")
project = rf.workspace().project("formula-detector-egybi")
model = project.version(8).model

if len(sys.argv) != 2:
    print("Usage: python3 label.py <folderName>")
    sys.exit(1)

folder_name = sys.argv[1]
folder_path = os.path.join("/content/DLLFormula/data/output_frames", folder_name)
labels_folder_path = os.path.join("/content/DLLFormula/datasets/runs/detect/", folder_name + "_labels")
os.makedirs(labels_folder_path, exist_ok=True)


# Iterate over all files in the directory
for filename in os.listdir(folder_path):
  file_path = os.path.join(folder_path, filename)
  result = model.predict(file_path, confidence=50, overlap=50)


# Build the label file path within the labels folder
label_file_path = os.path.join(labels_folder_path, os.path.splitext(filename)[0] + ".txt")

# Write the prediction line in the label file
with open(label_file_path, 'w') as label_file:
  for prediction in result:
    x = prediction['x']
    y = prediction['y']
    width = prediction['width']
    height = prediction['height']
    class_label = prediction['class']
    label_file.write(f"{class_label} {x} {y} {width} {height}\n")

#pop empty last line in label file
def process_last_line(path):
    """input : path containing ur text files"""
    list_paths=[file for file in os.listdir(path) if file.endswith('.txt')]
    for filename in list_paths:

        with open(path+"/"+filename, 'r+') as fp:
            # read an store all lines into list
            lines = fp.readlines()
            lines[-1]=lines[-1].replace('\n','')

            fp.seek(0)
            fp.truncate()

            fp.writelines(lines)

process_last_line(labels_folder_path)
