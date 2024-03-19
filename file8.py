# 19-03-24

# eg :3
'''
def profile(name,age,place):
    txt="my name is {}.Iam {} years old.Iam from{}."
    print(txt.format(name,age,place))
profile("uday",20,"ATP")
'''



# eg :

# function with return statement .
'''
def f1():
    z=8
f1()
print(z)   #  error ---> cannot use outside the function.
'''


def f1(a,b):
    c=a*b
    return
f1(6,8)
# return
#1) A variable declared inside the function using return
#2) return does not print anything
#3) we cannot write any code below return statement.


'''
def f1 (a,b):
    c = a*b
    return c
#print(f1(6,8))
obj = f1(6,8)
obj = f1(4,6)


'''


#def gracemark(object):
#    print(object+4)
#gracemark(obj)
#gracemark(obj1)

#123

# probelem: 1
'''
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n,"palindrome")
    else:
        print("Not palindrome")
'''    
#a = int(input("Enter the value:"))
#palindrome(a)



# Based on the declaration of parameter and args
# functions are divided into 5 catagories

'''
*positional args
*keyword args
*defaultargs
*variable length args
*keyword variable length args 
'''

#* positional args.
#The position of parameters have to be same as position as arguments
# eg : 1
'''
def profile(name,phone,mark):
    txt = "my name is {}.my phone number is {}. I got {} marks.
    print(txt.format(name,phone,mark))
profile(146464115,"krish",87)   -----> # unexpected output

'''


# keyword args .

# Eg :
'''
*To overcome the diadvantage of position args,we use keyword args
*It is the process of intialising the parameter with the args while calling the
*function
'''
##
'''
def profile(name,phone,mark):
    txt = "my name is {}.my phone number is {}. I got {} marks."
    print(txt.format(name,phone,mark))
profile(name="krish",mark=45,phone=23367838)
'''


# to do---> exception of keyword args function
'''
def profile(name,phone,mark):
    txt="My name is {}.My phone number is {}.I got {}marks."
    print(txt.format(name,phone,mark)
'''
#profile("sid",mark=98,phone=2567524)  #  error---> positional args follow keyword args
#profile(45668575,name="krish",mark=78)# error ---> name has mulitiple values
#profile(" sid",mark=78,phone=88578748)


# ** Deafault args .
'''
The method of assigning the argument to
'''
# Eg : 1
'''
def profile(name,phone,place="kadapa"):
    txt="My name is {}.My phone number is {}.I got {}marks."
    print(txt.format(name,phone,mark)

profile("krish",26759763957)
        ###  eg : 2
'''
'''
def profile(name,phone,place="kadapa"):
    if place == "kadapa" or place=="kadapa" or place =="kadapa"
       txt =" my name is {}. my phone number is {}. i am from {}."
       print(txt.format(name,phone,place))
    elif:
        print("you are not eliogible to signup")
rofile("krish",723635567)
'''
##exception
'''
def profile(name,place="kadapa,phone"):
    if place == "kadapa" or place=="kadapa" or place =="kadapa"
       txt =" my name is {}. my phone number is {}. i am from {}."
       print(txt.format(name,phone,place))
    elif:
        print("you are not eliogible to signup")
rofile("krish",723635567)
'''



# * variable length params

# Eg : 1
'''
*To pass more then 1 arg to a parameter meanse we use variable length args
*To convert normal parameter to variable length param,add  * to their prifix of param
'''         
'''
def profile(*name):
    for val in name:
        print("my name is",val)
profile("krish",'name2','name3')
'''

#  Eg : 2
'''
def profile(*name,age):
    for val in name:
        print("my name is",val,"may age is",age)
profile("krish",'name2','name3',45)# age has no args 
'''
'''
def profile(age,*name):
    for val in name:
        print("my name is",val,"may age is",age)
profile(28,"krish",'name2','name3')
'''
# Keyword variable length args
'''
kwargs ---> Which is used to provide the args in the form of key value pair.
'''
# Eg : 1
'''
def price(price_list):
    print(price_list)
print(shirt=1000,iphone=80000)
'''
#n=5
#{1:1,2:4,3:9,4:16,5:25}
'''
n = int(input("enter the number"))
d1={}
for val in range(1,n+1):
    d1[val]=val**2
print(d1)
'''
####
'''
def dict1(n):
    d1 = {}
    for val in range(1,n+1):
        d1[val] = val**2
    print(d1)
dict1(5)
'''

### -----> Object oriented programming.
'''
 The panadigms of objects oriented programming are

'''
#class
#objects
#inheritance
#polymorphism
#abstraction
#encapsulation
'''
 class is a blue print of an object 
'''
#l1 = [1,2,3,4,5,6]


    # Eg : 1
'''    
class c1:
    name1 = "krish"
    
    print(name1)

'''
##-----> Eg : 2
'''
class c1:
    name ="krish"
c = person()   # c os object
the process of creation of an object is called as instantiation


print(C.name)
'''

##---> Eg : 3
'''
creation of a method
'''
#when the function is created with a class is called as method
# method with out parameter 
'''
class person:
    def display(person):  # It is a method
        print("Hello welcome to classes")

p = person()
p.display()
'''
##------> Eg : 4

# method with parameter
'''
class person:
    def display(person,name,age):
        print(name,age)
        
p = person()
p.display("krish",20)

'''
## ---> Eg :5
'''
fname= "krishj"# attribute or static variablie
lname = "t"
def first_name(self):
    print(self.fname)
def full_name(self)
    print(self.fname+""+self.lname)

    
p = person1()
p.first_name()
p.full_name()

'''


## ---> Eg: 6
# constructor--->_init_()
#This is a special method which has the ability to execute iotself with out calling it manually
#through the process of instansiation
'''
class profile:
    def_init_(self):# construcotor method 
        print("hey")

p = profile()# execution of constructor through this process 
'''





















