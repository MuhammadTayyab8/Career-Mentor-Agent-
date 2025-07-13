import os
from dotenv import find_dotenv, load_dotenv
import chainlit as cl
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Agent, Runner, function_tool
from openai.types.responses import ResponseTextDeltaEvent


load_dotenv(find_dotenv())
gemini_api_key = os.getenv("GEMINI_API_KEY")


# STEP#1
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/" 
)

#STEP#2
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", 
    openai_client=provider
)


#STEP#3
run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled = True,
)




# TOOL
career_skills = {
    "cybersecurity": ["Network Security", "Ethical Hacking", "SIEM tools (Splunk)", "Python Scripting"],
    "data science": ["Python", "Pandas", "SQL", "Machine Learning", "Data Visualization"],
    "web development": ["HTML", "CSS", "JavaScript", "React", "Node.js"],
    "ai engineer": ["Python", "TensorFlow", "PyTorch", "Neural Networks"],
    "mobile app developer": ["Flutter", "Dart", "UI/UX Basics", "Firebase"]
}

@function_tool
@cl.step(type="Roadmap of skills")
def get_career_roadmap(field: str) -> dict:
    """This return a roadmap of provided skill"""
    skills = career_skills.get(field.lower())
    if skills:
        return {"skills": skills}
    return {"skills": ["Research", "Field-specific tools", "Certifications"]}



# Carrer Agent
career_agent = Agent(
    name="Career Agent",
    instructions="Answer user question about career, suggests fields and gives roadmap using tool get_career_roadmap",
    tools=[get_career_roadmap]
)


# SkillAgent
skill_agent = Agent(
    name="Skill Agent",
    instructions="provide user shows skill-building plans based on user query"
)


# JobAgent
job_agent = Agent(
    name="Job Agent",
    instructions="shares real-world job roles based on user provided stream"
)




# MAIN AGENT
career_mentor_agent  = Agent(
    name="Career Mentor Agent ",
    instructions="""You are a Career Mentor Agent user ask you from study, career, jobs, skill if the 
    user question not related to these tells user that you only talk about these use agents to answer 
    based on user ask
    """,
    handoffs=[career_agent, skill_agent, job_agent]
)







@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message("Hello! I am a Career Mentor Agent").send()








@cl.on_message
async def main(message: cl.Message):
    try:
        history = cl.user_session.get("history")

        msg = cl.Message(content="")
        await msg.send()

        history.append({"role": "user", "content": message.content})


        result = Runner.run_streamed(
            career_mentor_agent,
            input=history,
            run_config=run_config
        )


        collected = ''

        async for event in result.stream_events():

            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                token = event.data.delta
                collected += token
                await msg.stream_token(token)

        history.append({"role": "assistant", "content": result.final_output})

        msg.content = collected
        await msg.update()

    except Exception as e:
        await cl.Message(content=f"Error: {str(e)}").send()
        raise
    

    


