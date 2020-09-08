#!/usr/bin/env python3

from PIL import Image
import os

curDir = "./supplier-data/images"

# go through each file
files = [f for f in os.listdir(curDir)]
for file in files:
  if file.endswith(".tiff"):
    print(file)
    im = Image.open(os.path.join(curDir+file))
    new_im = im.resize((600,400)).convert("RGB")
    new_im.save(curDir + "/" + file.replace(".tiff",".jpeg"))
