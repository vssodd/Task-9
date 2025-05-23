N = int(input('Enter the number of pyramid levels: '))
number = 1

for row in range(1, N + 1):
    print('\t' * (N - row), end='')
    for col in range(row):
        print(number, end='')
        number += 2
        if col < row - 1:
            print('\t' * 2, end='')
    print()
