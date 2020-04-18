def decor_for_wish(func):
    def inner(name):
        if name=='surender':
            print('#'*50)
            print('Hello Surender, you are the best and Most valuable asset to India.')
            print('Very Very Good Moring, the Richest man on earth...')
            print('#'*50)
        else:
            func(name)
    return inner
@decor_for_wish
def wish(name):
    print('Good Morning',name,'!!!')

wish('rahul')
wish('roopa')
wish('surender')
wish('upika')
