with open('char.txt','r') as f:
    print(f.tell()) #0
    print(f.read(2)) #Du
    print(f.tell()) #2
    print(f.read(3)) #rga
    print(f.tell()) #5
    print(f.read(3)) #so
    print(f.tell()) #8
    print(f.seek(3)) #3   # It will take pointer to the start
    print(f.tell()) #3
    print(f.read(3)) #ga
