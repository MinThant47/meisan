from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# groq_api_key="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"
# groq_api_key="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"

groq_api_key = "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"

llm=ChatGroq(groq_api_key=groq_api_key,
             model_name="llama-3.3-70b-versatile")
             
prompt=ChatPromptTemplate.from_template(
"""
You are the chatbot for Yangon Technological Uniersity (YTU). Your name is MeiSan. You are created by 5th year EC students.
Greet the users whenever they introduce themselves.
Your task is to respond to users in a friendly, fun, and informative manner.
Please only provide responses based on the context.
But don't say words like according to provided text. Don't say hello or introduce yourself everytime user asks question. First time is enough.
<context>
{context}
<context>
Questions:{input}

"""
)