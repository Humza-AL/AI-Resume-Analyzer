from tools import extract_text_from_pdf, clean_resume_text

from nodes import (
    analyze_skills,
    analyze_experience,
    analyze_education,
    analyze_job_match,
    generate_recommendations,
)


# --------------------------------------------------
# 1. Extract resume
# --------------------------------------------------

text = extract_text_from_pdf("resume.pdf")
clean_text = clean_resume_text(text)


# --------------------------------------------------
# 2. Job description
# --------------------------------------------------

job_description = """
Machine Learning Engineer

We are looking for a Machine Learning Engineer to build,
deploy, and maintain machine learning applications.

Requirements:

- Strong Python programming skills
- Experience with machine learning
- Experience with scikit-learn, PyTorch, or TensorFlow
- Experience working with large datasets
- SQL experience
- Experience building APIs
- Experience with Docker
- Experience with cloud platforms such as AWS
- Understanding of LLMs and generative AI
- Strong problem-solving and communication skills

Responsibilities:

- Develop and evaluate machine learning models
- Build data preprocessing pipelines
- Deploy machine learning models
- Develop AI-powered applications
- Collaborate with engineering and data teams
"""


# --------------------------------------------------
# 3. Initial State
# --------------------------------------------------

state = {
    "resume_text": clean_text,
    "job_description": job_description,
    "skills_analysis": {},
    "experience_analysis": {},
    "education_analysis": {},
    "job_match_analysis": {},
    "recommendations": {},
}


# --------------------------------------------------
# 4. Run analyses
# --------------------------------------------------

state.update(analyze_skills(state))

state.update(analyze_experience(state))

state.update(analyze_education(state))


# --------------------------------------------------
# 5. Job match
# --------------------------------------------------

state.update(analyze_job_match(state))


# --------------------------------------------------
# 6. Recommendations
# --------------------------------------------------

result = generate_recommendations(state)


# --------------------------------------------------
# 7. Display result
# --------------------------------------------------

print("\n" + "=" * 60)
print("RECOMMENDATIONS")
print("=" * 60)

print(result)