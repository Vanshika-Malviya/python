# def total(num1,num2):
#     SUM=num1+num2
#     return SUM

# def mul(m,s):
#     MUL=m*s
#     return MUL

### lis=[1,4,6,7,87,23,45,76,11,22]


# strin=input("Enter list : ")
# num=strin.split()
# num=[int(n) for n in num]

def avg_cal(A):
    totalsum=sum(A)
    totalelements=len(A)
    print("Your avg is ",totalsum/totalelements)
input_string=input("Enter the elements of the list: ")
num=input_string.split()
num=[int(n)for n in num]
avg_cal(A=num)


### THIS LINE HELPS To STOP EXECIUTING THIS FILE IN LINKED FILE IT WILL ONLY EXECUTE WHEN IT IS executed HERE ONLY
# if __name__=="__main__":
#     print("Hello")