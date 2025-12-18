import logging
import os

LOG_FILE = os.getenv("LOG_FILE", "chatbot.log")

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def get_logger(name: str = "chatbot"):
    return logging.getLogger(name)
