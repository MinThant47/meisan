from langgraph.graph import END, StateGraph, START
from schema import route_question, retrieve_FAQ, retrieve_EC, retrieve_MCE, reply_404, get_command
from typing import List
from typing_extensions import TypedDict

class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        command: LLM command
        documents: list of documents
    """

    question: str
    command: str
    documents: List[str]


workflow = StateGraph(GraphState)
# Define the nodes
workflow.add_node("FAQ", retrieve_FAQ)  # web search
workflow.add_node("EC", retrieve_EC)  # retrieve
workflow.add_node("MCE", retrieve_MCE)  # retrieve
workflow.add_node("CMD", get_command)  # retrieve
workflow.add_node("404", reply_404)  # retrieve


# Build graph
workflow.add_conditional_edges(
    START,
    route_question,
    {
        "retrieve_FAQ": "FAQ",
        "retrieve_EC": "EC",
        "retrieve_MCE": "MCE",
        "get_command": "CMD",
        "reply_404": "404",
    },
)
workflow.add_edge( "FAQ", END)
workflow.add_edge( "EC", END)
workflow.add_edge( "MCE", END)
workflow.add_edge( "CMD", END)
workflow.add_edge( "404", END)

# Compile
app = workflow.compile()