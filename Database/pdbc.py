standard steps to communicate with database
1. Import that database specific module
    import cx_Oracle
    import pymysql
2. Establish Connection betwenn python program and db
con=cx_Oracle.connect(database information);
eg:
    con=cx_Oracle('scott/tiger@locathost')
3. Cursor object
    cursor=con.cursor()
4. execute our sql query
    cursor.execute(sqlquerry)---> a single query
    cursor.executescript(sqlquerries)---> To execute a string of sql queries separated by ;
    cursor.executemany()---> To execute a parametrized query
5. Fetch the results
    cursor.fetchone()---> To fetch only one row
    cursor.fetchall()---> To fetch all rows
    cursor.fetchmany(n)---> To fetch n rows
6. commit() 
    By default auto commit is not enabled in python, to view the changes we have to commit it explicity
    rollback()
7. cursor.close()
   con.close() 
          
