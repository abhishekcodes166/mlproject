import logging
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
LOG_PATH = os.path.join(os.getcwd(), LOG_DIR, LOG_FILE)
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_PATH,LOG_FILE)
logging.basicConfig(
    filename=LOG_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logger has been set up.")