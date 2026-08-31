from pydantic import BaseModel, Field


class SkillsAnalysis(BaseModel):
    technical_skills: list[str] = Field(
        description="Technical skills found in the resume."
    )

    soft_skills: list[str] = Field(
        description="Soft skills demonstrated in the resume."
    )

    tools_and_technologies: list[str] = Field(
        description="Tools, frameworks, libraries, and technologies found in the resume."
    )

    strengths: list[str] = Field(
        description="The strongest aspects of the candidate's skills."
    )

    skill_gaps: list[str] = Field(
        description="Skills that appear to be missing or weak based on the resume."
    )


class ExperienceAnalysis(BaseModel):
    roles: list[str] = Field(
        description="Previous professional roles found in the resume."
    )

    relevant_experience: list[str] = Field(
        description="Experience particularly relevant to the candidate's career or target role."
    )

    achievements: list[str] = Field(
        description="Notable accomplishments or measurable achievements."
    )

    strengths: list[str] = Field(
        description="Strengths demonstrated through the candidate's experience."
    )

    weaknesses: list[str] = Field(
        description="Weaknesses or areas where the experience section could be improved."
    )

    seniority_assessment: str = Field(
        description="Assessment of the candidate's apparent professional seniority."
    )


class EducationAnalysis(BaseModel):
    degrees: list[str] = Field(
        description="Degrees found in the resume."
    )

    fields_of_study: list[str] = Field(
        description="Fields or majors associated with the candidate's education."
    )

    certifications: list[str] = Field(
        description="Certifications or professional credentials found in the resume."
    )

    relevant_coursework: list[str] = Field(
        description="Coursework that appears relevant to the candidate's career."
    )

    strengths: list[str] = Field(
        description="Strengths of the candidate's educational background."
    )

    gaps: list[str] = Field(
        description="Potential weaknesses or gaps in the educational background."
    )


class JobMatchAnalysis(BaseModel):
    match_score: int = Field(
        description="Overall resume-to-job match score from 0 to 100.",
        ge=0,
        le=100
    )

    matching_skills: list[str] = Field(
        description="Skills required by the job that the candidate appears to possess."
    )

    missing_skills: list[str] = Field(
        description="Important job requirements missing or not demonstrated in the resume."
    )

    relevant_experience: list[str] = Field(
        description="Resume experience that directly matches the job requirements."
    )

    experience_gaps: list[str] = Field(
        description="Important experience requirements that the resume does not demonstrate."
    )

    education_match: str = Field(
        description="Assessment of how well the candidate's education matches the job requirements."
    )

    strengths_for_role: list[str] = Field(
        description="The candidate's strongest advantages for this particular job."
    )

    weaknesses_for_role: list[str] = Field(
        description="The candidate's biggest weaknesses or risks for this particular job."
    )


class Recommendations(BaseModel):
    skills_to_emphasize: list[str] = Field(
        description="Skills already possessed by the candidate that should be emphasized."
    )

    experience_improvements: list[str] = Field(
        description="Specific ways to improve the experience section."
    )

    resume_improvements: list[str] = Field(
        description="Specific improvements to the resume overall."
    )

    keywords_to_consider: list[str] = Field(
        description="Relevant job keywords that could be incorporated when truthful."
    )

    priority_actions: list[str] = Field(
        description="The most important actions the candidate should take."
    )