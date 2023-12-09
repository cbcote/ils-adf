from utils.file_utils import get_pdf_paths

from data_preparation import DataPreparer
from data_cleaning import DataCleaner
from pdf_extraction import PDFExtractor


def main(pdf_path):
    pdf_extractor = PDFExtractor(pdf_path)
    pdf_extractor.read_pdf()
    raw_text = pdf_extractor.extract_all_text()

    # data_cleaner = DataCleaner(raw_text)
    # cleaned_text = data_cleaner.clean_text()

    # data_preparer = DataPreparer(cleaned_text)
    # extracted_data = data_preparer.extract_data_points()

    return raw_text

if __name__ == "__main__":
    data_dir = 'data'
    pdf_paths = get_pdf_paths(data_dir)
    data = main(pdf_paths[0])
    print(data)
