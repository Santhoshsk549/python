new_list=[100,150,200,250,300,350,400,450,500]
print("list",new_list)
print("list length:",len(new_list))
print()

print("positive index:",new_list[0])
print("negative index:",new_list[-1])
print()

new_list[3]=280
print("list",new_list)
print("update list",new_list)
print()

del new_list[3]
print("after del",new_list)
print()

new_list.append(550)
print("using append",new_list)
print()

new_list.insert(3,250)
print("using insert",new_list)
print()

new_list.remove(550)
print("remove the element",new_list)
print()

new_list.pop()
print("pop the element",new_list)
print()

new_list.clear()
print("clear the element",new_list)
print()
