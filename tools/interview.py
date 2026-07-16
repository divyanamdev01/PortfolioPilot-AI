from llm import ask_llm
from prompts import INTERVIEW_PROMPT
def generate_interview_questions(profile):

    prompt = f"""
    {INTERVIEW_PROMPT}

    Candidate Profile
    {profile}
    """

    response = ask_llm(prompt)

    return response