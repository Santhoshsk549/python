num = 12321
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if num == rev:
    print("Palindrome number")
else:
    print("Not a palindrome")
