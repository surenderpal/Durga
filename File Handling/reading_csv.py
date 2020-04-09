import csv
with open('emp.csv','r') as f:
    r=csv.reader(f)
    data=list(r)
    # print(data)
    for row in data:  
        # print(row)
        for column in row:
            print(column,'\t',end='')
        print()

