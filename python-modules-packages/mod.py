'''
Created on 15.09.2020

@author: jochen.gebsattel
'''

s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')
    
class Foo:
    pass


'''
sys.path.append(r'/home/jochen.gebsattel/LiClipse Workspace/RealPython/python-modules-packages')
import mod
mod.__file__
'/home/jochen.gebsattel/LiClipse Workspace/RealPython/python-modules-packages/mod.py'
import re
re.__file__
'/home/jochen.gebsattel/anaconda3/lib/python3.7/re.py'
print(mod.s)
If Comrade Napoleon says it, it must be right.
mod.a
[100, 200, 300]
mod.foo('quix', 'corge', 'grault')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: foo() takes 1 positional argument but 3 were given
mod.foo(['quix', 'corge', 'grault'])
arg = ['quix', 'corge', 'grault']
x = mod.Foo()
x
<mod.Foo object at 0x7f78ff3d8750>
'''