f1=open('molio.png','rb')
data=f1.read()
print(type(data)) #bytes
f2=open('udemy.png','wb')
f2.write(data)
f1.close()
f2.close()
