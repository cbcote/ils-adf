from src.utils.file_utils import get_pdf_paths
from src.data.pdf_extraction import PDFExtractor

data_dir = 'data'
pdf_paths = get_pdf_paths(data_dir)
extracted_text = PDFExtractor(pdf_paths[0]).extract_text()

print(extracted_text)