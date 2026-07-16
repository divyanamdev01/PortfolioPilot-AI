from prompts import CHAT_PROMPT
from llm import ask_llm
from memory import load_memory

def chat_with_portfolio(question):

    user = load_memory()

    prompt = f"""
    {CHAT_PROMPT}

    Resume:
    {user['resume']}

    LinkedIn:
    {user['linkedin']}

    GitHub:
    {user['github']}

    Job Description:
    {user['job_description']}

    User Question:
    {question}
    """

    return ask_llm(prompt)