class DataCleaner:
    def __init__(self, raw_text):
        self.raw_text = raw_text

    def clean_text(self):
        cleaned_text = ' '.join(self.raw_text.split())
        # Add more cleaning steps as necessary
        return cleaned_text
