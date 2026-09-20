# import langchain
# print(langchain.__version__) 

from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
model = ChatGroq(model = "openai/gpt-oss-20b",temperature=0.9)
result = model.invoke("What are the ai trends currently ")
print(result.content )