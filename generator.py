import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")
API_URL = "https://api.anthropic.com/v1/messages"
HEADERS = {
    "x-api-key": API_KEY,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json"
}

def generate_proposal(job_description, past_proposals, resume_summary, relevant_projects):
    with open("prompts/base_prompt.txt", "r") as f:
        prompt_template = f.read()

    prompt = prompt_template.format(
        job_description=job_description.strip(),
        past_proposals=past_proposals.strip(),
        resume_summary=resume_summary.strip(),
        relevant_projects=relevant_projects.strip()
    )

    body = {
        "model": "claude-3-opus-20240229",
        "max_tokens": 1000,
        "temperature": 0.7,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=HEADERS, json=body)

    if response.status_code == 200:
        return response.json()["content"][0]["text"]
    else:
        print("❌ Error:", response.status_code, response.text)
        return None
