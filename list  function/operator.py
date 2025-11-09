list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print("Combined list:", result)
print()

my_list = [1, 2, 3]
result = my_list * 3
print("Repeated list:", result)
print()

my_list = [10, 20, 30, 40]
element = 30
if element in my_list:
    print(f"{element} exists in the list.")
else:
    print(f"{element} not found in the list.")

print()

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("First 3 elements:", my_list[:3])
print("Last 3 elements:", my_list[-3:])
print()

my_list = [5, 1, 9, 3, 7, 2]
my_list.sort(reverse=True)
print("Largest two numbers:", my_list[:2])
print()

my_list = [1, 2, 3, 2, 4, 1, 5]
duplicates = [x for x in set(my_list) if my_list.count(x) > 1]
print("Duplicate elements:", duplicates)
print()

my_list = [1, 2, 3, 2, 4, 1, 5]
unique_list = list(set(my_list))
print("List without duplicates:", unique_list)
print()

list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged_list = sorted(list1 + list2)
print("Merged sorted list:", merged_list)
print()

squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print("Squares of numbers 1 to 10:", squares)
print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even numbers:", even)
print("Odd numbers:", odd)




