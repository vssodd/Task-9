while True:
    n = int(input('Enter the number of integers: '))
    prime_count = 0
    for _ in range(n):
        num = int(input('Enter a number: '))
        is_prime = True
        for divisor in range(2, num):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime and num > 1:
            prime_count += 1
    print('Number of prime numbers in the sequence:', prime_count)
