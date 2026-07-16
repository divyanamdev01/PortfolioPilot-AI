from llm import ask_llm
from prompts import ROADMAP_PROMPT

def generate_roadmap(analysis):
        prompt = f"""
            {ROADMAP_PROMPT}

            Missing Skills:
            {analysis}
        """
        roadmap= ask_llm(prompt)
        return roadmap