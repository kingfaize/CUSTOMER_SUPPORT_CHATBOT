import requests

MCP_SERVER_URL = "https://vipfapwm3x.us-east-1.awsapprunner.com/mcp"

headers = {
    "Accept": "text/event-stream",
    "Content-Type": "application/json"
}

data = {
    "jsonrpc": "2.0",
    "method": "help",
    "id": 1
}

try:
    response = requests.post(MCP_SERVER_URL, headers=headers, json=data, timeout=10)
    print("Status Code:", response.status_code)
    print("Response Headers:", response.headers)
    print("\n--- Response Content ---\n")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
