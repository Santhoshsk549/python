#1
l1=(10,20,30,40,50,60,70)
l2=list(l1)
l2[0]=23
print(l2)
print(tuple(l2))
print()
#2
print(len(l1))
print()

#3
print(tuple(sorted(l1)))
print()
#4
tuple1=(1,True,"santhosh",[1,2,3],(10,5))
print(tuple1)
for item in tuple1:
    print(item)
    print(type(item))
print()
#5
(a,b,c,d,e,f,g)=l1
print("value:",c)
print()

string1=("python")
string2=("program")
add=string1+string2
print(add)
print()
#6
s=('s','a','n','t','h','o','s','h')
t=''.join(s)
print(t)
print()

t1=(100,200,300,400,500,600,700)
print(t1[3],t1[-4])
