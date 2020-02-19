import inspect
def getInfo():
    # print(inspect.stack())
    print(inspect.stack()[1])     
    print('caller Moudle',inspect.stack()[1][1])
    print('caller function name:',inspect.stack()[1][3])
