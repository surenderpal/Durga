# create logger object and set level:
import logging
logger = logging.getLogger('Customlogger') #createing logger object
logger.setLevel(logging.DEBUG)
# create handler object and set level:
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.WARNING )
#               or 
# fileHandler=logging.FileHandler('abc.log',mode='w')
# fileHandler.setLevel(logging.ERROR)
# create Formatter object
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                               datefmt='%d/%m/%Y %I:%M:%S  %p'
                            )
# set formatter to handler
consoleHandler.setFormatter(formatter)
#add handler to logger:
logger.addHandler(consoleHandler)
# write log messages by logger object
logger.critical('critical message by customize logger')
logger.error('error message by customize logger')
logger.warning('warning message by customize logger')
logger.info('info message by customize logger')
logger.debug('debug message by customize logger')

  
