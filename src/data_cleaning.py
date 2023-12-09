import re


class DataCleaner:
    def __init__(self, raw_text):
        self.raw_text = raw_text

    def normalize_whitespace(self):
        cleaned_text = ' '.join(self.raw_text.split())
        return cleaned_text
    
    def remove_headers_footers(self):
        # Assuming headers and footers follow a pattern that can be identified by a regex
        self.raw_text = re.sub(r'Header or fotter pattern', '', self.raw_text)

    def remove_unwanted_characters(self):
        self.raw_text = re.sub(r'[^\x00-\x7F]+', '', self.raw_text)  # Removes non-ASCII characters

    def replace_newlines(self):
        self.raw_text = self.raw_text.replace('\n', ' ')

    def collapse_punctuation(self):
        self.raw_text = re.sub(r'[\.\,\'"!?;:-]{2,}', lambda x: x.group(0)[0], self.raw_text)

    def clean_text(self):
        self.normalize_whitespace()
        self.remove_headers_footers()
        self.remove_unwanted_characters()
        self.replace_newlines()
        self.collapse_punctuation()
        # Add other cleaning methods as needed
        return self.raw_text.strip()  # Final strip to clean up any leading/trailing whitespace
