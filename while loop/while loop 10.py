num = 123
sum_squares = 0

while num > 0:
    digit = num % 10
    sum_squares += digit ** 2
    num //= 10

print("Sum of squares of digits:", sum_squares)
