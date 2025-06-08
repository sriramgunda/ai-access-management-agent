from langchain.tools import Tool
import requests, json

def query_splunk_access_issues(user: str = "") -> str:
    query = (
      f'search index=auth_logs ( "access denied" OR "account locked" )'
      f' {"user="+user if user else ""}'
      ' | stats count by user,error'
    )
    results = requests.get("http://localhost:8080/services/search/jobs", params={"search": query}).json()["results"]
    return json.dumps(results)  # simplified example

splunk_tool = Tool(
    name="SplunkAccessLogTool",
    func=query_splunk_access_issues,
    description="Query Splunk for access errors like 'access denied', 'account locked'."
)
