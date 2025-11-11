#8
rep=(22,44,55,44,22,66)
for i in rep:
    if rep.count(i)>1:
        print(i)

print()
#9
print(55 in rep)
print()
#10
list=[0,1,2,3]
print(tuple(list))
print()
#11

t=(1,2,3,4,5,6)
for j in t:
    if j !=3:
        print(j)
print()
#12
print(t[1:3])
print()
#13
print(t.index(4))
print()
#14

print(len(t))
print()
#15
print(t[::-1])
print()
#16

string_list=["sam","roshan","nas"]
print(tuple(string_list))
