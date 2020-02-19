import logging
from generic_logger import get_custom_logger
def generic_log():
    logger=get_custom_logger(logging.DEBUG)
    logger.critical('Critical message from generic logger 2 module')
    logger.error('error message from generic logger 2 module')
    logger.warning('warning message from generic logger 2 module')
    logger.info('info message from generic logger 2 module')
    logger.debug('debug message from generic logger 2 module')
generic_log()
