import re

def extract_emails(text):
    """
    Extracts all email addresses from the given string using regular expressions.
    
    Args:
        text (str): The input string.
    
    Returns:
        list: A list of extracted email addresses.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

# Test the function
test_input = 'Contact us at support@example.com and sales@example.org.'
extracted_emails = extract_emails(test_input)
print(extracted_emails)
