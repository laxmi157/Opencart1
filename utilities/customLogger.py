import logging
import os

class LogGen():
    @staticmethod
    def loggen():
               
        # Configure logging
        logging.basicConfig(
        filename="test_logs.log",  # Log file name
        filemode="a",  # Open in append mode
        level=logging.INFO,  # Set the logging level
        format="%(asctime)s - %(levelname)s - %(message)s",  # Include date and time
        datefmt="%Y-%m-%d %H:%M:%S" , # Date and time format
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
      
        
   
 


# # Ensure the 'logs' directory exists
# os.makedirs("logs", exist_ok=True)

# # Full file path for logging
# log_file_path = os.path.join(os.getcwd(), "logs", "test.log")

# # Configure logging to a file
# logging.basicConfig(
#     filename=log_file_path,  # Ensure the file path is correct
#     level=logging.DEBUG,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )
