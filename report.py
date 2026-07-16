from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def  create_report(resume_analysis, linkedin_analysis, github_analysis, skill_gap, roadmap, projects, interview_questions):

    styles = getSampleStyleSheet()
    story = [Paragraph("PORTFOLIO & CAREER REPORT", styles['Title']), Spacer(1, 10)]
    
    sections = {
        "Resume Analysis": resume_analysis,
        "LinkedIn Analysis": linkedin_analysis,
        "GitHub Analysis": github_analysis,
        "Skill Gap Analysis": skill_gap,
        "Learning Roadmap": roadmap,
        "Recommended Projects": projects,
        "Interview Questions": interview_questions
    }
    
    for title, content in sections.items():
        if content:
        
            story.append(Paragraph(title, styles['Heading2']))
            
        
            story.append(Paragraph(str(content).replace('\n', '<br />'), styles['Normal']))
            
            
            story.append(Spacer(1, 10))
            
    # PDF generate karein
    pdf_path="Portfolio_Report_Plain.pdf"
    doc=SimpleDocTemplate(pdf_path)
    doc.build(story)
    return pdf_path



    
