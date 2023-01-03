def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)
 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
# First argument : Hello
# Next argument through *argv : Welcome
# Next argument through *argv : to
# Next argument through *argv : GeeksforGeeks
  
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
myFun(first='Geeks', mid='for', last='Geeks')
# first == Geeks
# mid == for
# last == Geeks

def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
 
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
# args: ('geeks', 'for', 'geeks')
# kwargs: {'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}

class car():
    def __init__(self,*args): # args receives unlimited no. of arguments as an array
        self.speed = args[0] 
        self.color = args[1]
                 
#creating objects of car class (args)        
audi=car(200,'red')
bmw=car(250,'black')
mb=car(190,'white')
    
print(audi.color)
print(bmw.speed)
# red
# 250

class car():
    def __init__(self,**kwargs): # kwargs receives unlimited no. of arguments as an array
        self.speed = kwargs['s'] 
        self.color = kwargs['c']
                 
#creating objects of car class (kwargs)
audi=car(s=200,c='red')
bmw=car(s=250,c='black')
mb=car(s=190,c='white')
    
print(audi.color)
print(bmw.speed)
# red
# 250
