import os
from PIL import Image
from pix2tex import cli as pix2tex
import pandas as pd
import sys


model = pix2tex.LatexOCR()

def upload_files():
    from google.colab import files
    from io import BytesIO
    uploaded = files.upload()
    return [(name, BytesIO(b)) for name, b in uploaded.items()]

folder_name = sys.argv[1]  

image_folder = os.path.join('/content/DLLFormula/datasets/runs/boxes', folder_name)

image_files = os.listdir(image_folder)
predictions = []

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    print(image_path)
    img = Image.open(image_path)
    latex_formula = model(img)
    print(latex_formula)
    predictions.append({'Filename': image_file, 'Formula': latex_formula})

# Create a pandas DataFrame
df = pd.DataFrame(predictions)

# Display the DataFrame (optional, for visualization)
print(df)

# Save the DataFrame to Excel
output_excel_file = "detected_formulas.xlsx"
df.to_excel(output_excel_file, index=False)

# Display the saved file path
print("Detected formulas saved to:", output_excel_file)
