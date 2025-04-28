import re

def preprocess(text):
    return re.sub(r'\W+', ' ', text.lower())
