# VideoToFrames

```
!pip install --upgrade opencv-python

!pip install opencv-python moviepy

!pip install scipy

!python3 extract_frames.py Arithmtique.mp4 #name_of_the_video
```

After the execution of the above command, a new folder "opencv-NameOfTheVideo" is created where you can find all the frames

Pour télécharger vidéo dll: afficher le code source du cadre, ouvrir le lien vimeo et utiliser l'extension professional video downloader

Now wer're done with the video to distinct frames part, let's now give our data the yolov8

# DETECTION
Now it's all ready we just need to take the directory to the frames and add it to the testing phase dataset as a source

 ## YOLOv8x
 ### Requirements
 ```
 !pip install ultralytics==8.0.20

 from IPython import display

 display.clear_output()

 import ultralytics
 
 ultralytics.checks()
 ```


YOLOv8 may be used directly in the Command Line Interface (CLI) with a yolo command:

```
yolo predict model=yolov8n.pt source='https://media.roboflow.com/notebooks/examples/dog.jpeg' save=True
```

yolo can be used for a variety of tasks and modes and accepts additional arguments, i.e. imgsz=640. See the YOLOv8 CLI Docs for examples.
### Usage

You can use YOLOv8 for object detection tasks using the Ultralytics pip package. The following is a sample code snippet showing how to use YOLOv8 models for inference:
 ```
from ultralytics import YOLO

# Load the model
model = YOLO('yolov8n.pt')  # load a pretrained model

# Perform inference
results = model('image.jpg')

# Print the results
results.print()
 ```

# CONVERSION

# ACKNOLEDGMENT:
code modified from:

- video to frames

- ocr latex converter: pix2tex - LaTeX OCR

- pre-pretreatment

- detection: @software{yolov8_ultralytics,
  author       = {Glenn Jocher and Ayush Chaurasia and Jing Qiu},
  title        = {YOLO by Ultralytics},
  version      = {8.0.0},
  year         = {2023},
  url          = {https://github.com/ultralytics/ultralytics},
  orcid        = {0000-0001-5950-6979, 0000-0002-7603-6750, 0000-0003-3783-7069},
  license      = {AGPL-3.0}
}
