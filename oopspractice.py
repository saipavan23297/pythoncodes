'''
class example:
    def __init__(self, name):
        self.name= name
    def greet(self):
        print("my name is", self.name)

myobj = example("saipavan")
myobj.greet()

'''
'''
#// inheritance
class person():
    def __init__(self, name, age):
        self.name = name
        self.age= age
        print("hi")
    def show_details(self):
        print("name is {} and age is {}".format(self.name, self.age))

class employee(person):
    def __init__(self,name, age, salary ):
        self.salary = salary
        person.__init__(self,name, age)
    def show_details1(self):
        print(f"{self.name} his salary is {self.salary} and his age is {self.age}") 
obj = employee("saipavan",21, 20200)
obj.show_details1()                       
obj.show_details()
'''
#exception handling practice
'''
x= 5
y="saipavan"
try:
 z=x+y
except:
 print("error")
'''
'''
def divide(x,y):
    try:

     result=x//y
     print(result)
    except Exception as e:
       print("exeception occurs:",e)

divide(2,0)     

'''

'''
a=[1,2,3,4,5]

def func1(x):
    y=2*x
    return y
b = map(func1, a)
print(list(b))
'''
'''
t=(1,23,4,5,6)
s=("dsa","Safas","fffa","sdfsd","sdaf")
z=zip(t,s)
for i in z:
    print(i)
#print(list(z))
'''
