# -*- encoding:utf-8 -*-  
### 匿名函数

func = lambda x: x**2
print(func(20))

a_list = range(10)
print(a_list)
a_list

print(type(map(func, a_list)))

print(map(func, a_list))

print(map(lambda x: x**2, a_list))

listaa = [12,23,32]
print(listaa)