num=int(input("Enter the number :"))
if num%2== 0:
    print("Even number")
else:
    print("odd number")



num=int(input("Enter the number :"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")


mark = int(input("Enter marks: "))
if mark >= 90:
    print("Grade A")
elif mark >= 75:
    print("Grade B")
elif mark >= 50:
    print("Grade C")
else:
    print("Fail")


year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print(f"Not eligible. Wait {18 - age} more years.")

a, b, c = 10, 25, 15

if a >= b and a >= c:
    print("a is largest")
elif b >= a and b >= c:
    print("b is largest")
else:
    print("c is largest")


num = int(input("Enter number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    print("Negative or Zero")


age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")


ch = input("Enter a letter: ").lower()

if ch in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")


m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))

if m1 >= 40 and m2 >= 40 and m3 >= 40:
    print("Pass")
else:
    print("Fail")
\






