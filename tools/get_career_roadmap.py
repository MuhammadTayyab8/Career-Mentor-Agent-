import os
from dotenv import find_dotenv, load_dotenv
from agents import AsyncOpenAI, function_tool, RunContextWrapper
from typing import TypedDict


load_dotenv(find_dotenv())
gemini_api_key = os.getenv("GEMINI_API_KEY")



# STEP#1
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/" 
)


class CareerRoadmapToolInput(TypedDict):
    career_field: str


@function_tool
async def get_career_roadmap(wrapper: RunContextWrapper, input: CareerRoadmapToolInput) -> dict:
    """Generate a career roadmap based on input"""
    try:
        print("Career roadmap...")
        prompt = (
            f"I am interested in becoming a {input['career_field']}.\n"
            "Please create a clear and structured career roadmap from beginner to advanced.\n"
            "Include skill stages, recommended learning resources, certifications, and practical experience steps.\n"
            "Format the answer as numbered stages."
        )

        response = await client.chat.completions.create(
            model="gemini-2.0-flash", 
            messages=[{"role": "user", "content": prompt}]
        )

        print(response.choices[0].message, 'retuennnn')

        # Wrap in dict (struct)
        return {
            "career_field": input["career_field"],
            "roadmap": response.choices[0].message.content.strip()
        }

    except Exception as e:
        print(f"Error in tool {str(e)}")
        return {"error": f"Error in tool {str(e)}"}
