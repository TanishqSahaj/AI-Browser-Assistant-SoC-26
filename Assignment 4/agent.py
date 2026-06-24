from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from tools import TOOLS

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

agent = llm.bind_tools(TOOLS)