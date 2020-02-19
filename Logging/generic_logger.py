import logging
import inspect
def get_custom_logger(level):
    function_name=inspect.stack()[1][3]
    logger_name=function_name +"logger"
    print(function_name)

    logger=logging.getLogger(logger_name)
    logger.setLevel(level)

    fileHandler=logging.FileHandler('abc.log',mode='a')
    fileHandler.setLevel(level)

    formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p')

    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    return logger

