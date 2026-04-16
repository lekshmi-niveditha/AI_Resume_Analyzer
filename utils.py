import PyPDF2
from skills import SKILLS
from sample_jobs import JOB_ROLES


def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text.lower()


def analyze_resume(text, job_role):
    resume_skills = []

    # Extract skills
    for skill in SKILLS:
        if skill.lower() in text:
            resume_skills.append(skill)

    job_skills = JOB_ROLES[job_role]

    matched_skills = list(set(resume_skills) & set(job_skills))
    missing_skills = list(set(job_skills) - set(resume_skills))

    # Score calculation
    if len(job_skills) == 0:
        score = 0
    else:
        score = int((len(matched_skills) / len(job_skills)) * 100)

    # Suggestions
    suggestions = []

    if score < 50:
        suggestions.append("Add more relevant skills to your resume.")
    if len(missing_skills) > 0:
        suggestions.append(f"Try to include skills like: {', '.join(missing_skills[:5])}")
    if "project" not in text:
        suggestions.append("Add project experience to strengthen your resume.")
    if "internship" not in text:
        suggestions.append("Include internship/work experience.")

    return {
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }