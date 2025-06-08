from langchain.tools import Tool
import requests
def create_access_request(user: str, issue: str) -> str:
    ticket_id = requests.post(
        "https://dev123456.execute-api.us-east-1.amazonaws.com/production/tickets",
        json={"user": user, "issue": issue},
    )
    return f"✅ Access request created: {ticket_id}"

access_request_tool = Tool(
    name="ServiceNowAccessRequest",
    func=create_access_request,
    description="Create an access request ticket in ServiceNow."
)
