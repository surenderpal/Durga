from threading import *
print('Current Thread:',current_thread().getName())
current_thread().setName('Surender')
print('Current Thread:',current_thread().name)
