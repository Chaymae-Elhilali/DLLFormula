import os
from PIL import Image
import sys
from pix2tex import cli as pix2tex
model = pix2tex.LatexOCR()
from IPython.display import display, HTML
import math


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

from IPython.display import HTML, Math
display(HTML("<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/"
             "latest.js?config=default'></script>"))
table = r'\begin{array} {l|l} %s  \end{array}'

folder_name = sys.argv[1]

image_folder = os.path.join('/content/DLLFormula/datasets/runs/boxes',folder_name)  # chemin vers dossier d'images

image_files = os.listdir(image_folder)
predictions = []

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    print(image_path)
    img = Image.open(image_path)
    math = model(img)
    print(math)
    predictions.append('\\mathrm{%s} & \\displaystyle{%s}' % (image_file, math))


table = r'\begin{array} {l|l} %s \end{array}'
latex_table_code = table % '\\\\'.join(predictions)

#if I want to display the formula written in latex
#doesn't work yet:
display(Math(latex_table_code))

# Save the LaTeX table code to a file
output_file = "output_formulas.tex"
with open(output_file, "w") as file:
    file.write(latex_table_code)

# Display the saved file path
print("Formulas saved to:", output_file)
