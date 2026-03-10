import fitz
import sys

def read_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        print(text[:4000]) # Extracting just the first 4000 characters to get the abstract/intro
    except Exception as e:
        print(f"Error reading PDF: {e}")

if __name__ == "__main__":
    read_pdf(sys.argv[1])
