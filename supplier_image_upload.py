#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
curDir = "./supplier-data/images"

# go through each file
files = [f for f in os.listdir(curDir)]
for file in files:
  if file.endswith(".jpeg"):
    with open(file, 'rb') as opened:
      r = requests.post(url, files={'file': opened})