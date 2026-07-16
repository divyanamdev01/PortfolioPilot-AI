# 🤖 PortfolioPilot AI

An AI-powered career assistant that analyzes your Resume, LinkedIn profile, GitHub profile, and Job Description to provide personalized career insights, skill gap analysis, project recommendations, learning roadmap, interview questions, and a downloadable PDF report.

---

## 📌 Overview

PortfolioPilot AI helps students and professionals evaluate their technical portfolio using Artificial Intelligence. By combining information from your Resume, LinkedIn profile, GitHub profile, and a target Job Description, the application provides personalized feedback and actionable recommendations to improve your chances of landing your desired role.

---

## ✨ Features

- 📄 Resume Analysis
- 💼 LinkedIn Profile Analysis
- 💻 GitHub Profile Analysis
- 🎯 Job Description Analysis
- 📊 Skill Gap Analysis
- 🛣 Personalized Learning Roadmap
- 💡 AI Project Recommendations
- 🎤 Interview Question Generation
- 💬 AI Portfolio Chat Assistant
- 📑 Downloadable PDF Report

---

## 📸 Screenshots

### Home Page

![Home](screenshots/home.png)

### Portfolio Analysis

![Analysis](screenshots/analyzing.png)

### Results & AI Chat

![Result](screenshots/result.png)

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI
- OpenAI GPT

### Libraries
- Streamlit
- OpenAI
- Requests
- PyPDF2
- ReportLab
- python-dotenv

---

## 📂 Project Structure

```text
PortfolioPilot-AI/
│
├── app.py
├── memory.py
├── report.py
├── requirements.txt
├── .env
│
├── uploads/
│
├── tools/
│   ├── resume_tool.py
│   ├── linkedIn_tool.py
│   ├── github_tool.py
│   ├── jd_tool.py
│   ├── skill_gap.py
│   ├── roadmap.py
│   ├── project.py
│   └── interview.py
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/PortfolioPilot-AI.git
```

### 2. Navigate to the Project

```bash
cd PortfolioPilot-AI
```

### 3. Create a Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

---

## 🚀 How It Works

1. Upload your Resume (PDF).
2. Upload your LinkedIn profile PDF.
3. Enter your GitHub profile URL.
4. Paste or upload a Job Description (optional).
5. Click **Analyze Portfolio**.
6. The AI analyzes your portfolio and generates:
   - Resume Analysis
   - LinkedIn Analysis
   - GitHub Analysis
   - Skill Gap Analysis
   - Learning Roadmap
   - Project Recommendations
   - Interview Questions
7. Download the generated PDF report.
8. Chat with your portfolio using the AI assistant.

---

## 📊 Output

The application generates a detailed AI-powered report containing:

- Resume Review
- LinkedIn Feedback
- GitHub Feedback
- Skill Gap Analysis
- Personalized Learning Roadmap
- Recommended Projects
- Interview Questions
- PDF Report

---

## 🎯 Future Improvements

- User Authentication
- ATS Resume Score
- Resume Optimization Suggestions
- GitHub Repository-Level Analysis
- AI Mock Interviews
- Portfolio Score
- Course Recommendations
- Multi-language Support
- Cloud Deployment

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Divya Namdev**

- GitHub: https://github.com/divyanamdev01
- LinkedIn: https://www.linkedin.com/in/divya-namdev-3550b92b3/

---

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub. Your support helps the project reach more developers and motivates future improvements.