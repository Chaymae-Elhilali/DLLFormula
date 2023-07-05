import os
import sys

# Check if running on Colab or locally
if "google.colab" in sys.modules:
    # Running on Google Colab
    base_directory = "/content/DLLFormula"
else:
    # Running locally
    base_directory = "./DLLFormula"  # Adjust this path accordingly

# Create the DLLFormula directory if it doesn't exist
if not os.path.isdir(base_directory):
    os.makedirs(base_directory)

# Change the current working directory to the DLLFormula directory
os.chdir(base_directory)

# Now continue with the rest of the code to create "formula-detector-9" inside DLLFormula
#!pip install ultralytics==8.0.20

from IPython import display
display.clear_output()

import ultralytics
ultralytics.checks()

from ultralytics import YOLO
from IPython.display import display, Image

# Create the datasets directory inside DLLFormula
datasets_directory = os.path.join(base_directory, "datasets")
if not os.path.isdir(datasets_directory):
    os.makedirs(datasets_directory)

cd {datasets_directory}

#!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="YOUR_ROBOFLOW_API_KEY")  # Replace "YOUR_ROBOFLOW_API_KEY" with your actual API key
project = rf.workspace("um6p-ts7fh").project("formula-detector-egybi")
dataset = project.version(9).download("yolov8")
