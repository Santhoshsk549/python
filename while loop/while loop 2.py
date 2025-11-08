num = 48293
sum_even = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        sum_even += digit
    num //= 10

print("Sum of even digits:", sum_even)
