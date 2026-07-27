import streamlit as st
import os
from memory import save_memory
from chat import chat_with_portfolio
from agent import run_agent
from tools.resume_tool import resume_text
from tools.linkedIn_tool import linkedin_text
from tools.github_tool import smry
import requests

from tools.jd_tool import *


st.set_page_config(
    page_title="PortfolioPilot AI",
    layout="centered"
    page_icon="🤖"
)




st.title("🤖 AI Portfolio Analyzer")


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)



# ---------------- Session State ----------------

if "report" not in st.session_state:
    st.session_state.report = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "pdf_path" not in st.session_state:
    st.session_state.pdf_path = None
    
if "analysis_count" not in st.session_state:
    st.session_state.analysis_count = 0

MAX_ANALYSES = 2
# ---------------- Form ----------------

with st.form("portfolio_form"):

    resume = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf"]
    )

    
    linkedin = st.file_uploader(
        "💼 Upload LinkedIn PDF",
        type=["pdf"]
    )

    github_url = st.text_input(
        "🐙 GitHub Profile URL"
    )

    job_description = st.text_area(
        "📝 Job Description (Optional)"
    )

    job_pdf = st.file_uploader(
        "📄 Upload Job Description PDF (Optional)",
        type=["pdf"]
    )

    submitted = st.form_submit_button(
        "Analyze Portfolio"
    )

# ---------------- Analyze ----------------

if submitted:
     # Check usage limit first
    if st.session_state.analysis_count >= MAX_ANALYSES:
        st.error("🚫 You have reached the maximum limit of 2 analyses.")
        st.info("You can only analyze your portfolio 2 times.")

    elif not resume:
        st.error("Upload Resume")

    elif not linkedin:
        st.error("Upload LinkedIn")

    elif not github_url:
        st.error("Enter GitHub URL")

    else:
        resume = resume_text(resume)
        linkedin = linkedin_text(linkedin)
        git= smry(github_url)


        jb= x_y_z(job_description,job_pdf)
        save_memory({
            "resume": resume,
            "linkedin": linkedin,
            "github": git,
            "job_description": jb,
          
        })

        with st.spinner("Analyzing..."):
            result=run_agent()
             # Count only after successful analysis
            st.session_state.analysis_count += 1
            st.session_state.report = result
            st.session_state.pdf_path = result.get("pdf")

# ---------------- Result ----------------

if st.session_state.report:

    st.success("Portfolio Analysis Completed")

   
    pdf_path = st.session_state.get("pdf_path")

    if pdf_path and os.path.exists(pdf_path):
        with open(st.session_state.pdf_path, "rb") as pdf_file:
            st.download_button(
                "📥 Download PDF Report",
                data=pdf_file,
                file_name="Portfolio_Report.pdf",
                mime="application/pdf"
            )

    else:
        st.error('PDF file not found')

    st.divider()

    st.subheader("💬 Chat With Your Portfolio")

    question = st.chat_input(
        "Ask anything about your portfolio..."
    )

    if question:

        answer = chat_with_portfolio(question)

        st.session_state.chat_history.append(
            ("You", question)
        )

        st.session_state.chat_history.append(
            ("AI", answer)
        )

    for role, message in st.session_state.chat_history:

        with st.chat_message(role):

            st.write(message)
