import streamlit as st

from tools import extract_text_from_pdf, clean_resume_text
from graph import graph


# --------------------------------------------------
# Helper functions
# --------------------------------------------------

def render_bullets(items):
    """Display a list as clean bullet points."""
    
    if not items:
        st.write("None identified.")
        return

    for item in items:
        st.markdown(f"- {item}")


def render_numbered_items(items):
    """Display a list as numbered items."""
    
    if not items:
        st.write("None identified.")
        return

    for index, item in enumerate(items, start=1):
        st.markdown(f"**{index}.** {item}")


def render_text(text):
    """Display text only when it exists."""
    
    if text:
        st.write(text)
    else:
        st.write("No information available.")


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


            # ==================================================
            # Extract results
            # ==================================================

            skills = result.get("skills_analysis", {})
            experience = result.get("experience_analysis", {})
            education = result.get("education_analysis", {})
            job_match = result.get("job_match_analysis", {})
            recommendations = result.get("recommendations", {})


            # ==================================================
            # Overview
            # ==================================================

            st.header("📊 Analysis Overview")

            score = job_match.get("match_score", 0)

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Job Match Score",
                    f"{score}/100"
                )

            with col2:

                technical_count = len(
                    skills.get("technical_skills", [])
                )

                st.metric(
                    "Technical Skills",
                    technical_count
                )

            with col3:

                gap_count = len(
                    job_match.get("missing_skills", [])
                )

                st.metric(
                    "Missing Skills",
                    gap_count
                )

            st.progress(score / 100)

            st.divider()


            # ==================================================
            # Skills Analysis
            # ==================================================

            st.header("🧠 Skills Analysis")

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("Technical Skills")

                render_bullets(
                    skills.get("technical_skills", [])
                )


                st.subheader("Soft Skills")

                render_bullets(
                    skills.get("soft_skills", [])
                )


            with col2:

                st.subheader("Tools & Technologies")

                render_bullets(
                    skills.get("tools_and_technologies", [])
                )


                st.subheader("Skill Gaps")

                render_bullets(
                    skills.get("skill_gaps", [])
                )


            st.divider()


            # ==================================================
            # Experience Analysis
            # ==================================================

            st.header("💼 Experience Analysis")

            st.subheader("Seniority Assessment")

            render_text(
                experience.get(
                    "seniority_assessment",
                    ""
                )
            )


            col1, col2 = st.columns(2)

            with col1:

                st.subheader("Roles")

                render_bullets(
                    experience.get("roles", [])
                )


                st.subheader("Relevant Experience")

                render_bullets(
                    experience.get("relevant_experience", [])
                )


                st.subheader("Achievements")

                render_bullets(
                    experience.get("achievements", [])
                )


            with col2:

                st.subheader("Strengths")

                render_bullets(
                    experience.get("strengths", [])
                )


                st.subheader("Areas to Improve")

                render_bullets(
                    experience.get("weaknesses", [])
                )


            st.divider()


            # ==================================================
            # Education Analysis
            # ==================================================

            st.header("🎓 Education Analysis")

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("Degrees")

                render_bullets(
                    education.get("degrees", [])
                )


                st.subheader("Fields of Study")

                render_bullets(
                    education.get("fields_of_study", [])
                )


                st.subheader("Certifications")

                render_bullets(
                    education.get("certifications", [])
                )


            with col2:

                st.subheader("Relevant Coursework")

                render_bullets(
                    education.get("relevant_coursework", [])
                )


                st.subheader("Strengths")

                render_bullets(
                    education.get("strengths", [])
                )


                st.subheader("Gaps")

                render_bullets(
                    education.get("gaps", [])
                )


            st.divider()


            # ==================================================
            # Job Match Analysis
            # ==================================================

            st.header("🎯 Job Match Analysis")

            st.subheader("Match Score")

            st.metric(
                "Overall Match",
                f"{score}/100"
            )

            st.progress(score / 100)


            col1, col2 = st.columns(2)

            with col1:

                st.subheader("✅ Matching Skills")

                render_bullets(
                    job_match.get("matching_skills", [])
                )


            with col2:

                st.subheader("⚠️ Missing Skills")

                render_bullets(
                    job_match.get("missing_skills", [])
                )


            st.subheader("Relevant Experience")

            render_bullets(
                job_match.get(
                    "relevant_experience",
                    []
                )
            )


            st.subheader("Experience Gaps")

            render_bullets(
                job_match.get(
                    "experience_gaps",
                    []
                )
            )


            st.subheader("Education Match")

            render_text(
                job_match.get(
                    "education_match",
                    ""
                )
            )


            col1, col2 = st.columns(2)

            with col1:

                st.subheader("💪 Strengths for Role")

                render_bullets(
                    job_match.get(
                        "strengths_for_role",
                        []
                    )
                )


            with col2:

                st.subheader("⚠️ Weaknesses for Role")

                render_bullets(
                    job_match.get(
                        "weaknesses_for_role",
                        []
                    )
                )


            st.divider()


            # ==================================================
            # Recommendations
            # ==================================================

            st.header("📝 Recommendations")

            with st.expander(
                "🎯 Skills to Emphasize",
                expanded=True
            ):

                render_bullets(
                    recommendations.get(
                        "skills_to_emphasize",
                        []
                    )
                )


            with st.expander(
                "💼 Experience Improvements"
            ):

                render_bullets(
                    recommendations.get(
                        "experience_improvements",
                        []
                    )
                )


            with st.expander(
                "📄 Resume Improvements"
            ):

                render_bullets(
                    recommendations.get(
                        "resume_improvements",
                        []
                    )
                )


            with st.expander(
                "🔑 Keywords to Consider"
            ):

                render_bullets(
                    recommendations.get(
                        "keywords_to_consider",
                        []
                    )
                )


            with st.expander(
                "🚀 Priority Actions",
                expanded=True
            ):

                render_numbered_items(
                    recommendations.get(
                        "priority_actions",
                        []
                    )
                )


        except Exception as e:

            st.error(
                f"An error occurred while analyzing the resume: {e}"
            )