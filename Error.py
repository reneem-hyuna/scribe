import logging
import functools
import traceback

def create_logger():
    """
    Creates a logging object and returns it
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
 
    return logger

def exception(function):
    def wrapper(*args, **kwargs):
        logger = create_logger()
        try:
            return function(*args, **kwargs)
        except RequiredFieldMissing:
            # log the exception
            err = "Error: There was an exception in  "
            err += function.__name__
            logger.error(err)
            print(err)
        except Exception as e:
            logger.error(str(e) + "There was an error in " + function.__name__)
            traceback.print_exc()
    return wrapper

class Error(Exception):
    pass

class FieldIsMissing(Error):
    pass

class FieldIsNotInPayload(Error):
    pass

class RequiredFieldMissing(Error):
    pass