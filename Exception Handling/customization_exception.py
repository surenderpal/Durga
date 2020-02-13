class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg=msg
class TooOldException(Exception):
    def __init__(self,msg):
        self.msg=msg
age=float(input('Enter your age:'))
if age>60:
    raise TooYoungException('Please wait some more time, definitly you will get best match.')
elif age<18:
    raise TooOldException('Your age is alread crossed marriage date, No chance of getting married.')
else:
    print('Your request is saved, you will get notification via mail')
