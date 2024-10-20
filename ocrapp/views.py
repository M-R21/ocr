# ocrapp/views.py
import os
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from pdf2image import convert_from_bytes  # Use convert_from_bytes instead of path for in-memory files
import pytesseract
from .forms import PDFUploadForm

def pdf_to_csv_view(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']

            # Convert PDF file to bytes (works for both in-memory and disk-based files)
            pdf_bytes = pdf_file.read()

            # Convert PDF bytes to images (use convert_from_bytes instead of convert_from_path)
            images = convert_from_bytes(pdf_bytes)

            extracted_data = []

            # OCR on each page
            for img in images:
                text = pytesseract.image_to_string(img)
                # Process the extracted text to get table data
                rows = extract_table_data(text)
                extracted_data.extend(rows)

            # Create CSV from extracted data
            df = pd.DataFrame(extracted_data)

            # Return CSV as download
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="output.csv"'
            df.to_csv(path_or_buf=response, index=False)

            return response
    else:
        form = PDFUploadForm()

    return render(request, 'ocrapp/upload.html', {'form': form})

def extract_table_data(text):
    # Simple table extraction (modify this for your specific use case)
    rows = []
    lines = text.split("\n")
    for line in lines:
        columns = line.split()  # Assuming columns are separated by spaces
        if columns:  # Ignore empty lines
            rows.append(columns)
    return rows
