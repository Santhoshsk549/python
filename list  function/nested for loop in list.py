nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested list:", nested_list)
print()
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Element at [1][2]:", nested_list[1][2])
print()

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat_list = [num for sublist in nested_list for num in sublist]
print("Flattened list:", flat_list)
print()

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print("Common elements:", common)
print()

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
difference = list(set(list1) - set(list2))
print("Elements in list1 but not in list2:", difference)
print()

my_list = [1, 2, 3, 2, 4, 2, 5]
element = 2
new_list = [x for x in my_list if x != element]
print("List after removing all occurrences of", element, ":", new_list)
print()

my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print("Converted tuple:", my_tuple)
print()
my_list = [10, 20, 30, 40, 50]
average = sum(my_list) / len(my_list)
print("Average:", average)
print()

numbers = [1, -2, 0, 5, -7, 0, 8]
pos = neg = zero = 0
for num in numbers:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1
print("Positive:", pos)
print("Negative:", neg)
print("Zero:", zero)
print()

numbers = [2, 3, 4, 5]  
product = 1

for num in numbers:
    product *= num

print("Product of all elements:", product)


