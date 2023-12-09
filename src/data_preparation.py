import re

class DataPreparer:
    def __init__(self, cleaned_text):
        self.cleaned_text = cleaned_text

    def find_isin(self):
        match = re.search(r'[A-Z]{2}[A-Z0-9]{10}', self.cleaned_text)
        return match.group(0) if match else None

    # Define other methods to extract CUSIP, dates, etc.

    def extract_data_points(self):
        return {
            'ISIN': self.find_isin(),
            # 'CUSIP': self.find_cusip(),
            # 'First Payment Date': self.find_first_payment_date(),
            # ...
        }
