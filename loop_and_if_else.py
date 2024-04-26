# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<    IF-ELSE    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# available_balance=15000
# message="""
# Enter 1 for checking balance
# Enter 2 for deposit amount
# Enter 3 for withdrawl
# """
# print(message)
# task=int(input('Enter: '))

# if task==1:
#     #check balance
#     print('Your available balance is ',available_balance)
# elif task==2:
#     #deposit
#     deposit=int(input("Enter the amount to be deposited:"))
#     if deposit>0 and deposit<100000:
#         available_balance+=deposit
#         print(f"{deposit} is successfully deposited in your account")
#         print('Available balance is ',available_balance)
#     else:
#         print("Enter a valid amount")
# elif task==3:
#     #withdrawl
#     withdrawl=int(input("Enter the withdrawl amount:"))
#     if withdrawl>available_balance:
#         print("Available Balance is not sufficient")
#     else:
#         available_balance-=withdrawl
#         print(f"{withdrawl} is debited from your account")
#         print("Available balance is",available_balance)
# else:
#     print("Enter a valid task")




#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<      for loop    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
##for i in range(x):
# #for loop body
# #print(i)


# for i in range(9):
#     print(i)


# LIST=list(range(20))
# print(LIST)


# LIST=[10,20,30,60,50]
# x=int(input("Enter the item you want to search:"))
# for item in LIST:
#     if item==x:
#         print(f"{x} is in list")
#     else:
#         print(f"{x} is not in list")


# Tuple=(10,20,30,60,50)
# for item in Tuple:
#     print(item)


# String="vanshika"
# for char in String:
#     print(char)


# dt={'name':'vanshika','branch':'cse','age':20}
# print(dt.values())
# print(dt.keys())


# dt={'name':'vanshika','branch':'cse','age':20}
# for item in dt.values():
#     print(item)


# even=[]
# odd=[]
# sum=0
# Listssss=[21,62,43,444,5,16,7,78,49,11]
# for item in Listssss:
#     print(item)
#     if item%2==0:
#         even.append(item)
#     else:
#         odd.append(item)
# a=len(even)
# print(f'Total no of even no is {a}')
# b=len(odd)
# print(f'Total no of odd no is {b}')

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  WHILE LOOP  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# intialization
# while
# body
# increment


# i=0
# while i<10:
#     print(i)
#     i=i+1

## to make infinite value use True
# condition=True
# while condition:
#     print("hello")
#     condition=False


### break for breaking the code
### continue continues the code  of the outer iteration, breaks the current iteration
# for i in range(1,21,2):
#     print(i)
#     if i==10:
#         break
# for i in range(21):
#     if i==10:
#         continue
#     print(i)
    



