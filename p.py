Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\vanshika\Desktop\4thsem\first.py
hello
1
<class 'str'>
1 abc
6
<class 'bool'>
>>> a='hello world'
>>> a.count('l')
3
>>> a.index('h')
0
>>> b=(1,2,3,3)
>>> b.count(3)
2
>>> b.index(3)
2
>>> a.capitalize()
'Hello world'
>>> a.title()
'Hello World'
>>> a.lstrip()
'hello world'
>>> A=" hello"
>>> A.lstrip()
'hello'
>>> a.split()
['hello', 'world']
>>> x=a.split()
>>> x
['hello', 'world']
>>> '@'.join(x)
'hello@world'
>>> l=[1,2,3,4,5]
>>> l.append(6)
>>> l
[1, 2, 3, 4, 5, 6]
>>> l.insert(1,7)
>>> l
[1, 7, 2, 3, 4, 5, 6]
l.remove(4)
l
[1, 7, 2, 3, 5, 6]
m=[9,99]
l+=m
l
[1, 7, 2, 3, 5, 6, 9, 99]
l+=a
l
[1, 7, 2, 3, 5, 6, 9, 99, 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
[1, 7, 2, 3, 5, 6, 9, 99, 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
[1, 7, 2, 3, 5, 6, 9, 99, 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
y=['hello']
l+=y
l
[1, 7, 2, 3, 5, 6, 9, 99, 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', 'hello']
l.reverse()
l
['hello', 'd', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h', 99, 9, 6, 5, 3, 2, 7, 1]
l.sort()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    l.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
m.sort()
m
[9, 99]
m.append(2)
m.sort(reverse)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    m.sort(reverse)
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
m.sort(reverse=True)
m
[99, 9, 2]
l.sort()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    l.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
t=(1,2,3,)
t.length()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    t.length()
AttributeError: 'tuple' object has no attribute 'length'
t.len()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    t.len()
AttributeError: 'tuple' object has no attribute 'len'
len(t0
    len(t)
    
SyntaxError: '(' was never closed
len(t)
    
3
t.count(1)
    
1
t.append(6)
    
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    t.append(6)
AttributeError: 'tuple' object has no attribute 'append'
t.insert(1,5)
    
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    t.insert(1,5)
AttributeError: 'tuple' object has no attribute 'insert'
l.find('h')
    
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    l.find('h')
AttributeError: 'list' object has no attribute 'find'
dic={'Name':['vanshika','Tanishka','yash'],'Age':[19,20,20]}
    
dic
    
{'Name': ['vanshika', 'Tanishka', 'yash'], 'Age': [19, 20, 20]}
dic['Nmae']
    
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dic['Nmae']
KeyError: 'Nmae'
dic['Name']
    
['vanshika', 'Tanishka', 'yash']
dic['branch']=['cse','ece','it']
    
dic('branch')
    
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    dic('branch')
TypeError: 'dict' object is not callable
dic['branch']
    
['cse', 'ece', 'it']
dic['branch'].append('civil')
    
dic
    
{'Name': ['vanshika', 'Tanishka', 'yash'], 'Age': [19, 20, 20], 'branch': ['cse', 'ece', 'it', 'civil']}
s={1,3,2}
    
s2={4,6,5}
    
s.intersection(s2)
    
set()
s.add('hi')
    
s
    
{1, 2, 3, 'hi'}
s.update(s2)
    
s
    
{1, 2, 3, 4, 5, 'hi', 6}
s.clear()
    
s
    
set()
in=input('enter your name')
    
SyntaxError: invalid syntax
name=input('enter your name')
    
enter your namevanshika
name=input('enter your name: ')
    
enter your name: Vanshika
