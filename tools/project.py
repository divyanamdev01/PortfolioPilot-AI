from prompts import PROJECT_PROMPT
from llm import ask_llm

def recommend_projects(analysis):

    prompt = f"""
    {PROJECT_PROMPT}

    Candidate Profile
    {analysis}
    """

    response = ask_llm(prompt)

    return response