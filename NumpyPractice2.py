import numpy as np 

'''
a= np.array([12,3,3,4,534,5,43,43,5,3])
print(a)

b=np.empty_like(a)
b[:]=a
c=a.copy()

print(c)
print(b)
'''
'''
a=np.array([12,4,34,5,345])
print(a)
a=np.append(a,[1,2,4,55])
print(a)

b=np.arange(1,13).reshape(2,6)
print(b)
c=np.arange(5,11).reshape(1,6)
print(c)
#b=np.append(b,c, axis=0)
print(b)
d=np.array([1,2]).reshape(2,1)
print(d)

f=np.append(b,d,axis=1)
print(f)

'''

'''
a= np.array([12,23,3,4])
b=np.array([1,2,3,8])
c=np.hstack((a,b))
d=np.vstack((a,b))
e=np.concatenate((a,b),axis=0)
f=np.stack((a,b),axis=1)
print(c)
print(d)
print(e)
print(f)
'''

a=np.array([1,2,3,5,6])

#filt =[True, False, True, True, False]
filt=[]
for i in a:
    if i>3:
        filt.append(True)
    else:
        filt.append(False)    
b= a[filt]
print(b)

