#!/usr/bin/env python3
# Script to generate a PDF report
# credit: Sudhansu Dwivedi for forum contribution. Part of the code were adapted from his answers

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.units import inch

def generate_report(attachment, add_info, title):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles['h1'])
    report_info = Paragraph(add_info, styles['BodyText'])
    space = Spacer(1,0.2*inch)

    report.build([report_title, space, report_info, space])
