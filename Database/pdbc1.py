import cx_Oracle
con=cx_Oracle.connect('scott/tiger@localhost')
if con!= None:
    print('Connect established successfully')
    print('Database version:',con.version)
else:
    print('connection not established')
con.close()
