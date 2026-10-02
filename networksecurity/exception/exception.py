import sys 
from networksecurity.logging import logger 
class NetworkSecurityException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        self.error_message = error_message
        _,_, exc_tb = error_detail.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "error occurred in script: [{0}] at line number: [{1}] error message: [{2}]".format( 
        self.file_name, self.lineno, self.error_message
        )


if __name__ == "__main__":
    try:
        logger.logging.info("enter the try block ")
        a = 1/0
    except Exception as e:
        raise NetworkSecurityException(e, sys)

    