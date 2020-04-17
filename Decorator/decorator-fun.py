def decor(func):
    def inner():
        print('send the person to the beauty parlor')
        print('showing a person with full of decoration')
    return inner # this is returned by the outer function
@decor
def dispaly():
    print('shwoing a person as it is')
dispaly()
