import pdfplumber

def  resume_text(file):
    with pdfplumber.open(file)as pdf:
        text=''
        for page in pdf.pages:
            page_text=page.extract_text()
            if page_text:
                text+=page_text

    
    return text


