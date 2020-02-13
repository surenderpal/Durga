# # if no exception 
# try:
#     print('try')
# except:
#     print('except')
# finally:
#     print('Finally')

# # if exception raised and handled
# try:
#     print('try')
#     print(10/0)
# except ZeroDivisionError:
#     print('except')
# finally:
#     print('finally')

# if exception raised but not handled
try:
    print('Try')
    print(10/0)
except ValueError:
    print('Except')
finally:
    print('finally')
