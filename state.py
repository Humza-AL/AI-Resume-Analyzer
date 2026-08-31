from typing import TypedDict


class ResumeState(TypedDict):
    resume_text: str
    job_description: str

    skills_analysis: dict
    experience_analysis: dict
    education_analysis: dict
    job_match_analysis: dict
    recommendations: dict

