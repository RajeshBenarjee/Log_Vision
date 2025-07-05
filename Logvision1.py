import pytesseract
from PIL import Image, ImageFilter
import pandas as pd
import re
import os


# using of tesseract need's this to be interpreted
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


image_path = 'sample2.jpg'


img = Image.open(image_path).convert('L') 
# gray scale conversion for better text extraction


img = img.filter(ImageFilter.SHARPEN)  


custom_config = r'--oem 3 --psm 6'
# custom configuration for the OCR Model espically for the 'log Files' need to be converted into excel sheets 
# "--oem 3 " --> means that auto selection of ocr models 
# "--psm 6 " --> page segmentation mode 


text = pytesseract.image_to_string(img, config=custom_config)
# extraction of all the text

lines = text.split('\n')
rows = [line.strip() for line in lines if line.strip()] 


structured_rows = []
for row in rows:
    columns = re.split(r'\s{2,}', row)
    if len(columns) <= 1:
        columns = row.split()
    structured_rows.append(columns)


max_cols = max(len(r) for r in structured_rows)
for row in structured_rows:
    while len(row) < max_cols:
        row.append('')  

df = pd.DataFrame(structured_rows)

os.makedirs('output', exist_ok=True)  
output_filename = f"{os.path.splitext(os.path.basename(image_path))[0]}.xlsx"
output_path = os.path.join('output', output_filename)
df.to_excel(output_path, index=False, header=False)

print(f"\nExtraction Complete! Excel saved at: {output_path}")
