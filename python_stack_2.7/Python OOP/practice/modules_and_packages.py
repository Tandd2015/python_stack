# modules

# # import the library
# import urllib
# # Note: there's a urllib version for each version of Python
# # Use urllib2 if your using Python 2
# # Use urllib3 for Python 3
# # Finally, use it...
# urllib.urlopen(...)

import arithmetic
print arithmetic.add(5, 8)
print arithmetic.subtract(10, 5)
print arithmetic.multiply(12, 6)

import urllib

dir(urllib)

help(urllib)

# print dir(urllib)
# print help(urllib)

# packages

from my_package.subdirectory import my_functions
import my_modules.test_module
#            OR
# from my_modules import test_module
__all__ = ["test_module"]

# sample_project
#     |_____ python_file.py
#     |_____ my_modules
#                |_____ __init__.py
#                |_____ test_module.py
#                |_____ another_module.py
#                |_____ third_module.py






