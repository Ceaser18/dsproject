import logging 
import os 
from datetime import datetime 

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

os.makedirs(logs_path,exist_ok=True) #keep on appending the logs to the same file

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] [%(levelname)s] [%(filename)s] [%(funcName)s] [%(lineno)d] [%(message)s]",
    level=logging.INFO

)

if __name__=="__main__":
    logging.info("This is an info message")
    logging.error("This is an error message")
    logging.warning("This is a warning message")
    logging.critical("This is a critical message")
    logging.debug("This is a debug message")

