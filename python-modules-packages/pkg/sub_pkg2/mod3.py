def baz():
    print('[mod3] baz()')
    
class Baz:
    pass

# go up one level with '..'
from .. import sub_pkg1
print(sub_pkg1)

from ..sub_pkg1.mod4 import qux
qux()

'''
from pkg.sub_pkg2 import mod3
Invoking __init__.py for pkg
<module 'pkg.sub_pkg1' (namespace)>
[mod4] qux()
'''