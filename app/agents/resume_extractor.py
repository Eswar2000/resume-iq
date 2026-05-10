from openai import OpenAI
from app.prompts import RESUME_EXTRACTION_PROMPT

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama', # Required but ignored locally
)

def extract_resume_info(resume_text):

    prompt = RESUME_EXTRACTION_PROMPT.format(resume_text=resume_text)

    response = client.chat.completions.create(
        model="phi3",
        messages=[
            {"role": "system", "content": "You are a strict resume JSON extraction engine. Never hallucinate or invent information."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    print(f"Response from Ollama: {response.choices[0].message.content}")
    return response.choices[0].message.content