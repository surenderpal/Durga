def decor_for_wish(func):
    def inner(name):
        names=['CM','PM','MINISTER','surender','upika']
        if name.lower() in names:
            print('*'*50)
            print('Hello {} you are very important Asset to India, \nThanks for coming here, \nWe are honored.'.format(name))
            print('@'*50)
        else:
            func(name) 
    return inner  
# @decor_for_wish
def wish(name):
    print('Good Morning',name,'!!!')
decorated_wish=decor_for_wish(wish)
wish('rahul')
wish('surender')
# wish('ravi')
# wish('roopa')
decorated_wish('upika')
