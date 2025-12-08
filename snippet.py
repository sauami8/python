def myf(*args, **kwargs):
    print(f'args values are {args}')
    print(f'kwargs values are {kwargs}')
    print ('unpacking args and kwargs values')
    return args, kwargs
l=[10,20,30,40]
d= {"name":"Saurabh", "age":26, "city":"Kitchener", "phone":'888-888-8888'}

print(myf(l, d))

import random as r
print('Random number between 1 to 100 is: ', r.randint(1,100))
print('Random choice from list is: ', r.choice(['apple', 'banana', 'mango', 'grapes']))

# import os as s
# print('Current working directory is: ', s.getcwd())
# print('List of files and directories in current working directory are: ', s.listdir())
# print('Environment variables are: ', s.environ)
# print('OS name is: ', s.name)
# print('OS path separator is: ', s.path.sep)
# print('OS path current directory is: ', s.path.curdir)
# print('OS path absolute path is: ', s.path.abspath('.'))
# print('OS path join example is: ', s.path.join(s.getcwd(), 'snippet.py'))

import antigravity
antigravity.fly()