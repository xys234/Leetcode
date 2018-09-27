a_list = [1,2,3]
print(id(a_list))
a_list = a_list + [4,5]
print(id(a_list))

b_list = [1,2,3]
print(id(b_list))
b_list.append(4)
print(id(b_list))