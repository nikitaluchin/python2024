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

# 1 test
# for n in range(1, 30):
#     print(str(n) + ": " + str(sum_prime_divs(n)))

# 2
def count_odd_digits(num):
    return len([str(num)[i] for i in range(len(str(num))) if int(str(num)[i]) % 2 and int(str(num)[i]) > 3])

# 2 test
# print(count_odd_digits(123456789))

def digits_sum(num):
    return sum([int(str(num)[i]) for i in range(len(str(num)))])

# 3
def prod_divs(num):
    num_digits_sum = digits_sum(num)
    divs = [1]

    for div in range(2, num):
        if not num % div and digits_sum(div) < num_digits_sum:
            divs += [div]
    
    prod = 1
    for div in divs:
        prod *= div
    print(divs)
    return prod

# 3 test
print(prod_divs(23454))