from state import ResumeState
from model import llm

from schema import (
    SkillsAnalysis,
    ExperienceAnalysis,
    EducationAnalysis,
    JobMatchAnalysis,
    Recommendations,
)


def analyze_skills(state: ResumeState):
    resume = state["resume_text"]

    structured_llm = llm.with_structured_output(SkillsAnalysis)

    prompt = f"""
Analyze the skills in the following resume.

Only identify skills that are actually supported by the resume.
Do not invent skills.

Resume:
{resume}
"""

    result = structured_llm.invoke(prompt)

    return {
        "skills_analysis": result.model_dump()
    }


def analyze_experience(state: ResumeState):
    resume = state["resume_text"]

    structured_llm = llm.with_structured_output(ExperienceAnalysis)

    prompt = f"""
Analyze the professional experience in this resume.

Only make claims supported by the resume.

Resume:
{resume}
"""

    result = structured_llm.invoke(prompt)

    return {
        "experience_analysis": result.model_dump()
    }


def analyze_education(state: ResumeState):
    resume = state["resume_text"]

    structured_llm = llm.with_structured_output(EducationAnalysis)

    prompt = f"""
Analyze the educational background in this resume.

Only make claims supported by the resume.

Resume:
{resume}
"""

    result = structured_llm.invoke(prompt)

    return {
        "education_analysis": result.model_dump()
    }


def analyze_job_match(state: ResumeState):
    resume = state["resume_text"]
    job = state["job_description"]

    skills = state["skills_analysis"]
    experience = state["experience_analysis"]
    education = state["education_analysis"]

    structured_llm = llm.with_structured_output(JobMatchAnalysis)

    prompt = f"""
Compare the candidate's resume against the job description.

Use the supplied analyses as supporting information.

Do not give credit for skills or experience that are not actually
supported by the resume.

RESUME:
{resume}

SKILLS ANALYSIS:
{skills}

EXPERIENCE ANALYSIS:
{experience}

EDUCATION ANALYSIS:
{education}

JOB DESCRIPTION:
{job}
"""

    result = structured_llm.invoke(prompt)

    return {
        "job_match_analysis": result.model_dump()
    }


def generate_recommendations(state: ResumeState):
    skills = state.get("skills_analysis", {})
    experience = state.get("experience_analysis", {})
    education = state.get("education_analysis", {})
    job_match = state.get("job_match_analysis", {})

    structured_llm = llm.with_structured_output(Recommendations)

    prompt = f"""
Generate specific resume improvement recommendations based on
the following analysis.

Do not recommend claiming skills or experience that the candidate
does not actually possess.

SKILLS:
{skills}

EXPERIENCE:
{experience}

EDUCATION:
{education}

JOB MATCH:
{job_match}
"""

    result = structured_llm.invoke(prompt)

    return {
        "recommendations": result.model_dump()
    }