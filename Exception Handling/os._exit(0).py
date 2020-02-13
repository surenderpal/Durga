import os
try:
    print('try')
    os._exit(0)
except ValueError:
    print('ValueError')
finally:
    print('Finally')
