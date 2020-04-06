import logging
logging.basicConfig(filename='abc.log',level=logging.DEBUG,filemode='w')
logging.basicConfig(filename='xyz.log',level=logging.DEBUG,filemode='w')
logging.critical('It is critical message')
logging.error('It is error message')
logging.warning('It is warning message')
logging.info('It is Info message')
logging.debug('It is debug message')
 lo
