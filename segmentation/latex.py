from PIL import Image
import sys
from pix2tex import cli as pix2tex
model = pix2tex.LatexOCR()
from IPython.display import display, HTML
from sympy import latex, preview, sympify

import math
import os, requests



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

from IPython.display import HTML, Math
display(HTML("<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/"
             "latest.js?config=default'></script>"))
table = r'\begin{array} {l|l} %s  \end{array}'

#def formula_as_file(formula, file):
 #   with open(file, "w") as f:
  #      f.write(formula)

folder_name = sys.argv[1]

image_folder = os.path.join('/content/DLLFormula/datasets/runs/boxes',folder_name)  # chemin vers dossier d'images

image_files = os.listdir(image_folder)
predictions = []

def preprocess_latex(latex_code):
    # Replace Unicode characters with LaTeX representations
    latex_code = latex_code.replace('→', r'\longrightarrow')
    return latex_code

def latex_to_file(formula, file):
    display(Math(formula))
    with open(file, "w") as f:
        f.write(str(formula))
        
        
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    print(image_path)
    img = Image.open(image_path)
    latex_code = model(img)
    print(latex_code)
    latex_code = preprocess_latex(latex_code)
    
    predictions.append('\\mathrm{%s} & \\displaystyle{%s}' % (image_file, latex_code))
    latex_to_file(latex_code, image_file + ".txt")
    
    
    #predictions.append('\\mathrm{%s} & \\displaystyle{%s}' % (image_file, latex_code))
    l#atex_to_file(latex_code, image_file + ".txt")
    


table = r'\begin{array} {l|l} %s \end{array}'
latex_table_code = table % '\\\\'.join(predictions)

#if I want to display the formula written in latex
#doesn't work yet:
display(Math(latex_table_code))
output_file = "output_formulas.tex"
#with open(output_file, "w") as file:
   # file.write(latex_table_code)

# Display the saved file path
#print("Plain text formulas saved to:", output_file)