import os
from dotenv import find_dotenv, load_dotenv
import chainlit as cl
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Agent, Runner
import asyncio



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



#STEP#4
agent1 = Agent(
    name="Tayyab Agent",
    instructions="You are a helpful agent."
)


user_input = input("Enter Query: ")


async def main():
    result = await Runner.run(
        agent1,
        input=user_input,
        run_config=run_config
    )

    print(result.final_output)


asyncio.run(main())


