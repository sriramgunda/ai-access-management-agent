from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from splunk_tools import splunk_tool
from servicenow_tools import access_request_tool

llm = ChatOpenAI(temperature=0, model="gpt-4")
agent = initialize_agent(
    tools=[splunk_tool, access_request_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)