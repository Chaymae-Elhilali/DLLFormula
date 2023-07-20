import os
from PIL import Image
import sys
from pix2tex import cli as pix2tex
from IPython.display import display, HTML, Math

if len(sys.argv) != 2:
    print("Usage: python3 label.py <folderName>")
    sys.exit(1)

def upload_files():
    from google.colab import files
    from io import BytesIO
    uploaded = files.upload()
    return [(name, BytesIO(b)) for name, b in uploaded.items()]

from pix2tex import cli as pix2tex
from PIL import Image
model = pix2tex.LatexOCR()

def latex_to_image(latex_code):
    display(Math(latex_code))

folder_name = sys.argv[1]
image_folder = os.path.join('/content/DLLFormula/datasets/runs/boxes', folder_name)

image_files = os.listdir(image_folder)
predictions = []

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    print(image_path)
    img = Image.open(image_path)
    math = model(img)
    print(math)
    latex_to_image(math)  # Display the LaTeX formula
    predictions.append('\\mathrm{%s} & \\displaystyle{%s}' % (image_file, math))

table = r'\begin{array} {l|l} %s \end{array}'
latex_table_code = table % '\\\\'.join(predictions)

# Save the LaTeX table code to a file
output_file = "output_formulas.tex"
with open(output_file, "w") as file:
    file.write(latex_table_code)

# Display the saved file path
print("Formulas saved to:", output_file)
