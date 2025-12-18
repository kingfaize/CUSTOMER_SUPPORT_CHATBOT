# Customer Support Chatbot Prototype

This project is a prototype for a customer support chatbot for a company selling computer products (monitors, printers, etc). The chatbot integrates with an MCP server using Streamable HTTP to access company features and is designed for demo deployment on platforms like HuggingFace Spaces.

## Features
- Simple chatbot UI for customer support
- Integration with MCP server: https://vipfapwm3x.us-east-1.awsapprunner.com/mcp
- Uses a cost-effective LLM (flash or mini level)
- Demo deployment (HuggingFace Spaces or similar)

## Requirements
- Python 3.8+
- Streamlit (for UI)
- Requests (for HTTP communication)
- Any additional libraries for LLM integration (e.g., HuggingFace Transformers, if using a hosted LLM API)

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app locally:
   ```bash
   streamlit run app.py
   ```
3. Deploy to HuggingFace Spaces or another demo cloud platform as desired.

## Documentation
See the documentation file for details on architecture, usage, and deployment.
