#NEW Beginning
""""
multi
line
comment
"""
print("HEY PRAKHAR", end=" ")
print("lets begin the new journey")

print("HEY PRAKHAR" ,"lets begin the new journey")
#(,) is used as space in output

print("HEY \nPRAKHAR")
"\n is used to create a new line known as escape sequence character"

"VARIABLES" #STRING , INTEGER , FLOAT
var1="HELLO WORLD"
var2=4
var3=32.3
var4="8"
var5="9"
print(type(var1))
print(type(var2))
print(type(var3))
print(var2 + var3)
print(var1 + var4)
#it concatinate (joined)

print(var4 + var5)
"WE EXPECTED THAT IT WILL GIVE OUTPUT AS 17 BUT IT DIDNT BECAUSE strings cannont be added"
#double inverted commas implies strings

"can we change this string to integer?"
#yes , with the method known as typecasting
print(int(var5) + int(var4))
#similarly we can convert among the following variables called typecasting

print(5*"prakhar\n")

"USER INPUT"
print("enter your number")
inpnum=input()
print("YOU ENTERED" ,int(inpnum)+10)

"lets try to make simple calculator which add numbers through through user input"
"""
print("ENTER FIRST NUMBER")
n1=input()
print("ENTER SECOND NUMBER")
n2=input()
print("RESULT" ,int(n1) + int(n2))

"SUBTACTING CALCULATOR #practise"
print("ENTER FIRST NO.")
n1=input()
print("ENTER SECOND NO.")
n2=input()
print("and the result is" , int(n1) - int(n2))
"""
"LETS SEE OUT SOME MORE EXAMPLES ON USER TYPE"

print("HOW MANY CHOCOLATES YOU WANT?")
n=input()
if n>"7":
    print("OUT OF STOCK")
else:
    print("yes in stock")

"exploring STRING datatype"

mystr="I M TECH ENTHUSIAST"
print(mystr)
print(mystr[0:4]) #this is called indexing , basically it defines the range of printing
print(len(mystr)) #remember indexing starts with 0
print(mystr[0:8:2]) #2 is the gap i.e., we will get output first character , third char. , fifth......
print(mystr[0:])
print(mystr[:7]) #if we left the preceeding value , bydefault it will se it to 0
print(mystr[0:-5]) #negative index

print(mystr[2:-5]) #negative index
print(mystr[2:14]) #negative index

print(mystr[-5:-2]) #negative index
print(mystr[14:17]) #negative index

"FUNCTIONS OF STRINGS"
print(mystr.endswith("ENTHUSIAST")) #remember python is case sensitive
print(mystr.count("I")) #count simply means how many the particular argument is there
print(mystr.find("TECH")) #find where the arguement is
print(mystr.lower()) #converts text to lower case

print("hello world")

"LISTS : A NEW DATATYPE"

gadgets = ["CAMERA", "PC", "MOBILE"]
print(gadgets)
numbers=[12,34,77,33]
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.append(6)
print(numbers)
print(numbers[2])
numbers.insert(1,9)
print(numbers)
#indexing is same as indexing in string

"TUPLE" #tuple is immutable i.e., it cannot change while list is mutable i.e., it can be changed
tp=(1,3,4,5)
print(tp)

"DICTIONARY"
mydict={"PRAKHAR":"BURGER","PRABAL":"PIZZA","ANKIT":"PAOBHAJI","AMAN":"CHOWMEIN"}
print(mydict)
print(mydict["PRAKHAR"])
mydict1={"PRAKHAR":"BURGER","PRABAL":"PIZZA","ANKIT":"PAOBHAJI","AMAN":"CHOWMEIN","NEHA":{"B":"ROTI CHAI", "L":"DAL CHAWAL", "D":"ROTI SABJI"}}
print(mydict1)
print(mydict1["NEHA"])
print(mydict1["NEHA"]["B"])
mydict["ROHAN"]="JUNK FOOD"
print(mydict)
del mydict["ROHAN"]
print(mydict)

d3=mydict.copy()
del d3["AMAN"]
print(mydict)
mydict.update({"PRAKHAR":"MOMOS"})
print(mydict)
print(mydict.keys())
print(mydict.items())

"lets play with dict. through exercise"
#create a dictionary of 4 words in whcich the word is given by user which are in dict. and returns the value of that word #apni dictionary
#print("enter words to know the meaning")
"""
mydict2={"oppurtunity":"chance", "suspicious":"doubtful", "prakhar":"great", "computer":"a machine"}
word=input()
print(mydict2[word])
word=input()
print(mydict2[word])
word=input()
print(mydict2[word])
word=input()
print(mydict2[word])
"""

"SETS"
s1={1,2,3,4,5}
print(s1)
print(type(s1))
s1.add(1)    #will not be added because set is unique , it cannot have same values
print(s1)
print(min(s1))
s1.remove(1)
print(s1)

"IF ELSE & ELIF Statements"
var1="6"
var2="36"
var3=input()
if var3>var2:     #colon is used so that we can enter into if else statement
    print("greater")
elif var3==var2:
    print("equal")
else:
    print("not greater")

list=[1,2,4]
print(5 not in list)
if 5 in list:
    print("5 in list")
else:
    print("not in the list")

"Quiz- Make A Program iF You Are Driving & Traffic Police Ask You About Your Age , take three conditions 18+ , <18 & =18"
print("What iS Your Age")
n1=int(input())
if n1>18:
    print("YOU CAN DRIVE")

elif n1==18:
    print("We Cannot Decide , Come Physically And We Will Test You")

else:
    print("Underage")

"FOR LOOPS"
list1=["Tippiya", "Gullua", "Gunnua"]
print(list1[0] , list1[1] , list1[2]) #this looks very untidy so we use "for" loop to print the values in the more efficient manner , consider if there will be 1000 values and we have to print each one of them seperately , this would take lot of time so to avoid this , we use loop.
for item in list1:
    print(item)
"list in list"
list1=[["Tippiya",6], ["Gullua",4], ["Gunnua",0.5]]
for item,age in list1:
    print(item,"age is",age)

"QUIZ"
list1=["Tippiya", "Gullua", "Gunnua",2,4,7,8,9,45,54]
for items in list1:
    if str(items).isnumeric() and items>6:
        print(items)

"WHILE LOOP"
i=0
while(i<23):
    print(i)
    i=i+1 #this is the way to stop while loop

"BREAK & CONTINUE STATEMENT"
i=0
while(True):
    print(i+1, end=" ")
    if i==44:
        break
    i=i+1

"Quiz"

while(True):
    n3=int(input("PLZZZ ENTER A NUMBER\n"))
    if n3>100:
        print("CONGRATS YOU HAVE PRINTED A NUMBER GREATER THAN 100")
        break
    else:
        continue

"lets make a program to play a game called GUESS the NUMBER"
n5=18
while(True):
    n5 = int(input("Enter A NUMBER"))
    if n5>18:
        print("Greater")
        continue
    elif n5==18:
        print("YOU GUESSED THE NUMBER CORRECTLY")
        break
    else:
        print("Lesser")

"OPERATORS"
#ARITHMETIC OPERATOR
#ASSIGNMENT OPERATOR
#COMPARISON OPERATOR
#LOGICAL OPERATOR
#IDENTITY OPERATOR
#MEMBERSHIP OPERATOR
#BITWISE OPERATOR

#ARITHMETIC OPERATOR
print("5+6 is",5+6)
print("5-6 is",5-6)
print("5*6 is",5*6)
print("5/6 is",5/6)
print("5+6 is",5+6)

#ASSIGNMENT OPERATOR #assigning value to a variable
x=5
print(x)
x+=7
print(x)
x/=7

#COMPARISON OPERATOR
i=5
print(i==8)
print(i==5)
print(i>=5)
print(i<=5)

#LOGICAL OPERATOR
a=True
b=False
print(a or b)
print(a and b)
print(a is not b)

#MEMBERSHIP OPERATOR
lst=[1,3,4,54,6,5]
print(32 in lst)
print(32 not in lst)

#BITWISE OPERATOR #NoNeedToDoiTNow

"SHORT HAND IF-ELSE"
a=int(input("Enter a\n"))
b=int(input("Enter b\n"))
if a>b: print("A IS GREATER THAN B")
elif a==b: print("A IS EQUAL TO B")
else:print("A IS LESS THAN B")

"FUNCTIONS"
a=8
b=2
c=sum((a,b))
print(c)

#USER-DEFINED FUNCTION
#FIRST OF ALL WE HAVE TO DEFINE A FUNCTION USING def KEYWORD

def function():
    print("we are in function")

print(function()) #if we direcly write function(), we will not get none in output

def funct(a,b):
    """This is a function which will calculate average of two numbers , thisfunction does not wor ith three numbers"""
    #beware above statement is not a multiline comment , it is called DOCSTRING , remember string written in first line just after the function is defined , it is called as DOCSTRING
    #docstring is something which tell us what is the motive of the funvtion
    average=(a+b)/2
    print(average)
    return average
v=funct(5,7)
print(v) #if we will not RETURN AVERAGE we will get nothing (NONE) in output
print(funct.__doc__)

"TRY EXCEPT EXCEPTION HANDLING"

print("enter num1")
num1=input()
print("enter num2")
num2=input()
try: #basically try error is used for resolving error in code
    print("the sum of these no. is",int(num1)+int(num2))
except Exception as e:
    print(e)

print("THIS LINE IS VERY IMPORTANT")

# File IO Basiscs
"""
"r" - Open File For Reading
"w" - Open a file fo writing
"x" - creates file if not exists
"a" - add more content to file
"t" - text mode
"b" - binary mode
"+" - read & write
"""
"writing and appending a file in python"
f=open("prakhar.txt","w")
f.write("prakhar is great")
f.close() #look @ left , a file named prakhar.txt is created.
f=open("prakhar.txt","a")
f.write("prakhar is great\n")
f.close()
#handling read and write both
f=open("prakhar.txt","r+") #r+ mode is used to read and write the file
print(f.read())
f.write("thankyou")

"quiz - printing a star pattern on the basis of user input"
list2=[1,3,4,5]
n=input(list2)
print(4 in list2)
print("how many row you want to print")
x1=int(input())
print("type 1 or 0")
x2=int(input())
print("type 1 or 0")
new=bool(x2)
if new==True:
    for i in range(1,x1+1):
        for j in range(1,i+1):
            print("# ", end=" ")
            print()

elif new==False:
    for i in range(x1, 0, -1):
        for j in range(1, i + 1):
            print("# ", end=" ")
            print()


"SCOPE , GLOBAL VAR. & GLOBAL KEYWORD"
l=10 #global variable because it can use any no. of functions in program
def fun(n):
    # l=5 #local
    global l #this is global keyword used for changing the value of global variable
    l=l+45
    print(n,"i have printed")

print(l) #now , which value of l will get printed ? l=5 will get printed because it is acting as a local variable
"""remmeber , global variable act as central government , so if local value like in this case l=5 is not included in function then it will print the value 10"""
""" local variable is first prefence if it is present inside a function """
"if it is inside the function it is called local variable & if it is outside , it is called global variable"

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
print("enter no. to get factorial of")
x=int(input())
result=(fact(x))
print(result)

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*1
    return f
print("enter a number")
x=int(input())
result=(fact(x))
print(result)

"QUIZ- fibonacci seq."
def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fib(8)

"lambda functions also known as anonymous functions"
x=lambda a,b:a+b
print(x(5,6))
y=lambda a,b,c:a*b*c
print(y(2,2,2))
z=lambda a,b,c,d:a+b-c+d
print(z(1,2,3,4))

"WORKING WITH MODULES"
import random
random_number=random.randint(0,50)
print(random_number)
rand=random.random()
print(rand)
lisst=["prakhar" , "prabal" , "bobby"]
choice=random.choice(lisst)
print(choice)

import time #used to know how much time does these loops take to execute the prog.
initial=time.time()

k=0
while(k<105):
    print("i am prakhar")
    k+=1
print("while loop ran in" , time.time()-initial, "seconds")

initial2=time.time()
for i in range(105):
    print("i am prakhar")
print("for loop ran in" , time.time()-initial, "seconds")

localtime=time.asctime(time.localtime(time.time()))
print(localtime)

"OBJECT ORIENTED PROGRAMMING"
class student:
    pass
prakhar=student()
prabal=student() #they both seems to be same but they are not exactly same, because their address will be different
prakhar.name="PRAKHAR"
prakhar.passion="PROGRAMING"
prakhar.age="18"
print(prakhar.name)
print(prakhar.age)

prabal.name="PRABAL"
prabal.age="15"

"INSTANCE AND CLASS VARIABLE"
class Employee():
    no_of_leaves=12 #be careful this time , this is class variable , any of the object can use it.
    pass
harry=Employee()
rohan=Employee()

harry.name="HARRY"
harry.salary=500
harry.role="instructor"

rohan.name="ROHAN"
rohan.salary=499
rohan.role="coordinator"

print(harry.salary)
print(harry.no_of_leaves)
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)   #no doubt we will get the same value in each case
rohan.no_of_leaves=8   #instance variable which means that, this particular class has its own properties

print(Employee.no_of_leaves)  #we will again get 12 as output , since rohan's property is only changed
print(rohan.__dict__)

"CONSTRUCTORS"
class Employee():



    no_of_leaves=12

    def printdetails(self):  #"self" value depends on the object we are asking for.
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

harry=Employee()
rohan=Employee()

harry.name="HARRY"
harry.salary=500
harry.role="instructor"

rohan.name="ROHAN"
rohan.salary=499
rohan.role="coordinator"

print(rohan.printdetails())  #rohan's details will get printed, very obvious
print(harry.printdetails())  #harry's details will get printed, very obvious

"if would feel great , if there were no need to write such big details(line 507 - 513) , straightforwardly"
"saying that , this is not the wise option , instead of it we can directly give an argument to Employee class"
"but we cannot do such thing in this easy way , so we have to use constructor for this purpose."
"basically , constructor is something , which allows users to pass the argument to the class"
#so lets do it.

class Employee():  #time-saving
    no_of_leaves=12
    def __init__(self, aname, asalary, arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

harry=Employee("harry","500","instructor")
print(harry.salary)
 #remember if we are giving any argument to class , it will be handled by init


class Employee():  #time-saving
    no_of_leaves=12
    def __init__(self, aname, asalary, arole):
        self.name=aname
        self.salary=asalary
        self.role=arole


    def printdetails(self):
            return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

        # Class Methods

    def change_leaves(cls, newleaves):
            cls.no_of_leaves=newleaves

harry=Employee("harry","500","instructor")
rohan=Employee("rohan","499","coordinator")

harry.change_leaves(34)
print(harry.no_of_leaves)

"Practising Objects & Classes"
class Workers():

    def printinfo(self):
        return f"Name is {self.name}. workingdays are{self.workingdays}"

prabal=Workers()
prakhar=Workers()

prabal.name="PRABAL"
prabal.workingdays=30

prakhar.name="PRAKHAR"
prakhar.workingdays=20

print(prakhar.printinfo())
print(prabal.printinfo())

"ALTERNATE METHOD TO PRINT INFO SEPERATELY"
class Workers():
    def __init__(self, bname, bworkingdays):
        self.name="bname"
        self.workingdays="bworkingdays"

    def printinfo(self):
        return f"Name is {self.name} and workingdays are {self.workingdays}"

Prakhar=Workers("PRAKHAR" , "20")
print(Prakhar.workingdays)

"ABSTRACTION AND ENCAPSULATION"
"encapsulation basically means that we are just bothered about output , not the entire process like why and how it is processin?"
"let us take above example of WORKERS CLASS , when we are printing printinfo , we are just bothered about the correct output and not about how it is doing all that things"
"basically , it hide the implementation process"

#INHERITANCE "SINGLE INHERITANCE"
class A:
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B(A):
    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")


a1=A()
a1.feature1()
a1.feature2()

b2=B()
b2.feature1()
b2.feature3()

class A:
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B:
    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")

class C(B,A):
    def feature5(self):
        print("feature 5 is working")

c1=C()
c1.feature2()
c1.feature1()
c1.feature3()

"MULTILEVEL INHERITANCE"
class Dad(): #blue dot is representing that this class is overridden(used for inheritance)
    basketball=1 #this is just a random no. , here we can say it as a score

class Son(Dad):
    dance=1
    def idance(self):
        return f"yes i can dance{self.dance}"

class Grandson(Son):
    dance=6
    def idance(self):
        return f"i can dance awesomely{self.dance}"

darry=Dad()
larry=Son()
harry=Grandson()

print(harry.idance())   #parathesis of idance means that Grandson class has attribute named iDance & it is able to inherit from it directy.
print(harry.basketball) #concept is that firstly, grandson will see in its class that whether , is there any attribute named basket ball, if there is , it will directly print its vallue otherwise it will see in upper class from where it is inherited.

"POLYMORPHISM means ability to take various functions"
#for example
print(5+6)
print("5"+"6")

"SUPER AND OVERRIDING()"
class A():
    classvar1="i m class variable in A"
    def __init__(self):
        self.var1="i m inside class A's Constructor"
        self.classvar1="instance variable in class A"
        self.special="special"
class B(A):
    classvar2="i m in class B"

    def __init__(self):
        self.var1 = "i m inside class A's Constructor"   #overide lines 679 & 680
        self.classvar1 = "instance variable in class A" #if any constructor is overwritten , then uska wajud hi mit jayega for example constructor of class A is overwritten

a=A()
b=B()

print(b.classvar1)
#print(b.special) as you can clearly see while printing b.special, we are getting error as uska wajud hi mit gaya.

"but if we want that we can do by using super().__init__(): in second class , lets try"

class A():
    classvar1="i m class variable in A"
    def __init__(self):
        self.var1="i m inside class A's Constructor"
        self.classvar1="instance variable in class A"
        self.special="special"
class B(A):
    classvar2="i m in class B"

    def __init__(self):
        super().__init__()
        self.var1 = "i m inside class A's Constructor"   #overwrite lines 679 & 680
        self.classvar1 = "instance variable in class A" #if any constructor is override , then uska wajud hi mit jayega for example constructor of class A is overwritten

a=A()
b=B()

print(b.classvar1)
print(b.special) #yes it is working

"OPERATOR OVERLOADING"
#methods starting with __(double underscore) and ending with double underscore are called DUNDER METHODS.for ex. __init__

class Employee():  #time-saving
    no_of_leaves=12
    def __init__(self, aname, asalary, arole):
        self.name=aname
        self.salary=asalary
        self.role=arole


    def printdetails(self):
            return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

        # Class Methods

    def change_leaves(cls, newleaves):
            cls.no_of_leaves=newleaves

    def __add__(self, other):                      #dunder methods
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

harry=Employee("harry",500,"instructor")
rohan=Employee("rohan",499,"coordinator")
print(harry + rohan)
print(harry/rohan)
print(harry)


"ABSTRACT BASE CLASS AND ABSTRACT METHOD @abstractmethod"
#iska concept is something like , if we are defining any class and then making other class from inheritance
#we have to consider that some methods must be implemented in the other classs , for inheritance,otherwise it will show error\
"for example"
from abc import ABCMeta, abstractmethod
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type="Rectangle"
    sides=4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length*self.breadth

rect1=Rectangle()
print(rect1.printarea())
#remember we cannot create object from abstract class

"SETTERS AND PROPERTY DECORATORS"
class Employee():
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
        self.email=f"{fname}.{lname}@gmail.com"
    def explain(self):
        return f"this employee is {self.fname} {self.lname}"


    def printemail(self):
        pass

SinhaJi=Employee("Sinha", "Ji")
SharmaJi=Employee("Sharma", "Ji")

print(SinhaJi.explain())
print(SinhaJi.email)

SinhaJi.fname="Pandey"
print(SinhaJi.email) #but its email will not get changed #strange but anyway to do so , we have to make email as an attribute
#lets write above code once more to see the change


class Employee():
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
       # self.email=f"{fname}.{lname}@gmail.com"
    def explain(self):
        return f"this employee is {self.fname} {self.lname}"

    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"  #changing this willchange the email

Sinha_Ji=Employee("Sinha", "Ji")
Sharma_Ki=Employee("Sharma", "Ki")

print(Sinha_Ji.explain())
print(Sinha_Ji.email())

Sinha_Ji.fname="Pandey"
print(Sinha_Ji.email())   #will change but if we use a decorator for email function as a property,we will not use email() inside print(Sinha_Ji.email()) because it will take this function as a property
                           #lets see it down.

class Employee():
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
       # self.email=f"{fname}.{lname}@gmail.com"
    def explain(self):
        return f"this employee is {self.fname} {self.lname}"

    @property  #decorator
    def email(self):
        if self.fname==None or self.lname==None:  #this step is done to avoid throwing None as a output
            return "Email is not set"
        return f"{self.fname}.{self.lname}@gmail.com"  #changing this willchange the email

    @email.setter #decorator
    def email(self, string):
        print("Setting Now......")
        names=string.split("8")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    @email.deleter  #decorator
    def email(self):
        self.fname=None
        self.lname=None

Sinha_Ji=Employee("Sinha", "Ji")
Sharma_Ki=Employee("Sharma", "Ki")

print(Sinha_Ji.explain())
print(Sinha_Ji.email)

Sinha_Ji.fname="Pandey"
print(Sinha_Ji.email)
Sinha_Ji.email="this.that@gmail.com"

print(Sinha_Ji.fname)
print(Sinha_Ji.lname)
print(Sinha_Ji.email)
 #to delete, any component we have to make deleter to delete.if we try to delete it directly ot will throw an error

#now if we delete , it will throw output as "none" generally in object oriented programming , if we delete anything we try to show output as none but that can be prevented as well by using if statement , lets do that as well
del Sinha_Ji.email
print(Sinha_Ji.email)

"GENERATORS iN PYTHON"
"""
Iterable - __iter__ or __getitem__()
Iterator - __next__()
Iteration - 
"""
#iterators
def gen(n):
    for i in range(n):
        yield i

g=gen(3)
print(g.__next__())  #output - 0
print(g.__next__())  #output - 1
print(g.__next__())  #output - 2
    #if we do it again it will throw an error because n=3 , it cannot exceed the value of n.

#but if we use for loop for iteration , it will automatically handle the stop itration and we will not get error
for i in g:
    print(i)

p="Prakhar"
ier=iter(p) #iterable  #remember integers are not iterable
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

#we can do the same task using for loop as well
p="Prakhar"
for i in p:
    print(i)  #but if we print (p) , it will print Prakhar upto 7 times because it has 7 characters

"COMPREHENSIONS (List Comprehension)"
#consider if we need a list of multiples of 3 b/w 0 & 100
#how can we do it , one approach is this
ls=[]
for i in range(100):
    if i%3==0:
        ls.append(i)

print(ls)

#but this can be done in just one line using list comprehensions.

ls1=[i for i in range(100) if i%3==0]
print(ls1)

"DICTIONARY COMPREHENSION"
dict1={i:f"items(i)" for i in range(5)}
#we can also reverse key and value the dictionary usnig DICTIONARY COMPREHENSION
dict2={value:key for key,value in dict1.items()}
print(dict1,"/n",dict2)

"SET COMPREHENSION"
dresses={dress for dress in ["dress1","dress2","dress1","dress2"]}
print(dresses)  #we will get each value only one time as we know duplication in sets is not possible

print("no. of items to include in the list")
n1 = int(input())
print("what items to include in the list")
n2=str(input())
for n2 in range(n1):
    n3 = input(n2)

print("What kind of comprehension you want?")
n4 = input()
if n4 == "Dictionary Comprehension":
    pass
    dict5={n2:n3 for n2 in range(n1)}
    print(dict5)

"Using Else With For Loops"
khana=["roti","sabji","dal"]
for item in khana:
    print(item)
                                 #if we use break , we will only get roti and else will not get printed
else:
    print("this for loop ended properly")

"Function Caching"
import time
from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    #some task taking n seconds
    time.sleep(n)
    return n

if __name__=="__main__":
    print("Now Running Some Work")
    some_work(3)  #iske liye 3 seconds ka time lag
    some_work(1)
    some_work(6)  # 1,6,4 will come immediately because they are cached which means after printing some_work(9), it will again take 3 seconds to print some_work(3) , it is because we have assigned max size==3 which implies ye peeche ki 3 values cache memory mein store kr dega so it will get printed immediately but if we increase the max size say 32 , there will be no time lag and some_work(3) will also get printed immediately after some_work(9)
    some_work(4)
    print("Done.... calling again")
    some_work(3)  #iska turant ho gaya  because we have done caching #ye wala some_work save ho jaayega thats why we will get this immediately
    print("Called Again")

"COROUTINES"
def searcher():   #searcher is not a ordinary function , it is COROUTINE function but how will python understand this , the answer is through while loop
    import time
    #some 4 seconds consuming task
    book="Prakhar is an amazing guy"
    time.sleep(2)   #assume delay as read krne ka time.

    while(True):
        text=(yield )
        if text in book:
            print("your text is in the book")

        else:
            print("your text is not in the book")

search=searcher()
next(search)
search.send("is an")   #getting each of them will not have a delay of 2 seconds , only first will take 2 seconds because after that values are getting printed from while loops.
search.send("not")
search.send("Prakhar")
search.close()    #but if we send values again after closing search it will throw an error which is very obvious










