from tools import extract_text_from_pdf, clean_resume_text
from graph import graph


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

initial_state = {
    "resume_text": clean_text,
    "job_description": job_description,

    "skills_analysis": {},
    "experience_analysis": {},
    "education_analysis": {},
    "job_match_analysis": {},
    "recommendations": {},
}


# --------------------------------------------------
# 4. Run entire LangGraph
# --------------------------------------------------

result = graph.invoke(initial_state)


# --------------------------------------------------
# 5. Display results
# --------------------------------------------------

print("\n" + "=" * 60)
print("FULL RESUME ANALYZER GRAPH")
print("=" * 60)


print("\nSKILLS ANALYSIS")
print("-" * 60)
print(result["skills_analysis"])


print("\nEXPERIENCE ANALYSIS")
print("-" * 60)
print(result["experience_analysis"])


print("\nEDUCATION ANALYSIS")
print("-" * 60)
print(result["education_analysis"])


print("\nJOB MATCH ANALYSIS")
print("-" * 60)
print(result["job_match_analysis"])


print("\nRECOMMENDATIONS")
print("-" * 60)
print(result["recommendations"])