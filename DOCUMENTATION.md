# Customer Support Chatbot Documentation

## Overview
This prototype demonstrates a customer support chatbot for a company selling computer products. It connects to an MCP server using Streamable HTTP and provides a simple UI for customer interaction. The system is designed for easy demo deployment.

## Architecture
- **Frontend/UI:** Streamlit web app for chat interface.
- **Backend/Logic:** Python code to handle user input, interact with the MCP server, and call a cheap LLM (flash/mini level) for generating responses.
- **MCP Server:** External service at https://vipfapwm3x.us-east-1.awsapprunner.com/mcp for company-specific features.

## Key Components
- `app.py`: Main application file (to be created).
- `requirements.txt`: Python dependencies.
- `README.md`: Project overview and setup instructions.

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `streamlit run app.py`
3. Interact with the chatbot via the web UI.

## Deployment
- Recommended: HuggingFace Spaces (free/cheap demo hosting for Streamlit apps)
- Alternative: Vercel, GCP, AWS, Azure (for more advanced deployment)

## Notes
- Use a cost-effective LLM (e.g., HuggingFace Inference API with a mini/flash model, or OpenAI's cheapest tier).
- The MCP server URL is provided via the `MCP_SERVER_URL` environment variable or hardcoded for the prototype.
- This is a prototype; production deployments should consider authentication, security, and scalability.
