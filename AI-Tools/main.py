from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai.chat_models import ChatMistralAI
from langchain.tools import tool
from datetime import date


@tool
def getCurrentDate():
    """Use this tool for getting the current date"""
    return str(date.today())

model = ChatMistralAI(model="mistral-small").bind_tools([getCurrentDate])

response = model.invoke("today's date ?")

tool_result = getCurrentDate.invoke(response.tool_calls[0]["args"])

secondary_response = model.invoke(
    ["Human:- Today's Date", "Tool result := " + tool_result]
)

print(secondary_response.text)
