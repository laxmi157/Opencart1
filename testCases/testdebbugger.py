import os
import logging



# Ensure the 'logs' directory exists
os.makedirs("logs", exist_ok=True)

# Full file path for logging
log_file_path = os.path.join(os.getcwd(), "logs", "test_v1.log")

# Configure logging to a file
logging.basicConfig(
    filename=log_file_path,  # Ensure the file path is correct
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
 
logger = logging.getLogger(__name__)

def test_logging_to_file():
 
    logger.info("Log to file example.")
    logger.warning("This warning is logged to a file.")

