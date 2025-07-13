# Career Mentor Agent 🎓

An AI-powered multi-agent system designed to guide users in their career planning journey.

---

## 🧠 How It Works

### 🧩 Agents Involved:

1. **career_mentor_agent** – The main agent that:
   - Receives user input.
   - Validates whether the question is related to `career`, `jobs`, or `skills`.
   - Rejects irrelevant questions politely.
   - Hands off the task to one of the specialized agents based on context.

2. **career_agent** – Suggests relevant fields and uses the tool `get_career_roadmap` to generate a skill roadmap for selected careers.

3. **skill_agent** – Provides skill-building plans and learning paths based on the user’s interest.

4. **job_agent** – Suggests real-world job roles based on the user’s selected field or career path.

---

## 🔧 Tool Used

### `get_career_roadmap(field: str)`

A mock function that returns a list of essential skills for a given field.
```
career_skills = {
    "cybersecurity": ["Network Security", "Ethical Hacking", "SIEM tools (Splunk)", "Python Scripting"],
    "data science": ["Python", "Pandas", "SQL", "Machine Learning", "Data Visualization"],
    "web development": ["HTML", "CSS", "JavaScript", "React", "Node.js"],
    "ai engineer": ["Python", "TensorFlow", "PyTorch", "Neural Networks"],
    "mobile app developer": ["Flutter", "Dart", "UI/UX Basics", "Firebase"]
}


---

## 🛠️ Technologies

- Python 🐍
- Chainlit (for chat interface)
- OpenAI Agent SDK
- Mock tools + multi-agent system


