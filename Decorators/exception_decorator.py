import logging


def create_logger():

    logger = logging.getLogger('Exception Decorator')
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler('exceptions.log')
    format = '%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s'
    formatter = logging.Formatter(format)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger


def log_exception(fun):
    def wrapper(*args, **kwargs):
        logger = create_logger()
        try:
            return fun(*args, **kwargs)
        except:
            error = 'There was an exception in {}'.format(fun.__name__)
            logger.exception(error)
            # Re-raise the exception
            raise
    return wrapper