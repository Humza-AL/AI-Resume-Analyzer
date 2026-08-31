
import streamlit as st

from tools import extract_text_from_pdf, clean_resume_text
from graph import graph


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide",
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📄 Resume Analyzer")

st.write(
    "Upload your resume and compare it against a job description "
    "using a LangGraph-powered AI analysis."
)


# --------------------------------------------------
# Resume upload
# --------------------------------------------------

uploaded_resume = st.file_uploader(
    "Upload your resume",
    type=["pdf"],
)


# --------------------------------------------------
# Job description
# --------------------------------------------------

job_description = st.text_area(
    "Paste the job description",
    height=250,
    placeholder="Paste the full job description here...",
)


# --------------------------------------------------
# Analyze button
# --------------------------------------------------

analyze_button = st.button(
    "🔍 Analyze Resume",
    type="primary",
)


# --------------------------------------------------
# Run analysis
# --------------------------------------------------

if analyze_button:

    if uploaded_resume is None:
        st.error("Please upload a resume PDF.")

    elif not job_description.strip():
        st.error("Please paste a job description.")

    else:

        try:

            # ------------------------------------------
            # Save uploaded PDF temporarily
            # ------------------------------------------

            with open("uploaded_resume.pdf", "wb") as f:
                f.write(uploaded_resume.getbuffer())


            # ------------------------------------------
            # Extract resume text
            # ------------------------------------------

            with st.spinner("Extracting resume text..."):

                resume_text = extract_text_from_pdf(
                    "uploaded_resume.pdf"
                )

                clean_text = clean_resume_text(resume_text)


            # ------------------------------------------
            # Create initial LangGraph state
            # ------------------------------------------

            initial_state = {
                "resume_text": clean_text,
                "job_description": job_description,

                "skills_analysis": {},
                "experience_analysis": {},
                "education_analysis": {},
                "job_match_analysis": {},
                "recommendations": {},
            }


            # ------------------------------------------
            # Run LangGraph
            # ------------------------------------------

            with st.spinner("Analyzing your resume..."):

                result = graph.invoke(initial_state)


            # ------------------------------------------
            # Analysis complete
            # ------------------------------------------

            st.success("Resume analysis complete!")


            # ==========================================
            # Skills Analysis
            # ==========================================

            st.header("🧠 Skills Analysis")

            skills = result["skills_analysis"]

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("Technical Skills")

                st.write(
                    skills.get("technical_skills", [])
                )

                st.subheader("Soft Skills")

                st.write(
                    skills.get("soft_skills", [])
                )

            with col2:

                st.subheader("Tools & Technologies")

                st.write(
                    skills.get("tools_and_technologies", [])
                )

                st.subheader("Skill Gaps")

                st.write(
                    skills.get("skill_gaps", [])
                )


            # ==========================================
            # Experience Analysis
            # ==========================================

            st.header("💼 Experience Analysis")

            experience = result["experience_analysis"]

            st.subheader("Roles")

            st.write(
                experience.get("roles", [])
            )

            st.subheader("Relevant Experience")

            st.write(
                experience.get("relevant_experience", [])
            )

            st.subheader("Achievements")

            st.write(
                experience.get("achievements", [])
            )

            st.subheader("Strengths")

            st.write(
                experience.get("strengths", [])
            )

            st.subheader("Weaknesses")

            st.write(
                experience.get("weaknesses", [])
            )

            st.subheader("Seniority Assessment")

            st.write(
                experience.get("seniority_assessment", "")
            )


            # ==========================================
            # Education Analysis
            # ==========================================

            st.header("🎓 Education Analysis")

            education = result["education_analysis"]

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("Degrees")

                st.write(
                    education.get("degrees", [])
                )

                st.subheader("Fields of Study")

                st.write(
                    education.get("fields_of_study", [])
                )

                st.subheader("Certifications")

                st.write(
                    education.get("certifications", [])
                )

            with col2:

                st.subheader("Relevant Coursework")

                st.write(
                    education.get("relevant_coursework", [])
                )

                st.subheader("Strengths")

                st.write(
                    education.get("strengths", [])
                )

                st.subheader("Gaps")

                st.write(
                    education.get("gaps", [])
                )


            # ==========================================
            # Job Match Analysis
            # ==========================================

            st.header("🎯 Job Match Analysis")

            job_match = result["job_match_analysis"]

            score = job_match.get("match_score", 0)

            st.metric(
                label="Match Score",
                value=f"{score}/100",
            )

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("Matching Skills")

                st.write(
                    job_match.get("matching_skills", [])
                )

            with col2:

                st.subheader("Missing Skills")

                st.write(
                    job_match.get("missing_skills", [])
                )

            st.subheader("Relevant Experience")

            st.write(
                job_match.get("relevant_experience", [])
            )

            st.subheader("Experience Gaps")

            st.write(
                job_match.get("experience_gaps", [])
            )

            st.subheader("Education Match")

            st.write(
                job_match.get("education_match", "")
            )

            st.subheader("Strengths for Role")

            st.write(
                job_match.get("strengths_for_role", [])
            )

            st.subheader("Weaknesses for Role")

            st.write(
                job_match.get("weaknesses_for_role", [])
            )


            # ==========================================
            # Recommendations
            # ==========================================

            st.header("📝 Recommendations")

            recommendations = result["recommendations"]

            st.subheader("Skills to Emphasize")

            st.write(
                recommendations.get(
                    "skills_to_emphasize",
                    []
                )
            )

            st.subheader("Experience Improvements")

            st.write(
                recommendations.get(
                    "experience_improvements",
                    []
                )
            )

            st.subheader("Resume Improvements")

            st.write(
                recommendations.get(
                    "resume_improvements",
                    []
                )
            )

            st.subheader("Keywords to Consider")

            st.write(
                recommendations.get(
                    "keywords_to_consider",
                    []
                )
            )

            st.subheader("Priority Actions")

            st.write(
                recommendations.get(
                    "priority_actions",
                    []
                )
            )


        except Exception as e:

            st.error(
                f"An error occurred while analyzing the resume: {e}"
            )
    
