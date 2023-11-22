import os
import glob

def get_pdf_paths(data_dir):
    search_pattern = os.path.join(data_dir, '**', '*.pdf')
    pdf_paths = glob.glob(search_pattern, recursive=True)
    return pdf_paths