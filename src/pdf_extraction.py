from PyPDF2 import PdfReader

class PDFExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = ""

    def read_pdf(self) -> str:
        """
        Reads the PDF and extracts the text.
        
        Returns:
            str: The extracted text.
        """
        with open(self.pdf_path, 'rb') as file:
            reader = PdfReader(file)
            for page in reader.pages:
                self.text += page.extract_text()
        return self.text
