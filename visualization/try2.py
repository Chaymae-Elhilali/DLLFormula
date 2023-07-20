import os
from PIL import Image
from pix2tex import cli as pix2tex
import pandas as pd
import base64
from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage
import sys
from io import BytesIO


model = pix2tex.LatexOCR()

def upload_files():
    from google.colab import files
    from io import BytesIO
    uploaded = files.upload()
    return [(name, BytesIO(b)) for name, b in uploaded.items()]

folder_name = sys.argv[1]  

image_folder_boxes = os.path.join('/content/DLLFormula/datasets/runs/boxes', folder_name)
image_folder_eq = os.path.join('/content/DLLFormula/datasets/runs/boxes', folder_name)

image_files_boxes = os.listdir(image_folder_boxes)
image_files_eq = os.listdir(image_folder_eq)

predictions = []

for image_file in image_files_eq:
    image_path_boxes = os.path.join(image_folder_boxes, image_file)
    image_path_eq = os.path.join(image_folder_eq, image_file)

    print(image_path_boxes)
    print(image_path_eq)

    img = Image.open(image_path_boxes)
    latex_formula = model(img)
    print(latex_formula)

    # Convert the image to a Data URL (HTML representation)
    with open(image_path_eq, "rb") as f:
        data_uri = base64.b64encode(f.read()).decode("utf-8")

    # Append the Data URL representation and the detected formula to the list
    predictions.append({'Image': data_uri, 'Formula': latex_formula})

# Create a pandas DataFrame
df = pd.DataFrame(predictions)

# Create a new Excel workbook and sheet
output_excel_file = "detected_formulas.xlsx"
workbook = Workbook()
sheet = workbook.active

# Write the data to the Excel sheet
for idx, row in df.iterrows():
    img_data = base64.b64decode(row['Image'])
    img = Image.open(BytesIO(img_data))
    img_cell = XLImage(img)
    sheet.column_dimensions['A'].width = 20
    sheet.column_dimensions['B'].width = 100
    sheet.row_dimensions[idx + 2].height = 100
    sheet.add_image(img_cell, f'A{idx+2}')
    sheet.cell(row=idx + 2, column=2).value = row['Formula']

# Save the Excel workbook
workbook.save(output_excel_file)

# Display the saved file path
print("Detected formulas saved to:", output_excel_file)
