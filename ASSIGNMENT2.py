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
