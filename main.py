from agents import Runner
import chainlit as cl
from setup_config import run_config
from expert.career_mentor_agent import career_mentor_agent
from openai.types.responses import ResponseTextDeltaEvent



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
    
