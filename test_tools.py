from tools import extract_text_from_pdf, clean_resume_text
text=extract_text_from_pdf("resume.pdf")
clean_text=clean_resume_text(text)

print(clean_text)