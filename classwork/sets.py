#classwork_sets

#lst (1-100)
#even = even numbers
#odd = odd numbers

#common
#difference
#symm difference
#union

my_list = []
even_list = []
odd_list = []
for i in range(1, 101):
    my_list.append(i)

even_list = [i for i in my_list if i % 2 == 0]
odd_list = [i for i in my_list if i % 2 != 0]

#print(my_list)
#print(even_list)
#print(odd_list)
print(set(even_list).union(set(odd_list)))
print(set(even_list).symmetric_difference(set(odd_list)))
print(set(even_list).intersection(set(odd_list)))
print(set(even_list).difference(set(odd_list)))
