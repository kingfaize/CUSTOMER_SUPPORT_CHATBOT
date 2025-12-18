
import os
import streamlit as st
import requests
import openai
from dotenv import load_dotenv
from logger import get_logger



# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "https://vipfapwm3x.us-east-1.awsapprunner.com/mcp")
LLM_MODEL = "gpt-4o"
logger = get_logger()

st.set_page_config(page_title="Customer Support Chatbot", page_icon="💬")
st.title("💬 Customer Support Chatbot Demo")

if not OPENAI_API_KEY:
    st.warning("Please set your OpenAI API key in the environment variable 'OPENAI_API_KEY'.")
    st.stop()

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []


# Display chat history
for msg in st.session_state["messages"]:
    st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")

# Chat input at the bottom for follow-up
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", "", key="user_input")
    submitted = st.form_submit_button("Send")

def call_mcp_server(user_message):
    # Enhanced: send user message to MCP server and provide debug info
    try:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        # Example test customer (replace with UI input or logic as needed)
        test_email = "donaldgarcia@example.net"
        test_pin = "7912"
        json_payload = {
            "jsonrpc": "2.0",
            "method": "get",
            "params": {
                "email": test_email,
                "pin": test_pin
            },
            "id": 1
        }
        response = requests.post(
            MCP_SERVER_URL,
            json=json_payload,
            headers=headers,
            timeout=10
        )
        debug_info = f"MCP DEBUG: status={response.status_code}, headers={response.headers}, text={response.text}"
        logger.debug(f"MCP request: {json_payload}")
        logger.debug(debug_info)
        if response.status_code == 200:
            try:
                data = response.json()
                result = data.get("result", None)
                if result is not None:
                    return result
                else:
                    logger.error(f"No result in MCP response: {data}")
                    return f"(No result from MCP server)\n{debug_info}"
            except Exception as json_err:
                logger.error(f"MCP server JSON decode error: {json_err}\n{debug_info}")
                return f"(MCP server JSON decode error: {json_err})\n{debug_info}"
        else:
            logger.error(f"MCP server error: {response.status_code}\n{debug_info}")
            return f"(MCP server error: {response.status_code})\n{debug_info}"
    except Exception as e:
        logger.exception(f"MCP server exception: {e}")
        return f"(MCP server error: {e})"


def call_openai_llm(messages):
    try:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=messages,
            max_tokens=256,
            temperature=1.0,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"(OpenAI error: {e})"

if submitted and user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    # Optionally, call MCP server for company-specific info
    mcp_result = call_mcp_server(user_input)
    # Add MCP result to context for LLM
    context_messages = st.session_state["messages"] + [
        {"role": "system", "content": f"Company info: {mcp_result}"}
    ]
    bot_reply = call_openai_llm(context_messages)
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
    st.rerun()

st.markdown("---")
st.markdown("_Powered by OpenAI GPT-4o mini and MCP server integration._")
