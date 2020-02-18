import logging
logging.basicConfig(filename='mylog17022020.log',
                    level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%A %B %d/%m/%Y %H:%M:%S ')
logging.info('A new request come')
try:
    x=int(input('Enter first Number: '))
    y=int(input('Enter second Number: '))
    print('The result is:',x/y)
except ZeroDivisionError as msg:
    print("Can't divide with zero")
    logging.exception(msg)
except ValueError as msg:
    print("Provide int values only")
    logging.exception(msg)

logging.info('A request processing completed')
# logging.critical('This is critical message')
# logging.error('This is error message')
# logging.warning('This is warning message')
# logging.info('This is info message')
# logging.debug('This is debug message')


