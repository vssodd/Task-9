N = int(input('Enter a number: '))

for depth in range(N, 0, -1):
    for length in range(N, 0, -1):
        if length >= depth:
            print(length, end='')
        else:
            print('.', end='')

    for length in range(1, N + 1):
        if length >= depth:
            print(length, end='')
        else:
            print('.', end='')
    print()
