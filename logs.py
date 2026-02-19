import logging
import os

# Create logs folder if it does not exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
