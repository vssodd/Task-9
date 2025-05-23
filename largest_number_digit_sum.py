N = int(input('Enter the number of numbers: '))
max_number = 0
max_digit_sum = 0

for _ in range(N):
    num = int(input('Enter a number: '))
    if num > max_number:
        max_number = num
        max_digit_sum = 0
    digit_sum = 0
    temp_num = num
    while temp_num > 0:
        digit_sum += temp_num % 10
        temp_num //= 10
    if num == max_number:
        max_digit_sum += digit_sum

print('The largest number entered:', max_number)
print('Sum of its digits:', max_digit_sum)
