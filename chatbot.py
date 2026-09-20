from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage

load_dotenv

model = ChatGroq(model = "openai/gpt-oss-20b")
msg = [(
    SystemMessage
)]
while True:
    user = input("User: ")
    if user=="0":
        break
    msg.append(user)
    result = model.invoke(user)
    msg.append(result.content)
    print("Bot:",result.content)
print(msg)

