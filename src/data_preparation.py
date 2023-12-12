import re

class DataPreparer:
    def __init__(self, cleaned_text):
        self.cleaned_text = cleaned_text

    def find_issuer(self):
        # Updated regex to account for the series of dots and capture the name following them
        pattern = r'Issuer:\s*(\.{2,})\s*([\w\s\d]+)'
        match = re.search(pattern, self.cleaned_text)
        if match:
            # Group 2 should contain the issuer's name
            return match.group(2).strip()
        return None

    def find_isin(self):
        match = re.search(r'[A-Z]{2}[A-Z0-9]{10}', self.cleaned_text)
        return match.group(0) if match else None

    def find_dates(self, label):
        pattern = r'{}:\s*(\bJanuary|\bFebruary|\bMarch|\bApril|\bMay|\bJune|\bJuly|\bAugust|\bSeptember|\bOctober|\bNovember|\bDecember)\s\d{{1,2}},\s\d{{4}}'.format(label)
        matches = re.findall(pattern, self.cleaned_text)
        return matches
    
    def find_first_payment_date(self):
        # Adjusted regular expression to match the format "Month Day, Year"
        pattern = r'First Payment Date:\s*(\bJanuary|\bFebruary|\bMarch|\bApril|\bMay|\bJune|\bJuly|\bAugust|\bSeptember|\bOctober|\bNovember|\bDecember)\s\d{1,2},\s\d{4}'
        match = re.search(pattern, self.cleaned_text)
        return match.group(0) if match else None

    def find_reduced_interest_spread(self):
        match = re.search(r'Reduced Interest Spread:.*?([\d.]+%)', self.cleaned_text)
        return match.group(1) if match else None
    
    def find_off_risk_period_spread(self):
        match = re.search(r'Off-Risk Period Spread:\s*[\.\s]*([\d.]+%)', self.cleaned_text)
        return match.group(1) if match else None
    
    def find_initial_trigger_amount_refined(self):
        pattern = r'Initial Trigger Amount:\s*\.{2,}\s*(\$\s*[^\n]+)'
        match = re.search(pattern, self.cleaned_text)
        return match.group(1).strip() if match else None


    def extract_data_points(self):
        return {
            'Issuer': self.find_issuer(),
            'ISIN': self.find_isin(),
            'Scheduled Redemption Date': self.find_dates("Scheduled Redemption Date"),
            'Final Redemption Date': self.find_dates("Final Redemption Date"),
            'First Payment Date': self.find_first_payment_date(),
            'Reduced Interest Spread': self.find_reduced_interest_spread(),
            'Off-Risk Period Spread': self.find_off_risk_period_spread(),
            'Initial Trigger Amount': self.find_initial_trigger_amount_refined(),
        }
