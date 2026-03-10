import PyPDF2
import sys

def extract_pdf(file_path):
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            print(text[:4000]) # output first 4000 characters to get the abstract and intro
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    extract_pdf(sys.argv[1])
