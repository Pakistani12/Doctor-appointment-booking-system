from langgraph.graph import StateGraph
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.llms import OpenAI
from agents.medical_agent import tools

from rag.rag_pipeline import get_rag_chain

llm = OpenAI()
rag_chain = get_rag_chain()

agent = create_openai_functions_agent(llm=llm, tools=tools)
executor = AgentExecutor(agent=agent, tools=tools)

def build_graph():
    builder = StateGraph()
    builder.add_node("RAG_QA", rag_chain)
    builder.add_node("AGENT", executor)
    builder.set_entry_point("AGENT")
    return builder.compile()