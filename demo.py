from Hate.logger import logging
from Hate.exception import CustomException
import sys
#logging.info("welcome to the hate_speech_classification Project")
try:
    a=90/"0"
except Exception as e:
    raise CustomException(e,sys) from e