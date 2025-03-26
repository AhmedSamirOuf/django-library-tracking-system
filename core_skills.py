import random

def is_less_than_10(number):
    return number < 10

rand_list = []
for i in range(1,10):
    rand_list.append(random.randint(1,20))

# print(rand_list)
list_comprehension_below_10 = [rand for rand in rand_list if rand < 10]

# print(list_comprehension_below_10)

list_comprehension_below_10_using_filter = filter(is_less_than_10,rand_list)

# for item in list_comprehension_below_10_using_filter:
#     print(item)