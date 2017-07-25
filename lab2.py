Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> "dont"+"forgot"+"to"+"converse"+"water"
'dontforgottoconversewater'
>>> 'dont+'forget'+'to'+'converse'+'water'
SyntaxError: invalid syntax
>>> "the"*3
'thethethe'
>>> 'the'+3
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    'the'+3
TypeError: Can't convert 'int' object to str implicitly
>>> "the"*3+"beautiful"+"earth"
'thethethebeautifulearth'
>>> 2*"true"
'truetrue'
>>> a='save
SyntaxError: EOL while scanning string literal
>>> a='save'
>>> b='the'
>>> c='planet'
>>> (a+b*5)
'savethethethethethe'
>>> a+b*5
'savethethethethethe'
>>> a=4
>>> b='panda bears'
>>> (a+b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    (a+b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> a='4'
>>> b='panda bears'
>>> (a+b)
'4panda bears'
>>> a='4 '
>>> b='panda bears'
>>> (a+b)
'4 panda bears'
>>> plants="i need water"
>>> plannts()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    plannts()
NameError: name 'plannts' is not defined
>>> plants()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    plants()
TypeError: 'str' object is not callable
>>> len(plants)
12
>>> len(planta+100)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    len(planta+100)
NameError: name 'planta' is not defined
>>> len(plants+100)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    len(plants+100)
TypeError: Can't convert 'int' object to str implicitly
>>> len(plants*5)
60
>>> upper()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    upper()
NameError: name 'upper' is not defined
>>> upper(plants)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    upper(plants)
NameError: name 'upper' is not defined
>>> test="i love meet"
>>> test.upper()
'I LOVE MEET'
>>> test.lower()
'i love meet'
>>> test.capitalize.()
SyntaxError: invalid syntax
>>> test.capitalize()
'I love meet'
>>> test.swapcase()
'I LOVE MEET'
>>> test.replace()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    test.replace()
TypeError: replace() takes at least 2 arguments (0 given)
>>> test.replace("o","i")
'i live meet'
>>> test.replace("e","i","w")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    test.replace("e","i","w")
TypeError: 'str' object cannot be interpreted as an integer
>>> test.replace("i","o")
'o love meet'
>>> a="MEET"
>>> b="meet"
>>> c="meat"
>>> a==b
False
>>> a==c
False
>>> b==c
False
>>> a !=b
True
>>> a=b
>>> a !=c
True
>>> b !=c
True
>>> ==
SyntaxError: invalid syntax
>>> !=
SyntaxError: invalid syntax
>>> a !=b
False
>>> a !==b
SyntaxError: invalid syntax
>>> a!==b
SyntaxError: invalid syntax
>>> a !=b
False
>>> a == b
True
>>> a
'meet'
>>> b
'meet'
>>> a="meet"
>>> b="meat"
>>> c="meal"
>>> a == b
False
>>> a == c
False
>>> a ==a
True
>>> meet_value="alexadamfarahkatamir"
>>> meet_value{17:2}
SyntaxError: invalid syntax
>>> meet_value="alexadamfarahkatamir"
>>> my_string=“bananayellowthinkhatgreyBIGcalifornia314”
SyntaxError: invalid character in identifier
>>> my_string = “bananayellowthinkhatgreyBIGcalifornia314”
SyntaxError: invalid character in identifier
>>> my_string = "bananayellowthinkhatgreyBIGcalifornia314"
>>> my_string{0}
SyntaxError: invalid syntax
>>> my_string[0]
'b'
>>> my_string[12:17]
'think'
>>> my_string[24: ]
'BIGcalifornia314'
>>> my_string[24:27]
'BIG'
>>> print(my_string)
bananayellowthinkhatgreyBIGcalifornia314
>>> my_string=[12:17]+" "+[24:27]
SyntaxError: invalid syntax
>>> meet_value=my_string[12:17]+" "+my_string[24:27]
>>> meet_value
'think BIG'
>>> upper(think)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    upper(think)
NameError: name 'upper' is not defined
>>> meet_value.upper(think)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    meet_value.upper(think)
NameError: name 'think' is not defined
>>> meet="think big"
>>> meet.upper(think)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    meet.upper(think)
NameError: name 'think' is not defined
>>> think.upper()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    think.upper()
NameError: name 'think' is not defined
>>> meet.upper()
'THINK BIG'
>>> 
