from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# LangChain이 지원하는 다른 채팅 모델을 사용합니다. 여기서는 Ollama를 사용합니다.
# llm = ChatOllama(model="EEVE-Korean-10.8B:latest")


#llm = ChatOllama(model="EEVE-Korean-10.8B-Q5_K_M:latest")
#llm = ChatOllama(model="llama3-instruct-8b:latest")

#llm = ChatOllama(model="mistral:latest")
#llm = ChatOllama(model="qwen2:latest")
#llm = ChatOllama(model="phi3:latest")

#llm = ChatOllama(model="gemma2:9b") // error
llm = ChatOllama(model="gemma:7b")
