#1.# m=[[x,y] for x in range(0,4) for y in range(0,4)]  
#ans:16

#2 kvps={"1":1,"2":2}
# theCopy=kvps
# kvps["1"]=5
# sum=kvps["1"]+theCopy["1"]
# print(sum)
#Ans:10

#3 test_list=[1,2,3,4,5]
# for i in test_list:
#     print(i,end='')
#     if i==2:
#         test_list.remove(i)

# Ans:1245

#4 def even_infinite():
#     num=0
#     while True:
#         yield num
#         num+=2
# evev_iter_obj=even_infinite()
# for i in range (2):
#     next(evev_iter_obj)

# print(next(evev_iter_obj))
# #Ans:4

# import re
# regx='(\w+)8(\w+)9(\w+)'
# m=re.search(regx,'applr8mango9kiwi')
# print(len(m.groups()))
# ans:3

# 6.
# sum=0
# for i in range(4):
#     sum+=i
# print(sum)
# sum(34,23)
# Ans:6,error

#7 def check_even_odd(**check):
#     if check['isEven']%2==0:
#         print('even')
#     else:
#         print('Odd')
# check_even_odd(isEven=3)

# Ans:odd

#8 class Animal():
#     def __init__(self,name):
#         print("Animal",end="")
#         self.name=name
# class Dog(Animal):
#     def __init__(self,name,age):
#         print("Dog",end='')
#         super().__init__(name)
#         self.age=age

# yuki=Dog("yuki singh",4)

# Ans:DogAnimal

# Q.9
# def a(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return a(n-1)+a(n-2)

# for i in range(0,4):
#     print(a(i),end='')
# Ans:0112

# Q.10
#  [A-Z]+[a-z]+$ 


# Q.11
# s='Python,Java,C,C++'
# print(s[10:1:-2])
# ans:aa,ot

#12 m=[[x,x+1,x+2] for x in range(0,3)]
# print(m)
# ans:[[0, 1, 2], [1, 2, 3], [2, 3, 4]]

#13 d={"id":101,"name":"ABC"}
# a=d.setdefault("name","PQR")
# print(a)
# ans=ABC


#14 x=50
# def fun():
#     global x
#     print('x is',x)
#     x=2
#     print('changble global x to',x)
# fun()
# print('value of x is',x)
# ans:x is 50
# changble global x to 2
# value of x is 2  

#15 def find(a,**b):
#     print(type(b))
# find('letters',A='1',B='2')
#ans: dict

#16 l=[1,2,3,4]
# iter_object=iter(l)
# while True:
#     try:
#         print(next(iter_object),end='##')
#     except StopIteration:
#         break
# ans:1##2##3##4##

#17 for item in csv_reader:
#     print(item)

#18 class X:
#     def __init__(self):
#         print("inside X",end='*')
#     def fun(self):
#         print("fun of X",end='*')
# class A(X):
#     def __init__(self):
#         print("inside A",end='*')
#     def fun(self):
#         print("fun of A",end='*')
# class B(X):
#      def __init__(self):
#         print("inside B",end='*')

#19 i=0
# while i<3:
#     i+=1
# print('i is',i)
# Ans:i is 3


#20 import re
# sentence = 'horses are fast'
# regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
# matched = re.search(regex, sentence)
# print(matched.group(2))
# Ans:are

#21 a=lambda x: return x
# print(a(2))
# ans:SyntaxError: invalid syntax

#22 test_list=[1,2,3,4,5]
# test_list_duplicate=test_list
# print(id(test_list)==id(test_list_duplicate))
# ans:True

#23 def d(f):
#     def n(*args):
#         return "$" + str(f(*args))
#     return n
# @d
# def p(a,t):
#     return a+a*t

# print(p(100,0))
# ans:$100


#24 import re
# sentence = 'we are humans'
# matched = re.match(r'(.*) (.*?) (.*)', sentence)
# print(matched.groups())
# ans:('we', 'are', 'humans')

#25 class Sales:
#     def __init__(self,id):
#         self.id=id
#         id=100

# val=Sales(123)
# print(val.id)
# ans:123

#26 def a(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return a(n-1)+a(n-2)
# for i in range(0,4):
#     print(a(i),end="")
# ans:0112