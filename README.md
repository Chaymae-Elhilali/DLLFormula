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

# CONVERSION

# ACKNOLEDGMENT:
code modified from:

- video to frames

- ocr latex converter

- pre-pretreatment