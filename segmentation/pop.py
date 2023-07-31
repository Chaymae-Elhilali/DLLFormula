import os, requests
def formula_as_file(formula, file, negate=False):
    '''render the latex formula ( for visual validation) '''
    ##https://jamesgregson.blogspot.com/2013/06/latex-formulas-as-images-using-python.html
    tfile = file
    if negate:
        tfile = 'tmp.png'
    r = requests.get('http://latex.codecogs.com/png.latex?\dpi{300} \Large	 %s' % formula)
    f = open(tfile, 'wb')
    f.write(r.content)
    f.close()
    if negate:
        os.system('convert tmp.png -channel RGB -negate -colorspace rgb %s' % file)


try:
        #formula_as_file(r'\Gamma_{Levin}(x) = \| \nabla p(x) \|_2^{0.8} + \sum_i |\frac{\partial^2 p(x)}{\partial x_i^2}|^{0.8}','test1.png')
        formula_as_file(r'x^{\prime}=\sin(t x),\;x_{*}^{\prime}=t^{2}+x^{2}', 'test2.png', negate=True)
        print('formula saved as file')
except:
        print("can't save as file")
        
import os
import sys
from PIL import Image
from pix2tex import cli as pix2tex
from sympy import latex
from IPython.display import display, HTML, Math

# Your model initialization and other code here...

# Your folder_name and other code here...

predictions = []

# Function to preprocess LaTeX formula before saving it
def preprocess_latex(latex_code):
    # Replace Unicode characters with LaTeX representations
    latex_code = latex_code.replace('→', r'\longrightarrow')
    return latex_code

# Function to render LaTeX formula and save it as plain text
def latex_to_file(formula, file):
    display(Math(formula))
    with open(file, "w") as f:
        f.write(formula)

# Render LaTeX formulas and store them as plain text
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    print(image_path)
    img = Image.open(image_path)
    latex_code = model(img)
    print(latex_code)
    
    # Preprocess the LaTeX formula before saving it
    latex_code = preprocess_latex(latex_code)
    
    predictions.append('\\mathrm{%s} & \\displaystyle{%s}' % (image_file, latex_code))
    
    # Convert the LaTeX formula to plain text and save it
    latex_to_file(latex_code, image_file + ".txt")

# Generate LaTeX table code
table = r'\begin{array} {l|l} %s \end{array}'
latex_table_code = table % '\\\\'.join(predictions)

# Display the LaTeX table code as LaTeX
display(Math(latex_table_code))

# Save the LaTeX table code to a file
output_file = "output_formulas.tex"

