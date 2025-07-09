import os
from pathlib import Path
import pytesseract
from pdf2image import convert_from_path
from tqdm import tqdm
import re

def extract_text_from_pdf(pdf_path):
    pages = convert_from_path(pdf_path, dpi=300)
    text_all = ""
    
    for i, page in tqdm(enumerate(pages), desc="Processing pages"):
        text = pytesseract.image_to_string(page, lang='vie')
        text_all += f"\n--- Page {i+1} ---\n{text}"
    
    return text_all

if __name__ == "__main__":
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    PDF_PATH = Path(os.path.join(PROJECT_ROOT, 'data', 'pdf', 'sachgiaokhoalichsu11.pdf'))
    text_all = extract_text_from_pdf(PDF_PATH.as_posix())
    Path('raw_text_ocr.txt').write_text(text_all, encoding='utf-8')

