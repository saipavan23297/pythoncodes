import numpy as np
import array
import pylab as pl
'''
a=np.array([[1,2,3,4],[4,2,4,4]])
print(type(a))
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)
'''
'''
a = np.array([[1,2,4],[5,8,7]], dtype= "float")
print(a)
b = np.array((1,3,2))
print(b)
c=np.zeros((3,4))
print(c)
d=np.full((3,6),6,dtype='complex')
print(d)
print(np.random.random((2,2)))
e=np.arange(0,30,5)
print(e)
f=np.linspace(0,5,10)
print(f)
arr = np.array([[1, 2, 3, 4], 
                [5, 2, 4, 2], 
                [1, 2, 0, 1]]) 
newarr= arr.reshape(2,2,3)
print(arr)
print(newarr)
arr1= np.array([[1,23,4],[23,24,32]])
print(arr1)
newarr1 = arr1.flatten()
print(newarr1)
'''
'''
arr3 = np.array([[-1, 2, 0, 4], 
                [4, -0.5, 6, 0], 
                [2.6, 0, 7, 8], 
                [3, -7, 4, 2.0]])
print(arr3)
temp = arr3[:2, ::2]
print(temp)
temp = arr3[[0,1,2,3],[3,2,1,0]]
print(temp)
print(arr3[arr3>0])
'''

'''
a = np.array([[1, 2],
              [3, 4]])
 

b = np.array([[4, 3],
              [2, 1]])

print(a+1)
print(b-2)
print(a.sum())
print(a+b)

'''
'''
a=  [1,2,3,4,5]
n= np.array(a)
print(n)
for i in n:
    print(i)
'''
'''
arr=array.array('i',[1,2,3])
print(arr)
for i in range(0,3):
    print(arr[i])

a=np.empty(2, dtype=int)
print(a)
b= np.empty([2,2], dtype=int)
print(b)
c=np.zeros([2,2])
print(c)
'''

'''
a=np.arange(8)
print(a)
b= np.arange(8).reshape(2,4)
print(b)
c= np.arange(8).reshape(2,2,2)
print(c)
d=np.arange(3,10,3)
print(d)
e=np.linspace(2,3,num=4).reshape(2,2)
print(e)
f=np.linspace(2,3,num=4)
print(f)
g= np.array([[1,2],[3,4]])

print(g.flatten())

a=np.zeros(4, dtype=int)
print(a)
b= np.ones(3)
print(b)
c=np.ones([3,3])
print(c)
'''
'''
a= np.eye(4,4)
b= np.eye(2, dtype=int)
c= np.eye(4,5, k=-1)
print(a)
print(b)
print(c)

a="saipavan"
b= np.fromiter(a, dtype='U2')
print(b)


c = np.empty((3,4))
print(c)
d= np.full((3,4),5)
print(d)
'''
'''
a= np.array([2,3,4,45,5,6])
b=a
c=a.view() 
d=a.copy()
print(id(a))
print(id(b))
print(id(c))
print(id(d))
b[0]=12
print(a)
print(b)
print(c)
print(d)

'''





