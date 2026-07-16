import json
from prompts import SKILL_GAP_PROMPT
from llm import ask_llm
import re

def analyze_skill_gap(resume, linkedin, github, jd):

    prompt = f"""
    {SKILL_GAP_PROMPT}

    Resume:
    {resume}

    LinkedIn:
    {linkedin}

    GitHub:
    {github}

    Job Description:
    {jd}
    """
    response = ask_llm(prompt,True)

    response = re.sub(r"```json|```", "", response).strip()

   

    return json.loads(response)