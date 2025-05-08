from dotenv import load_dotenv
import os
import openai
import requests
from typing import Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model 
from pydantic import BaseModel, Field
from typing_extensions import TypedDict


# Load environment variables from .env file
load_dotenv()


llm = init_chat_model("groq:gemma2-9b-it")

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

user_input = input("Enter your message: ")
state = graph.invoke({"messages": [{"role": "user", "content": user_input}]})


print(state['messages'])
print(state["messages"][-1].content)
# This code is a simple chatbot using LangGraph and Groq's API. It initializes a state graph, adds a chatbot node, and allows the user to input messages. The chatbot responds using the Gemma2-9B model.
