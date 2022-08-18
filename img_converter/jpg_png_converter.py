import sys
import os
from PIL import Image

# grab the first and second argument.

image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new folder exists. if not, create it.
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
for file in os.listdir(image_folder):
    img = Image.open(os.path.join(image_folder, file))
    clean_name = os.path.splitext(file)[0]
    img.save(f'{output_folder}{file}.png', 'png')
    print(clean_name) 
    print('All ok!')