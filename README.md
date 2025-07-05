# 📄 LogVision - Phase 1

**LogVision** is a simple OCR-powered tool that converts scanned or printed log images into Excel spreadsheets, making it easier to search and analyze data from printed logs.

This is **Phase 1** of the project, focusing on:
- Extracting data from printed/scanned log images.
- Automatically detecting table rows and columns.
- Saving extracted data into an Excel file (`log_output.xlsx`).



## ✅ Features
- Converts scanned/printed log images into Excel spreadsheets.
- Supports images containing printed/typed text.
- Auto-detects rows and columns from table-like data.
- Saves extracted data into an Excel file for easy analysis.
- Preprocessing included to improve OCR accuracy.



## ✅ How It Works
1. Load a scanned/printed log image.
2. Preprocess the image (grayscale + sharpening) for better OCR results.
3. Extract text using Tesseract OCR.
4. Automatically split text into rows and columns using smart logic.
5. Save the structured data into an Excel spreadsheet.
