### Python basically imagined the loops     {   Behind the Scene    }    

## iter tools or iteration tools    
-  ( for, comprehension, map )  
## for iterable objects
-  list, strings, file

## Response     ( __next__ )


## How internally things work

1) iteration tools query iterable object - that is loop possible ??
    -   So tool send iter() / internal to object
    -   Then object sends __next__ to tool

2) When we get __next__, we net the starting value initially, this tells that more values are there in memory address.

3) At last / final value with next an exception arise "Stop iteration". 


### In python, an object can be iterable or non-iterable on the basis that it has __next__ in its internal properties or not.   {   __next__    -   core syntax that make iterable.     }


### In python immediate garbage collection is not there.    { may have to run the terminal again }


### Shell Working for 01_basics

PS C:\Users\Srish\Desktop\Python\01_basics> python
Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> file = open(chai.py)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'chai' is not defined
>>> file = open("chai.py")
>>> file.readline()                                 <!-- .readline() iterable tool -->
'from hello_intro import chai \n'
>>> file.readline()
'# This created new folder __pycache__\n'
>>> file.readline()
'\n'
>>> file.readline()
'chai("Not Me")'
>>> file.readline()                                 <!--    After the file ends     -->
''          <!--    After the file ends, as exception had already raised that file has already readed     -->
>>> file.readline()
''
>>> file = open("chai.py")                      <!--    File again loaded   -->
>>> file.__next__()             <!--    How python internally treats,   Raw way     -->
'from hello_intro import chai \n'
>>> file.__next__()             <!--    Readline() use this internally, but with execption handling     -->
'# This created new folder __pycache__\n'
>>> file.__next__()
'\n'
>>> file.__next__()
'chai("Not Me")'
>>> file.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> file.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration


for line in open('chai.py').readlines:
<!-- File is also iterable so loops can be used. "readlines not used as not good for memory - heavy"    -->


>>> for line in open('chai.py'):
...     print(line,end="")       
...
from hello_intro import chai
# This created new folder __pycache__

chai("Not Me")>>>


>>> while True: 
...     line = file.readline()
...     if not line:
...             break
...     print(line, end='')
...
from hello_intro import chai
# This created new folder __pycache__

chai("Not Me")


>>> file = open("chai.py") 
>>> while True:
...     line = file.readline()
...     print(line, end='')
...
from hello_intro import chai
# This created new folder __pycache__

        <!-- This does not terminates, nor the endline printed., not getting terminated even by ctrl+z -->


# File also use "iter()".   ( Only for files, internally )



Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> mylist = [ 1, 2, 3, 4, 5, 6]
>>> i = iter(mylist)                      <!--    iter(any_iterable_object) - a method    -->
>>> i
<list_iterator object at 0x0000023CDEB103D0>        <!-- a reference is hold - list_iterator -->
>>> i.__next__()
1
>>> i.__next__()
2
>>> i.__next__()
3
>>> i.__next__()
4
>>> i.__next__()
5
>>> i.__next__()
6
<!--    'i' hold same memory location every time - it doesn't changes     -->
<!--    memory refernce is same but a internal pointer is there for next.    -->
>>> i.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration


>>> range = range(15,20)
>>> r = iter(range)     
>>> r
<range_iterator object at 0x0000023CDE79A0B0>
>>> range
range(15, 20)
>>> r is range
False


>>> f = open("01_basics\\chai.py")
>>> file_ref = iter(f)
>>> file_iter = f.__iter__()
>>> file_ref is f
True
>>> file_iter is f 
True
>>> file_iter is file_ref
True
<!--    Only in files all these are same, file reference (store) taken in a variable is an iterable object.    -->


>>> dict = {1:2, 3:4, 5:6}
>>> d = iter(dict)              <!--    Reference of dictionary is stored in 'd' variable       -->
>>> next(d)
1
>>> next(d)                     <!--    Internally Same     -->
3
>>> d.__next__()
5
>>> d.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> d is dict
False
>>> for key in dict.keys():
...     print(key)
...
1
3
5