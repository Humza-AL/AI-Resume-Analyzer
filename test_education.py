from tools import extract_text_from_pdf, clean_resume_text
from nodes import analyze_education


# Extract resume text
text = extract_text_from_pdf("resume.pdf")
clean_text = clean_resume_text(text)


# Create the State needed by analyze_education
state = {
    "resume_text": clean_text,
    "job_description": "",
    "skills_analysis": {},
    "experience_analysis": {},
    "education_analysis": {},
    "job_match_analysis": {},
    "recommendations": {},
}


# Run education analysis
result = analyze_education(state)


# Display result
print("\nEDUCATION ANALYSIS")
print("=" * 50)

print(result)