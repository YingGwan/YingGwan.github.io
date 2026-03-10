---
description: 如何使用指定的 FastIKD Conda 环境读取和解析 PDF 文件
---

When the user requests to read, parse, or extract text from a PDF file, you MUST follow these specific instructions:

1. **Python Interpreter Path:** You must execute any PDF processing scripts using the user's specific Conda environment Python executable.
   - Exact Python Path: `D:\conda\envs\FastIKD\python.exe`
   - **DO NOT** use default `python` or `python3` commands in the terminal.

2. **Script Creation:** Create a temporary python script (e.g., in `/tmp/extract_cmd_pdf.py`) to handle the PDF reading.
   - Recommended library: `pymupdf` (imported as `fitz`).
   - Example script structure:
     ```python
     import fitz
     import sys

     def read_pdf(file_path):
         try:
             doc = fitz.open(file_path)
             text = ""
             for page in doc:
                 text += page.get_text()
             print(text)
         except Exception as e:
             print(f"Error reading PDF: {e}")

     if __name__ == "__main__":
         read_pdf(sys.argv[1])
     ```

3. **Execution:** Run the script using the explicit environment path:
   `D:\conda\envs\FastIKD\python.exe /tmp/extract_cmd_pdf.py "<path_to_pdf_file>"`

4. **Dependency Handling:** If the script fails because `pymupdf` (or another required library) is not installed, install it strictly within the given environment first:
   // turbo
   `D:\conda\envs\FastIKD\python.exe -m pip install pymupdf`
