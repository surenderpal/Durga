import logging
logger=logging.getLogger('StudentLogger')
logger.setLevel(logging.DEBUG)
fileHandler=logging.FileHandler('student1.log',mode='w')
fileHandler.setLevel(logging.ERROR)
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s%(message)s')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.critical('critical message from student1 module')
logger.error('error message from student1 module')
logger.warning('warning message from student1 module')
logger.info('info message from student1 module')
logger.debug('debug message from student1 module')

