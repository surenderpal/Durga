l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2
l3=[*l1,*l2]
print('list merging',l3)
t1=(1,2,3)
t2=(4,5,6)
t3=(*t1,*t2)
print('tuple merging',t3)
s1={1,2,3,4}
s2={5,6,7,8} 
s3={*s1,*s2}
print('set merging',s3)
d1={'a':1,'b':2}
d2={'c':3,'d':4}
d3={**d1,**d2}   #dictionary merging
print('dict merging',d3)

