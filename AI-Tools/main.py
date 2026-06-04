from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai.chat_models import ChatMistralAI
from langchain.tools import tool
from datetime import date


@tool
def getCurrentDate():
    """Use this tool for getting the current date"""
    return str(date.today())


print(getCurrentDate.invoke({}))