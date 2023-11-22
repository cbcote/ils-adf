import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

class PDFExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self):
        with open(self.pdf_path, "rb") as fd:
            viewer = SimplePDFViewer(fd)
            text = ''
            for canvas in viewer:
                viewer.render()
                text += ' '.join(viewer.canvas.strings)
        return text