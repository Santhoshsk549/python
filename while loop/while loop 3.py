num = 12345
count = 0

while num > 0:
    count += 1
    num //= 10

print("Total digits:", count)
