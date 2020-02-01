# encoding: utf-8
"""
@author: sunshuai
@contact: sunshuai.edu@gmail.com
@time: 2020/2/1 3:11 下午
@file: test.py
@desc: 
"""
a = 1

try:
    print(a.endswith('s'))
except AttributeError:
    print('AttributeError')
    pass
finally:
    print('final')