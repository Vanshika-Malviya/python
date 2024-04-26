# a='Ram'
# b='and'
# c='Shyam'
# print(a,b,c)



# x=10
# y=11
# z=5
# if(x>y) and (x>z):
#  print('the largest no is',x)
# elif(y>x) and (y>z):
#  print('the largest no is',y)
# else:
#  ('the largest no is',z)



###____________________ASSIGNMENT2_______________________:
#Q1. min and max from list 
#Q2.  avg using for loop

# sum=0
# items=[10,23,45,65,32,2,3,99,46,21,33]
# for i in items:
#     sum+=i
# a=len(items)
# avg=sum/a
# print("Average of the list is",avg)



# input_string=input("Enter the elements of the list: ")
# num=input_string.split()
# num=[int(n)for n in num]
# ### num=[10,23,4,54,78,90,12,11,222,1]
# largest=num[0]
# smallest=num[0]
# for i in num:
#     if i > largest:
#         largest=i
#     if i < smallest:
#         smallest=i
# print(f"{largest} is max")
# print(f"{smallest} is min")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
###  CALCULATOR FUNCTION
# def CAL(num1,num2,operation):
#     if operation=='add':
#             Add=num1+num2
#             return Add
#     elif operation=='subtract':
#             sub=num1-num2
#             return sub
#     elif operation=='multiply':
#             mul=num1*num2
#             return mul
#     elif operation=='divide':
#         div=num1/num2
#         return div
#     else:
#         print("Enter a valid operation !!!")
# print("Choose a operation: add , subtract , multiply , divide ")
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# operation=input("Enter a operation: ")
# result=CAL(num1,num2,operation)
# print(result)

# def palindrome(S):
#     a=""
#     for i in STRING:
#         a=i+a
#     if STRING==a:
#         print(f"{STRING} is PALINDROME")
#     else:
#         print(f"{STRING} is not PALINDROME")
# STRING=input("Enter a string: ")
# palindrome(S=STRING)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   ASSIGNMENT 2  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
### Q1. PALINDROME FUNCTION
def PALINDROME(s):
    reverse=reversed(STRING)
    if list(reverse)==list(STRING):
        print("TRUE")
    else:
        print("FALSE")
STRING=input("Enter something : ")
PALINDROME(s=STRING)


### Q2. CALCULATOR FUNCTION
def CAL(num1,num2,operation):
    if operation=='add':
        print(f"{num1} + {num2} =",num1+num2)
    elif operation=='subtract':
        print(f"{num1} - {num2} =",num1-num2)
    elif operation=='multiply':
        print(f"{num1} x {num2} =",num1*num2)
    elif operation=='divide':
        print(f"{num1} / {num2} =",num1/num2)
    else:
        print("Enter a valid operation !!!")
print("Choose a operation: add , subtract , multiply , divide ")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operation=input("Enter a operation: ")
CAL(num1,num2,operation)

        

### Q3. RIGHT TRIANGLE PATTERN FUNCTION
def right_angle_triangle_function(n):
    for i in range(0,n,1):
        for j in range(0,i+1,1):
            print("* ",end='')
        print("\n")
n=int(input("Enter the number of rows: "))
right_angle_triangle_function(n)


###  Q4. COUNTER FUNCTION
def counter(S):
    count = {}
    for i in S:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(f"Occurrence of all characters in {S} is ",count)
S=input("Enter a string : ")
counter(S)


###  Q5. MULTIPLICATION TABLE FUNCTION
def multiplication_table(n):
    for i in range(1,11,1):
        print(f"{n} x {i} =",n*i)
n=int(input("Enter a number : "))
multiplication_table(n)





