import os
from datetime import *
stat=os.stat('cwd')
for statistics in stat:
    print(statistics)
print(stat)
# print('size of the file:',stat.st_size)
# print('last modification time:',datetime.fromtimestamp(stat.st_mtime))
# (
#     st_mode=16877, 
#     st_ino=15963277, 
#     st_dev=16777220, 
#     st_nlink=3, 
#     st_uid=502, 
#     st_gid=20, 
#     st_size=96, 
#     st_atime=1586712458, 
#     st_mtime=1586712448, 
#     st_ctime=1586712448
# )


