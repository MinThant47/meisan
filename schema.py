from load import get_context
from llm_prompt import llm
from routes import question_router
from langchain.schema import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from tools import get_mark
from langchain_core.prompts import ChatPromptTemplate
from typing import Literal
from pydantic import BaseModel, Field


def reply_404(state):
    """
    used when relevant information in the documents can't be found

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, documents, that contains retrieved documents
    """
    print("---404 document---")
    question = HumanMessage(content=state["question"] + "The answer to the question isn't available in the document.")
    system_message = SystemMessage(content="You are a Yangon Technological University chat bot that provides polite and concise reponse when there is no relevant information in the given documents.")

    response = {"input": question, "answer": llm.invoke([system_message, question]).content}

    return {"documents": response, "question": question, "command": "stop"}


def get_command(state):
    """
    used when user asked for move forward or backward

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, documents, that contains retrieved documents
    """
    print("---Command Instruction---")
    question = HumanMessage(content=state["question"])
    system_message = SystemMessage(content="You are a fun physical robot who responds with sound actively when you ask me to move closer or step back or spin around. You can be also requested to smile or show a sad face!")

    response = {"input": question, "answer": llm.invoke([system_message, question]).content}

    class CommandQuery(BaseModel):
        """Classify user commands to relevant datasource."""

        datasource: Literal["forward", "backward", "spin", "smile", "sad"] = Field(
            ...,
            description="""You are given a user question, help me choose classification
            1. forward
            2. backward
            3. spin
            3. smile
            4. sad
            """
        )

    structured_llm_router = llm.with_structured_output(CommandQuery)

    # Prompt
    system = """You are an expert at classifying a user question to smile, sad, forward, and backward.
    returns forward if user ask for coming towards him (for eg. come closer, move forward)
    returns backward if user ask for moving backward (for eg. move backward, stay back)
    returns spin if user ask to spin around. (for eg. spin around, make a round)
    returns smile if user ask to make a smiley face or make a smile.
    returns sad if user make you a sad face.
    """

    command_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
    )

    command_router = command_prompt | structured_llm_router
    classifier = command_router.invoke({"question": question})
    
    return {"documents": response, "question": question, "command": classifier.datasource}


def retrieve_FAQ(state):
    """
    Retrieve documents

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, documents, that contains retrieved documents
    """
    print("---RETRIEVE FAQ---")
    
    question = state["question"]
    response = get_context("YTUFAQ", question)

    return {"documents": response, "question": question, "command": "stop"}


def retrieve_EC(state):
    """
    Retrieve documents

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, documents, that contains retrieved documents
    """
    print("---RETRIEVE EC---")
    question = state["question"]
    # Retrieval
    response = get_context("YTUEC", question)

    return {"documents": response, "question": question, "command": "stop"}

def retrieve_MCE(state):
    """
    Retrieve documents

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, documents, that contains retrieved documents
    """
    print("---RETRIEVE MCE---")
    question = state["question"]
    response = get_context("YTUMCE", question)
    print(state)
    return {"documents": response, "question": question, "command": "stop"}

def route_question(state):
    """
    Route question to FAQ or EC or MCE or CMD or 404.

    Args:
        state (dict): The current graph state

    Returns:
        str: Next node to call
    """

    print("---ROUTE QUESTION---")
    question = state["question"]
    source = question_router.invoke({"question": question})
    if source.datasource == "FAQ":
        print("---ROUTE QUESTION TO FAQ---")
        return "retrieve_FAQ"
    elif source.datasource == "EC":
        print("---ROUTE QUESTION TO EC---")
        return "retrieve_EC"
    elif source.datasource == "MCE":
        print("---ROUTE QUESTION TO MCE---")
        return "retrieve_MCE"
    elif source.datasource == "CMD":
        print("---ROUTE QUESTION TO CMD---")
        return "get_command"    
    else:
        print("Can't find related documents")
        return "reply_404"