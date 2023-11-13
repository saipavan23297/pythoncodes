'''

def div(a, b):

    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b =b,a
        return func(a,b)

    return inner

div1=smart_div(div)

div1(4,2 )



def outer_func(msg):
    
    def inner_func():
        print(msg)
    return inner_func

my_func= outer_func("dsa")
my_func()
'''


def dec_func(originalfunction):
    def wrapper_func(*args, **kwargs):
        return originalfunction(*args, **kwargs)
    return wrapper_func    

@dec_func
def display():
    print("display function ran")

@dec_func
def display_info(name, age):
    print("display_info function ran with argument ({},{})".format(name,age))


display_info("Sai", 30)

display()

#decorated_func = dec_func(display)

#decorated_func() 




  





