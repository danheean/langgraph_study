from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from llm import llm

# LangChain이 지원하는 다른 채팅 모델을 사용합니다. 여기서는 Ollama를 사용합니다.
#llm = ChatOllama(model="EEVE-Korean-10.8B-Q5_K_M:latest")

# 프롬프트 설정
prompt = ChatPromptTemplate.from_template(
    "Translate following sentences into Korean:\n{input}"
)

# LangChain 표현식 언어 체인 구문을 사용합니다.
chain = prompt | llm | StrOutputParser()