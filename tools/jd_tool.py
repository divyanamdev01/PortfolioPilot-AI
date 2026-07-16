import pdfplumber

def x_y_z(job_description=None, pdf_file=None):

    if pdf_file:

        text = ""

        with pdfplumber.open(pdf_file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text.strip()

    return job_description

