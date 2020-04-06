import logging
logger=logging.getLogger('Customlogger')
logger.setLevel(logging.DEBUG)
fileHandler=logging.FileHandler('cust_test.log',mode='w')
fileHandler.setLevel(logging.ERROR)
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                             datefmt='%d/%m/%Y %H:%M:%S'
                            )
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.critical('Is is critical message')
logger.error('Is is error message')
logger.warning('Is is warning message')
logger.info('Is is info message')
logger.debug('Is is debug message')
