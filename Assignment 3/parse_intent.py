import json
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

from prompts import SYSTEM_PROMPT

load_dotenv()

client = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    timeout=30
)


async def parse_intent(user_command: str):

    response = client.invoke([
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_command)
    ])

    output = response.content.strip()

    if output.startswith("```json"):
        output = output.replace("```json", "", 1)

    if output.endswith("```"):
        output = output[:-3]

    output = output.strip()

    return json.loads(output)