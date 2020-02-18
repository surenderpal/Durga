import logging
# logging.basicConfig(filename='log123.txt',level=logging.WARNING)
# logging.basicConfig(format='%(levelname)s')
# logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s')
logging.basicConfig(format='%(levelname)s:%(name)s')
logging.critical('This is critical')
logging.error('This is error')
logging.warning('This is warning')
logging.info('This is info')
logging.debug('This is debug')
print('Logging Demo')