from tools import extract_text_from_pdf, clean_resume_text
from nodes import analyze_experience


# Extract resume text
text = extract_text_from_pdf("resume.pdf")
clean_text = clean_resume_text(text)


# Create the State needed by analyze_experience
state = {
    "resume_text": clean_text,
    "job_description": "",
    "skills_analysis": {},
    "experience_analysis": {},
    "education_analysis": {},
    "job_match_analysis": {},
    "recommendations": {},
}


# Run experience analysis
result = analyze_experience(state)


# Display result
print("\nEXPERIENCE ANALYSIS")
print("=" * 50)

print(result)