from pypdf import PdfReader

def extract_text_from_pdf(file_path: str)->str:
    """Extract text from a pdf file"""
    reader=PdfReader(file_path)

    text=""

    for page in reader.pages:
        page_text=page.extract_text()

        if page_text:
            text+=page_text + "\n"
    return text


def clean_resume_text(text: str)->str:
    """ Clean extracted resume text"""

    lines=[]

    for line in text.splitlines():
        line= line.strip()

        if line:
            lines.append(line)
    return "\n".join(lines)


