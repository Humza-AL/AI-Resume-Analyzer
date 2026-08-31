from langgraph.graph import StateGraph, START, END

from state import ResumeState

from nodes import (
    analyze_skills,
    analyze_experience,
    analyze_education,
    analyze_job_match,
    generate_recommendations,
)


# Create graph
builder = StateGraph(ResumeState)


# --------------------------------------------------
# Add nodes
# --------------------------------------------------

builder.add_node("skills", analyze_skills)
builder.add_node("experience", analyze_experience)
builder.add_node("education", analyze_education)
builder.add_node("job_match", analyze_job_match)
builder.add_node("recommendations", generate_recommendations)

# --------------------------------------------------
# Parallel analysis
# --------------------------------------------------

builder.add_edge(START, "skills")
builder.add_edge(START, "experience")
builder.add_edge(START, "education")


# --------------------------------------------------
# Job match waits for all three analyses
# --------------------------------------------------

builder.add_edge("skills", "job_match")
builder.add_edge("experience", "job_match")
builder.add_edge("education", "job_match")
builder.add_edge("job_match", "recommendations")


# --------------------------------------------------
# End
# --------------------------------------------------

builder.add_edge("recommendations", END)


# Compile graph
graph = builder.compile()