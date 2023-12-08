from PyPDF2 import PdfFileReader

class PDFExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.reader = None
        self.text = ""

    def read_pdf(self):
        with open(self.pdf_path, 'rb') as file:
            self.reader = PdfFileReader(file)

    def extract_all_text(self):
        if self.reader is not None:
            for page_num in range(self.reader.numPages):
                self.text += self.reader.getPage(page_num).extractText()
        return self.text
