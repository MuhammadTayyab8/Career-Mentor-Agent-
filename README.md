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

Example fields supported:
- Cybersecurity
- Data Science  
(You can extend this with more careers easily.)

---

## 🛠️ Technologies

- Python 🐍
- Chainlit (for chat interface)
- OpenAI Agent SDK
- Mock tools + multi-agent system


