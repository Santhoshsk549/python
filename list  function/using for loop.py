new_list= [100, 200, 300, 400, 500]
for num in new_list:
    print(num)
print()


print("sum of the element",sum(new_list))
print()

print("min of the element",min(new_list))
print("max of the element",max(new_list))
print()


numbers = [10, 200, 200, 30, 40, 50, 200]
print("200 appears:", numbers.count(200), "times")
print()

print("index of 400",new_list.index(400))
print()

new_list.reverse()
print("reverse of list",new_list)
print()


num1 = [500, 200, 400, 100, 300]
num1.sort()
print("Ascending:", num1)
num1.sort(reverse=True)
print("Descending:", num1)
print()

copy_list=new_list.copy()
print("copy the list",copy_list)
print()

list = [100, 177, 200, 299, 300, 333]
for num in list:
    if num % 2 == 0:
        print("even number:",num)
print()



for num in list:
    if num % 2 != 0:
        print("odd number:",num)
print()
