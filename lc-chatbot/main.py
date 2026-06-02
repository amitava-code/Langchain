from dotenv import load_dotenv
load_dotenv()


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai.chat_models import ChatMistralAI
from langchain.messages import HumanMessage,AIMessage


model = ChatMistralAI(model ="mistral-small-latest")

messages = []

while True:
    userInput = input("Enter Prompt ......")

    messages.append(HumanMessage(userInput))

    response = model.invoke(messages)

    messages.append(AIMessage(response.content))

    print(response.text)

