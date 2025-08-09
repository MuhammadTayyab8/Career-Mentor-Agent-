import os
from dotenv import find_dotenv, load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Agent, Runner, function_tool
from openai.types.responses import ResponseTextDeltaEvent


load_dotenv(find_dotenv())
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("Please set gemini api key")


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