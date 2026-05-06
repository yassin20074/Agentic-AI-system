#Retrieve the required libraries 
from typing import Annotated, List, TypedDict
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from Tool import tools, search_tool
from database import get_checkpointer

#Input definition 
class AgentState(TypedDict):
    messages: Annotated[List, add_messages]
#Creating Llm 
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Definition of an agent 
def researcher(state: AgentState):
    llm_with_tools = llm.bind_tools(tools)
    response = llm_with_tools.invoke([
        SystemMessage(content="You are a technical researcher; use the tool to gather information. ")  
    ] + state['messages'])
    return {"messages": [response]}

#Linking the tools 
from langgraph.prebuilt import ToolNode, tools_condition
tool_node = ToolNode(tools=[search_tool])

# Building a Graph 
builder = StateGraph(AgentState)
builder.add_node("researcher", researcher)
builder.add_node("tools", tool_node)

builder.set_entry_point("researcher")
builder.add_conditional_edges("researcher", tools_condition)
builder.add_edge("tools", "researcher")

# Linking the agent to memory 
checkpointer = get_checkpointer()
agent_app = builder.compile(checkpointer=checkpointer)
