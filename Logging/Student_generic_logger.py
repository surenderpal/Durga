from generic_logger import get_custom_logger
import logging
def logtest():
    logger=get_custom_logger(logging.DEBUG)
    logger.critical('Critical message from student module')
    logger.error('error message from student module')
    logger.warning('warning message from student module')
    logger.info('info message from student module')
    logger.debug('debug message from student module')
logtest()
