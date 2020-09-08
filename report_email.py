#!/usr/bin/env python3
# process supplier fruit description data from supplier-data/descriptions directory
# credit: Sudhansu Dwivedi for forum contribution. Part of the code were adapted from his answers

import os

from datetime import date
from reports import generate_report
from emails import generate_email, send_email

supplierDir = "./supplier-data/descriptions"
supplierData = dict.fromkeys(["name","weight","description"])

def report_body():
    """Generating a summary with two lists, which gives the output name and weight"""
    names = []
    weights = []
    for item in os.listdir(supplierDir):
      filename=os.path.join(supplierDir,item)
      with open(filename) as f:
        name = fp.readline()
        weight = fp.readline()
        
        names.append('name: ' +name)
        weights.append('weight: ' +weight)
        
        print(names)
        print(weights)
        
    new_obj = ""  # initializing the object
    # Calling values from two lists one by one.
    for i in range(len(names)):
      new_obj += names[i] + '<br />' + weights[i] + '<br />' + '<br />'
    return new_obj
    

if __name__ == "__main__":
    user = os.getenv('USER')
    current_date = date.today().strftime("%B %d, %Y")  # Format: "Sept 5, 2020"
    title = 'Processed Update on ' + str(current_date)  
    generate_report('/tmp/processed.pdf', title, report_body())  
    
    email_subject = 'Upload Completed - Online Fruit Store'  
    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'  
   
    message = generate_email("automation@example.com", "{}@example.com".format(user),email_subject, email_body, "/tmp/processed.pdf")
    unsuccessful = send_email(message)
    
    print(unsuccessful)