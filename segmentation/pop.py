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

# Render LaTeX formulas and save them as images
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    print(image_path)
    img = Image.open(image_path)
    math = model(img)
    print(math)
    formula_as_file(math, image_file + ".png")

# Display the images with LaTeX formulas
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file + ".png")
    img = Image.open(image_path)
    display(img)