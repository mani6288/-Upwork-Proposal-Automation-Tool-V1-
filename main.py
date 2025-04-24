import json
from generator import generate_proposal

def load_json_data():
    with open("proposals.json", "r") as f:
        data = json.load(f)
    return [item["submitted_proposal"] for item in data]

def load_resume():
    with open("resume_summary.txt", "r") as f:
        return f.read()

def load_job_description():
    with open("job_description.txt", "r") as f:
        return f.read()

def load_projects():
    with open("projects.json", "r") as f:
        return json.load(f)

def get_relevant_projects(job_description, all_projects):
    job_lower = job_description.lower()
    relevant = []

    for project in all_projects:
        for tech in project.get("tech_stack", []):
            if tech.lower() in job_lower:
                relevant.append(f"- **{project['title']}**: {project['summary']}")
                break  # one match is enough to include the project

    if not relevant:
        return "No direct match found, but relevant project experience can be shared upon request."
    
    return "\n".join(relevant)

def main():
    job_description = load_job_description()
    past_proposals = "\n\n---\n\n".join(load_json_data())
    resume_summary = load_resume()
    all_projects = load_projects()
    relevant_projects = get_relevant_projects(job_description, all_projects)

    print("⏳ Generating Proposal...\n")
    proposal = generate_proposal(job_description, past_proposals, resume_summary, relevant_projects)

    if proposal:
        print("✅ Proposal Generated:\n")
        print(proposal)
    else:
        print("❌ Failed to generate proposal.")

if __name__ == "__main__":
    main()
