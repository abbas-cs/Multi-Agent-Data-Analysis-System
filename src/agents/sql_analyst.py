from langgraph.graph import StateGraph, START, END
from src.state import AgentState


graph = StateGraph(AgentState)

graph.add_edge('schema_inspection', schema_inspection)
graph.add_edge('sql_generation', sql_generation)
graph.add_edge('sql_validation', sql_validation)
graph.add_edge('execution', execution)
graph.add_edge('anslysis_output', analysis_output)