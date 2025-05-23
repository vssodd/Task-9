N = int(input('Enter a number: '))

for number in range(1, N + 1):
    for _ in range(number):
        print(number, end='\t')
    print()
