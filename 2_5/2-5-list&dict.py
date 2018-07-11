# -*- encoding:utf-8 -*-  
import string

print(string.ascii_letters)

a_list = range(10)
print('a_list:', list(a_list))

b_list = [i*i for i in a_list]
print('b_list:', b_list)

b_dict = {i: string.ascii_letters[i] for i in a_list}
print('b_dict:', b_dict)

print('++++++++++++++++++++++++++++++++++++++++=')

for i in b_list:
    print(i)

for i in range(len(b_list)):
    print(a_list[i], end=', ')
print()

for index, value in enumerate(b_list):
    print(index, '-->', value, end=', ')
print()

for i in b_dict:
    print(i, '-->', b_dict[i], end=', ')
print()

for key, value in b_dict.items():
    print(key, '-->', value, end=', ')
print()