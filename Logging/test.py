import logging
# import student
logging.basicConfig(filename='test.log',level=logging.WARNING)
import student
logging.critical('critical message by test module')
logging.error('error message by test module')
logging.warning('warning message by test module')
logging.info('info message by test module')
logging.debug('debug message by test module')

