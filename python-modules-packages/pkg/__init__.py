# for 'from pkg import *' importing everything in the package:
__all__ = [
    'mod1',
    'mod2'
    ]

# will be imported into global namespace on module-Import from this package
print(f'Invoking __init__.py for {__name__}')
A = ['waka', 'Asthernbaum', 'Ronaldo McDonaldo']

'''
>>> import pkg
Invoking __init__.py for pkg
>>> pkg.A
'''

# or

'''
def foo():
    from pkg import A
    print('[mod1] foo() / A = ', A)

class Foo:
    pass
'''