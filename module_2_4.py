numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
    if num == 1:
        print("1 не является не простым и не сложным числом")

    elif num < 4:
        primes.append(num)
        print(f'число {num} - простое')

    elif num % 2 == 0:
        not_primes.append(num)
        print(f'число {num} - составное')
    else:

        for div in range(3, int(num**0.5) + 1, 2):
            if num % div == 0:
                not_primes.append(num)
                print(f'число {num} - составное')
                break
        else:
            primes.append(num)
            print(f'число {num} - простое')

print(f'{primes = }')
print(f'{not_primes = }')

    # 36
    #
    # 2   18
    # 3   12
    # 4   9
    # 6   6
