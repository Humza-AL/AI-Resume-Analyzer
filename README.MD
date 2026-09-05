# AI Resume Analyzer

An AI-powered resume analysis application that compares a resume against a job description and provides structured feedback on skills, experience, education, job fit, and areas for improvement.

The application uses **LangGraph** to organize the analysis into separate processing nodes and **Streamlit** to provide an interactive web interface.

---

## Features

### 🧠 Skills Analysis

Analyzes the skills found in a resume and identifies:

* Technical skills
* Soft skills
* Tools and technologies
* Skill gaps

### 💼 Experience Analysis

Evaluates the candidate's professional experience, including:

* Previous roles
* Relevant experience
* Achievements
* Strengths
* Weaknesses
* Estimated seniority level

### 🎓 Education Analysis

Reviews educational background and identifies:

* Degrees
* Fields of study
* Certifications
* Relevant coursework
* Education strengths
* Potential education gaps

### 🎯 Job Match Analysis

Compares the resume against a provided job description and evaluates:

* Overall match score
* Matching skills
* Missing skills
* Relevant experience
* Experience gaps
* Education alignment
* Strengths for the role
* Weaknesses for the role

### 📝 Resume Recommendations

Generates actionable recommendations based on the analysis, including:

* Skills to emphasize
* Experience improvements
* Resume improvements
* Keywords to consider
* Priority actions

---

## Architecture

The application uses **LangGraph** to coordinate multiple analysis nodes that operate on a shared resume analysis state.

```text
                    ┌───────────────┐
                    │   Streamlit   │
                    │    app.py     │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  PDF Resume   │
                    │ Text Extract  │
                    └───────┬───────┘
                            │
                            ▼
                    ┌────────────────────┐
                    │   LangGraph State  │
                    │    ResumeState     │
                    └─────────┬──────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
        ┌───────────┐   ┌────────────┐  ┌────────────┐
        │  Skills   │   │ Experience │  │ Education  │
        │   Node    │   │    Node    │  │    Node    │
        └─────┬─────┘   └─────┬──────┘  └─────┬──────┘
              │               │               │
              └───────────────┼───────────────┘
                              ▼
                     ┌────────────────┐
                     │   Job Match    │
                     │      Node      │
                     └───────┬────────┘
                             │
                             ▼
                     ┌────────────────┐
                     │ Recommendations│
                     │      Node      │
                     └───────┬────────┘
                             │
                             ▼
                     ┌────────────────┐
                     │   Streamlit    │
                     │    Results     │
                     └────────────────┘
```

The graph allows each analysis component to work with the shared state rather than putting the entire analysis process into one large function.

---

## Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── graph.py
├── model.py
├── nodes.py
├── schema.py
├── state.py
├── tools.py
│
├── test_education.py
├── test_experience.py
├── test_graph.py
├── test_jobmatch.py
├── test_parallel.py
├── test_recommendations.py
├── test_skills.py
├── test_tools.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

### `app.py`

The Streamlit frontend for the application.

It handles:

* Resume PDF uploads
* Job description input
* Running the analysis
* Displaying analysis results
* Presenting the results in a structured dashboard

### `graph.py`

Defines and compiles the LangGraph workflow.

It:

* Creates the `StateGraph`
* Registers analysis nodes
* Defines the relationships between nodes
* Compiles the graph used by the application

### `nodes.py`

Contains the main analysis functions used by the graph.

The nodes are responsible for:

* Skills analysis
* Experience analysis
* Education analysis
* Job matching
* Recommendation generation

### `model.py`

Contains the configuration for the language model used by the application.

Keeping model configuration separate from the graph and application logic makes it easier to modify or replace the model.

### `schema.py`

Defines structured schemas for the AI-generated analysis.

These schemas help ensure that model responses follow a predictable structure rather than returning completely unstructured text.

### `state.py`

Defines the shared state used throughout the LangGraph workflow.

The state contains information such as:

* Resume text
* Job description
* Skills analysis
* Experience analysis
* Education analysis
* Job match analysis
* Recommendations

Each node can read information from the state and add its results back into it.

### `tools.py`

Contains utility functions used by the application.

These include:

* Extracting text from PDF resumes
* Cleaning extracted resume text

### Test Files

The project includes separate test scripts for different parts of the system.

Examples include:

* `test_skills.py`
* `test_experience.py`
* `test_education.py`
* `test_jobmatch.py`
* `test_recommendations.py`
* `test_tools.py`
* `test_parallel.py`
* `test_graph.py`

These scripts are used to test individual components as well as the complete LangGraph workflow.

---

## How It Works

The application follows a multi-step analysis pipeline.

### 1. Upload Resume

The user uploads their resume as a PDF through the Streamlit interface.

### 2. Extract Resume Text

The PDF is processed and its text is extracted.

The extracted text is then cleaned before being passed to the AI analysis pipeline.

### 3. Create Graph State

The cleaned resume text and job description are placed into the shared `ResumeState`.

The state acts as the central data structure passed through the LangGraph workflow.

### 4. Analyze Skills, Experience, and Education

The graph processes the resume through separate analysis nodes.

These nodes evaluate:

* Skills
* Professional experience
* Education

The results are stored back into the shared state.

### 5. Analyze Job Match

The job match node compares the resume information with the provided job description.

It identifies areas where the candidate matches the position as well as areas where the resume may be missing relevant qualifications.

### 6. Generate Recommendations

The recommendation node uses the previous analysis results to generate actionable suggestions for improving the candidate's resume and positioning for the target role.

### 7. Display Results

The final state is returned to the Streamlit application and presented as a structured analysis dashboard.

---

## Technologies Used

### Programming Language

* Python

### AI / LLM

* LangChain
* LangGraph
* Pydantic

### User Interface

* Streamlit

### Document Processing

* PyPDF

### Development Tools

* Git
* GitHub
* Python virtual environments

---

## Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Then move into the project directory:

```bash
cd AI-Resume-Analyzer
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

On Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

If the application requires API credentials, create a `.env` file in the project directory.

Example:

```text
YOUR_API_KEY_NAME=your_api_key_here
```

Do **not** commit API keys or other credentials to GitHub.

The `.env` file is included in `.gitignore` to help prevent accidental commits.

---

## Running the Application

After activating the virtual environment, run:

```bash
streamlit run app.py
```

Streamlit will start the application and provide a local URL in the terminal.

Open that URL in your browser.

---

## Using the Application

1. Open the Streamlit application.
2. Upload your resume as a PDF.
3. Paste the job description into the text box.
4. Click **Analyze Resume**.
5. Wait for the LangGraph workflow to finish.
6. Review the generated analysis and recommendations.

---

## Testing

Individual components can be tested using the included test files.

For example:

```bash
python test_skills.py
```

```bash
python test_experience.py
```

```bash
python test_education.py
```

```bash
python test_jobmatch.py
```

```bash
python test_recommendations.py
```

The complete graph can be tested with:

```bash
python test_graph.py
```

---

## Example Workflow

A typical analysis looks like:

```text
Resume PDF
    ↓
Text Extraction
    ↓
Text Cleaning
    ↓
ResumeState
    ↓
┌───────────────┬────────────────┬────────────────┐
│ Skills        │ Experience     │ Education      │
│ Analysis      │ Analysis       │ Analysis       │
└───────────────┴────────────────┴────────────────┘
                    ↓
              Job Match Analysis
                    ↓
             Recommendations
                    ↓
             Streamlit Dashboard
```

For example, when analyzing a Machine Learning Engineer position, the application can identify relevant skills such as Python, machine learning, SQL, deep learning, and LLM-related technologies while also identifying areas where the resume may have less evidence.

---

## Project Overview

This project was built to explore how **LLMs, LangGraph, structured outputs, and traditional Python application logic** can be combined to create a practical AI application.

The project provided hands-on experience with:

* Designing a multi-node LangGraph workflow
* Managing shared state between nodes
* Structuring LLM outputs with schemas
* Processing PDF documents
* Building a Streamlit application
* Testing individual components
* Connecting backend AI logic to a user interface
* Using Git and GitHub for version control

---

## Author

**Humza Alvi**

AI / Machine Learning portfolio project focused on LLM applications, LangChain, LangGraph, and Python.
