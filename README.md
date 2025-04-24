# Upwork Proposal Automation with Claude AI — V1

**Built by: Muhammad Rehman**  
_Automate. Personalize. Win more projects._

---

## What is this?

A CLI-based intelligent automation tool to **generate highly personalized Upwork proposals** using **Claude AI (Anthropic)**, based on:

- The job post description  
- Your past proposals (to match tone/style)  
- Your resume summary  
- Relevant projects (auto-selected based on tech stack)

This tool saves time, brings consistency, and improves your chances of getting noticed on Upwork.

---

## How it Works

1. You paste a job post in `job_description.txt`
2. The system loads:
   - Your `resume_summary.txt`
   - Your past proposals from `proposals.json`
   - Your projects from `projects.json`
3. It filters projects that match the job keywords
4. It uses a Claude 3.7-powered API call to generate a personalized proposal
5. Final proposal is printed in the terminal — ready to copy!

---

## Directory Structure

```
UPWORK-AUTOMATION/
│
├── main.py                  # Main CLI interface
├── generator.py             # Claude API handler
├── .env                     # API key & config
│
├── prompts/
│   └── base_prompt.txt      # Customizable Claude prompt
│
├── job_description.txt      # Paste your new job post here
├── resume_summary.txt       # Your professional summary
├── proposals.json           # Past proposals for style/tone
├── projects.json            # All your project experience
```

---

## Features

- Personalized proposals powered by Claude 3.7
- Smart project matching using `tech_stack`
- Customizable prompt & resume injection
- Works entirely from terminal (lightweight & local)
- 100% customizable & extendable

---

## Requirements

- Python 3.8+
- Claude API key (from [Anthropic Console](https://console.anthropic.com))
- `requests`, `dotenv`, `json`

Install dependencies:
```bash
pip install requests python-dotenv
```

---

## Sample Prompt Output

Paste this in `job_description.txt`:
```
Looking for a Shopify developer to improve my store’s performance and UX across mobile.
```

Run:
```bash
python main.py
```

Output (example):
```
✅ Proposal Generated:
Hey there, I’ve helped 50+ brands rebuild Shopify stores for speed and UX...
... (full custom proposal)
```

---

Want to contribute or give feedback? Feel free to fork the repo or drop a message.