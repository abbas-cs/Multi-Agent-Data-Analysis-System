from typing import TypedDict, List, Annotated
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages

class AgentState(TypedDict):
    user_query: str
    messages: Annotated[List[BaseMessage], add_messages]
    sql_query: str
    db_schema: str