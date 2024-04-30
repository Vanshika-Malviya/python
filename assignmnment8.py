# PROGRAM TO FIND FACTORIAL OF A NON NEGATIVE INTEGER
def factorial(nums):
    fact=1
    for i in range(1,nums+1,1):
        fact*=i
    print(f"factorial of {nums} is {fact}")
m=int(input("Enter a number : "))
factorial(nums=m)    


#PROGRAM TO FIND THE COUNT THE NUMBER OF WORDS IN A TEXT FILE
FILE=input("Enter the name of file : ")
count=0
with open(FILE,"r") as text_file:
    for a in text_file:
        word=a.split()
        count=count+len(word)
print(f"Total words in text file {FILE} is {count} ")


#PROGRAM TO FIND MIN AND MAX WITHOUT USINH BUILT IN FUNCTIONS
def minmax(num):
    largest = num[0]
    smallest = num[0]
    for i in num:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
    print(f"{largest} is max")
    print(f"{smallest} is min")

input_string = input("Enter the elements of the list : ")
num = input_string.split()
num = [int(n) for n in num]
minmax(num)


#LONGEST WORD
def longest_word(word_list):
    longest=''
    for words in word_list:
        if len(words)>len(longest):
            longest=words
    print(f"longest word is {longest}")

input_string = input("Enter the elements of the list : ")
word_list= input_string.split()
longest_word(word_list)
