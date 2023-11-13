'''
def my_gen():
    yield 1 
    yield 2
    yield 3
    yield 4
x= my_gen()  // genertaor object 
print(next(x))
print(next(x))
print(next(x))
print(next(x)) 
'''
'''
def my_gen():
    yield 1
    yield 2 
    yield 3
for i in my_gen():
    print(i) 
'''
'''
number = [1,2,346,236,63]
#x=[i for i in number]
lamobj = map(lambda i : print(i), number)  #map returns the map objcet which can be passed to list or sort ot create list or list 
print(list(lamobj))
'''
'''
def outerfunction():
    x=10
    def innerfunction():
        print(x)
    return innerfunction
myfunction = outerfunction()
myfunction() 
'''
'''
def greet(text):
    return text.lower()
print(greet('HELLO'))
hep = greet 
print(hep("HELLO"))
'''
'''
#passig funciton as argument

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def operation(operation, x, y):
    return operation(x,y)

res1= operation(add, 2,3)
res2 = operation(sub, 2, 3)
print(res1)
print(res2)
 '''
'''
def body(*args):
    print(f"he is {args[0]} and he is very powerfull human in the {args[1]}")
body("saipavan", "world")    
 '''
'''
def outer(txt):
    message= txt
    def inner():
        print(message)
    return inner
func = outer("saipavan")
func()
'''
'''
def decorator_function(func):
    def wrapper_function(*args, **kwargs):
       print('{}'.format(func.__name__))
       return func(*args, **kwargs )
    return wrapper_function
@decorator_function
def display():
    print("this is display function")
#my_function = decorator_function(display) \\ same as @decorator_function
#my_function() 

@decorator_function
def display1(name, age):
    print("my name is {} and age is {}".format(name, age))    
display()
display1("saipavan", 22)
#my_function = decorator_function(display)   
#my_function()
'''
'''
def myfunc(func):
    def innerfunc():
        x=5
        print(x+x)
        return func()       
    return innerfunc

def outerfunc():
    return 90
z=myfunc(outerfunc)
print(z())
'''
'''
import copy
l=[1,2,33,4,[2432,436,436453]]
#z=l
z=copy.deepcopy(l)
l.append([23,4325,32])
z[2]=234
l[4][0]=90 
print(l)
print(z)
'''
'''
#json object to python object 
import json
employee = '{"id":"09", "name":"saipavan", "age":22}'
print(type(employee))
print(employee)
dict1 = json.loads(employee)
print(dict1, type(dict1))
'''
'''
#python object to JSON object
import json 
dict = {"id":"09", "name":"saipavan", "age":22}
print(type(dict), dict)
dict1 = json.dumps(dict, indent=4)
print(type(dict1), dict1)
'''







