from math import sqrt, ceil

def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True

    for div in range(2, num):
        if not num % div and num != div:
            return False
    return True

# 1
def sum_prime_divs(num):
    if num == 2:
        return 2
    divs = [] if not is_prime(num) else [num]

    for div in range(2, num):
        if not num % div and is_prime(div):
            divs += [div]
    # return divs
    return sum(divs)

for n in range(1, 30):
    print(str(n) + ": " + str(sum_prime_divs(n)))