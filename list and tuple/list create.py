l=["Apple","banana","grapes","watermelon","mango"]
print("created list",l)

print()

l.append("staberry")
print("added:",l)
print()

l.remove("staberry")
print("removed:",l)

print()

print("count of fruits:",len(l))
print()


print("fruits one by one:")
for l in l:
    print(l)

l=["Apple","banana","grapes","watermelon","mango"]
l.reverse()
print("reversed list:",l)
print()

l=["Apple","banana","grapes","watermelon","mango"]
l.sort()
print(l)
print()

l=["Apple","banana","grapes","watermelon","mango"]
if "mango" in l:
    print("yes,the fruits in :",l)
else:
    print("no,the fruits in :",l)
