#! /usr/bin/env python3
# Uploading the descriptions through REST

import os
import requests

supplierDir = "./supplier-data/descriptions"
supplierData = dict.fromkeys(["name","weight","description"])

# list all files
files = [f for f in os.listdir(feedbackDir)]

# traverse through each file
for f in files:
  if f.endswith(".txt"):
    # serialize information into dictionary
    with open(feedbackDir + "/" + f) as fp:
      supplierData["name"] = fp.readline()
      supplierData["weight"] = int(fp.readline()[:-4]
      supplierData["description"] = fp.readline()
      supplierData["image_name"] = f + ".jpeg"

      #POST to feedback
      r = requests.post('http://34.121.68.83/fruits/', data = supplierData)
      #if not okay, raise exception
      if not r.ok:
        raise Exception("POST failed with status code {}".format(r.status_code))
    fp.close()