# -*- encoding:utf-8 -*-  
### 函数为第一公民的应用
import string

def a_function(x):
    if isinstance(x, int):
        if 0 <= x < len(string.ascii_letters):
            return string.ascii_letters[x]
    else:
        return 'x is not valid'

def b_function(a_list=None, func=None):
    for index, value in enumerate(a_list):
        print(index, '->', func(value))

    return None

b_function(a_list=[1, 3, 8, 'a', 'b', '^_^', 10], func=a_function)