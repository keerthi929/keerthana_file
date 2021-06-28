1)   IndexError
L1=[1,2,3]
 L1[3]
 
#Error      
L1[3]
IndexError: list index out of range

2)   ModuleNotFoundError

  >>>import notamodule
  
  #error 
import notamodule
ModuleNotFoundError: No module named 'notamodule'

3)   KeyError

d={'1':"aa", '2':"bb", '3':"cc"}
d['4']

#Error
            
D1['4']
KeyError: '4'

4)    ImportError

>>>from math import cube

#Error 

from math import cube
ImportError: cannot import name 'cube

5)     StopIteration Error


>>>it=iter([1,2,3])
next(it)
1
 next(it)
2
 next(it)
3
next(it)
 
 #Error
next(it)
StopIteration

6)  Type Error

2'+2

#Error  
>>>'2'+2
TypeError: must be str, not int in line1

7) Value Error

 >>>int('xyz')

 #Error
int('xyz')
ValueError: invalid literal for int()

8) NameError
>>>>age

#Error
            
age
NameError: name 'age' is not defined

9)    ZeroDivisionError

>>> x=100/0

#Error
x=100/0
ZeroDivisionError: division by zero


10)    KeyboardInterrupt

>>> name=input('enter your name')
enter your name^c

  #Error
       
name=input('enter your name')
KeyboardInterrupt

11)Syntax Error
def some_function()
    msg = 'hello, world!'
    print(msg)
     return msg
     
  #Error
    def some_function()
                       ^
SyntaxError: invalid syntax

12)  Indentation Error

def some_function():
    msg = 'hello, world!'
    print(msg)
     return msg
     
  #Error
    return msg
    ^
IndentationError: unexpected indent
13)  Name error

>>>print(a)
#Error

NameError                                 

NameError: name 'a' is not defined