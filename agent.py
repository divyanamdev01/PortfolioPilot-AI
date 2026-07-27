from memory import load_memory
from tools.skill_gap import analyze_skill_gap
from tools.roadmap import generate_roadmap
from tools.project import recommend_projects
from tools.interview import generate_interview_questions
from report import create_report


def run_agent():

    user = load_memory()
    resume=user["resume"]

    linkedin= user["linkedin"]

    github =user["github"]


    analysis = analyze_skill_gap(

        user["resume"],

        user["linkedin"],

        user["github"],

        user["job_description"]

    )

    roadmap = generate_roadmap(
        analysis
    )

    projects = recommend_projects(
        analysis
    )

    interview = generate_interview_questions(
        analysis
    )

    pdf = create_report(
        resume_analysis=resume,

        linkedin_analysis=linkedin,

        github_analysis=github,

        skill_gap=analysis,

        roadmap=roadmap,

        projects=projects,

        interview_questions=interview

    )

    print(pdf)
   
    return {
        "analysis": analysis,
        "roadmap": roadmap,
        "projects": projects,
        "interview": interview,
        "pdf": pdf
    }

