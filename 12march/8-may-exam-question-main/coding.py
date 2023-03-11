#Q.1 sum of letters

# str=input("Enter a string:")
# s=0
# for i in str:
#     x=0
#     y=1
#     if i=="A":
#         y=0
#     else:
#         for j in range(ord(i)-66):
#             z=x
#             x=y
#             y+=z
#     k=y
#     s+=k
# print(s)

# Q.2 on ={'+','-','/','*'}
# class UserMainCode(object):
#     @classmethod
#     def letter(cls,input1):
#         '''
#         input1:string
#         Expected return type: int
#         '''
#         s=input1
#         n=len(s)
#         stack=[]
#         a={'+','-','/','*'}
#         for i in range(n):
#             if s[i].isdigit():
#                 stack.append(int(s[i]))
#             elif s[i]=='+':
#                 op1=stack.pop()
#                 op2=stack.pop()
#                 stack.append(int(op2)+int(op1))
#             elif s[i]=='-':
#                 op1=stack.pop()
#                 op2=stack.pop()
#                 stack.append(int(op2)-int(op1))
#             elif s[i]=='/':
#                 op1=stack.pop()
#                 op2=stack.pop()
#                 stack.append(int(op2)/int(op1))
#             elif s[i]=='*':
#                 op1=stack.pop()
#                 op2=stack.pop()
#                 stack.append(int(op2)*int(op1))
#             return stack.pop()
                

#Q.3: sorted
# class UserMainCode(object):
#     @classmethod
#     def SortStudentMarks(cls,input1)
# dict1={}
# for i range(input2):
#     sum1=0
#     for j in range(input1):
#         sum1+=input3[j][i]
#         dict1[i]=sum1

# lowest=min(dict1.key=dict1.get)
# for i in range (input1):
#     x=input3[i][lowest]
#     print(x)
#     input3[i].remove(x)
# print(input3)
# print(len(input3))

# result=list(map(sum,input3))
# return result