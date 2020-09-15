'''
distinguish between when the file is loaded as a module and when it is run as a standalone script:
when a .py file is imported as a module, Python sets the special dunder variable __name__ to the name of the module.
If a file is run as a standalone script, __name__ is set to the string '__main__'.
'''

s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

if (__name__ == '__main__'):
    print('Executing as standalone script')
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)
