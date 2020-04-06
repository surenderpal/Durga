import logging
import student1
logger=logging.getLogger('Test1logger')
logger.setLevel(logging.DEBUG)
fileHandler=logging.FileHandler('test1.log',mode='a')
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',datefmt='%d/%m/%Y %H:%M:%S')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.critical('critical message form test1 module')
logger.error('error message form test1 module')
logger.warning('warning message form test1 module')
logger.info('info message form test1 module')
logger.debug('debug message form test1 module')
