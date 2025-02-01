### Router
from typing import Literal
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
import os
from llm_prompt import llm

# Data model
class RouteQuery(BaseModel):
    """Route a user query to the most relevant datasource."""

    datasource: Literal["FAQ", "EC", "MCE", "CMD", "404"] = Field(
        ...,
        description="""You are given a user question, help me choose a route to
        1. FAQ
        2. EC
        3. MCE
        4. CMD
        5. 404""",
    )


structured_llm_router = llm.with_structured_output(RouteQuery)

# Prompt
system = """You are an expert at routing a user question to FAQ or EC or MCE or 404.
The FAQ contains about greeting the user, finding general university questions such as about the majors, who is the pro rector and else.
The EC contains in depth about electronic engineering in YTU, topics such as fields and career of electronics engineering.
The MCE contains in depth about robotic, ai and mechatronic engineering in YTU, topics such as fields and career and advancement.
The CMD is routed when user asked for instructions like "Move Forward, Stay Backward, Come Here, Spin around, make a smiley face, make a sad face and so on".
If you can't find any related thing for the above topics, then reply 404
"""

route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

question_router = route_prompt | structured_llm_router

# print(
#     question_router.invoke(
#         {"question": "What are the aspects of electronic engineering?"}
#     )
# )
# print(question_router.invoke({"question": "What is robotic major in YTU?"}))
# print(question_router.invoke({"question": "Come to me closer please?"}))