from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client= OpenAI()

def ask_llm(prompt, json_mode=False):

    if json_mode:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt,
            text={"format": {"type": "json_object"}}
        )
    else:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )

    return response.output_text