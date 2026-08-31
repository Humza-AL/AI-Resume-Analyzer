from langgraph.graph import StateGraph, START, END

from state import ResumeState
from nodes import (
    analyze_skills,
    analyze_experience,
    analyze_education,
)

from tools import extract_text_from_pdf, clean_resume_text


# --------------------------------------------------
# 1. Extract resume
# --------------------------------------------------

text = extract_text_from_pdf("resume.pdf")
clean_text = clean_resume_text(text)


# --------------------------------------------------
# 2. Create initial State
# --------------------------------------------------

initial_state = {
    "resume_text": clean_text,
    "job_description": "",
    "skills_analysis": {},
    "experience_analysis": {},
    "education_analysis": {},
    "job_match_analysis": {},
    "recommendations": {},
}


# --------------------------------------------------
# 3. Build test graph
# --------------------------------------------------

builder = StateGraph(ResumeState)


builder.add_node("skills", analyze_skills)
builder.add_node("experience", analyze_experience)
builder.add_node("education", analyze_education)


# Start all three analyses
builder.add_edge(START, "skills")
builder.add_edge(START, "experience")
builder.add_edge(START, "education")


# End after each branch
builder.add_edge("skills", END)
builder.add_edge("experience", END)
builder.add_edge("education", END)


# Compile graph
graph = builder.compile()


# --------------------------------------------------
# 4. Run graph
# --------------------------------------------------

result = graph.invoke(initial_state)


# --------------------------------------------------
# 5. Display results
# --------------------------------------------------

print("\n" + "=" * 60)
print("PARALLEL GRAPH TEST")
print("=" * 60)

print("\nSKILLS:")
print(result["skills_analysis"])

print("\nEXPERIENCE:")
print(result["experience_analysis"])

print("\nEDUCATION:")
print(result["education_analysis"])