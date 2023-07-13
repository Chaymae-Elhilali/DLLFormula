import os
from PIL import Image

if len(sys.argv) != 2:
    print("Usage: python3 label.py <folderName>")
    sys.exit(1)

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


Math(table % '\\\\'.join(predictions))