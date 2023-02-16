import shutil
import sys
import os
from PIL import Image, ImageOps

extension = sys.argv[1]
original_dir = sys.argv[2]
new_dir = sys.argv[3]

try:
    os.mkdir(new_dir)
    for file in os.listdir(original_dir):
        if file.endswith(extension):
            image = Image.open(os.path.join(original_dir, file)).convert('RGB')
            inverted_image = ImageOps.invert(image)
            inverted_image.save(os.path.join(new_dir, file))
        else:
            shutil.copy(os.path.join(original_dir, file), os.path.join(new_dir, file))

except Exception as e:
    print(e)