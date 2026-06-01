from dotenv import load_dotenv
load_dotenv()


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage,AIMessage

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

messages = []

while True:
    userInput = input("Enter Prompt ......")

    messages.append(HumanMessage(userInput))

    response = model.invoke(messages)

    messages.append(AIMessage(response.content))

    print(response.text)

