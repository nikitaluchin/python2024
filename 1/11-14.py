from math import sqrt

def count_diff(line):
    vowels_amount, consonants_amount = 0, 0

    for symb in line:
        if symb.lower().isalpha():
            if symb.lower() in ('a', 'e', 'i', 'o', 'u', 'y'):
                vowels_amount += 1
            else:
                consonants_amount += 1
    return abs(vowels_amount - consonants_amount)

# tested on
# aaaaff
# aaf    
# ffff
def task_1():
    n = int(input("Enter amount of lines >> "))
    lines = [input() for i in range(n)]
    # print(list(map(count_diff, lines)))

    for i in range(n - 1):
        for j in range(i + 1, n):
            if count_diff(lines[i]) > count_diff(lines[j]):
                lines[i], lines[j] = lines[j], lines[i]
    return lines

# sd = sqrt(1/n * Σi=1,n (xi-\overline{x})^2),
# \overline{x} = 1/n * Σi=1,n (xi), where xi - ASCII code
# tested on
# fjfj ld djdjls
# abafk flff
# gkgkg nanas
def task_4():
    n = int(input("Enter amount of lines >> "))
    lines = [input() for i in range(n)]
    avg = (1/len(lines[0])) * sum([ord(lines[0][i]) for i in range(len(lines[0]))])
    # print(avg)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if sqrt((1/len(lines[i])) * sum([(ord(lines[i][k]) - avg) ** 2 for k in range(len(lines[i]))])) \
               > sqrt((1/len(lines[j])) * sum([(ord(lines[j][k]) - avg) ** 2 for k in range(len(lines[j]))])):
                lines[i], lines[j] = lines[j], lines[i]
                # print(sqrt((1/len(lines[i])) * sum([(ord(lines[i][k]) - avg) ** 2 for k in range(len(lines[i]))])))
    return lines

def get_max_avg(line):
    return max([1/3 * (ord(line[i]) + ord(line[i+1]) + ord(line[i+2])) for i in range(len(line) - 2)])

# tested on
# fjfj ld djdjls
# abafk flff
# gkgkg nanas
def task_8():
    n = int(input("Enter amount of lines >> "))
    lines = [input() for i in range(n)]

    for i in range(n - 1):
        for j in range(i + 1, n):
            if sqrt((1/len(lines[i])) * sum([(ord(lines[i][k]) - get_max_avg(lines[i])) ** 2 for k in range(len(lines[i]))])) \
               > sqrt((1/len(lines[j])) * sum([(ord(lines[j][k]) - get_max_avg(lines[j])) ** 2 for k in range(len(lines[j]))])):
                lines[i], lines[j] = lines[j], lines[i]
                # print(sqrt((1/len(lines[i])) * sum([(ord(lines[i][k]) - get_max_avg(lines[i])) ** 2 for k in range(len(lines[i]))])))
    return lines

# tested on
# hdaa aaad dk
# fh aa aa kaaa
# fjk aaa kka
def task_12():
    n = int(input("Enter amount of lines >> "))
    lines = [input() for i in range(n)]
    # был использован метод строк count(), прошу заметить (см. в нижний цикл)
    symbols_freqs = {}

    for line in lines:
        for symb in line:
            if symb in symbols_freqs:
                symbols_freqs[symb] += 1
            else:
                symbols_freqs[symb] = 1
    freqs = list(symbols_freqs.values())
    symbols = list(symbols_freqs.keys())
    mx = [max(freqs) / n, symbols[freqs.index(max(freqs))]]
    # print(mx)

    for i in range(n - 1):
        for j in range(i + 1, n):
            # sqrt((xi - x)^2) = abs(xi - x)
            if abs(lines[i].count(mx[1]) - mx[0]) > abs(lines[j].count(mx[1]) - mx[0]):
                lines[i], lines[j] = lines[j], lines[i]
    return lines

while True:
    task_num = input("Enter task num from (1, 4, 8, 12) >> ")

    if task_num == "1":
        print(task_1())
    elif task_num == "4":
        print(task_4())
    elif task_num == "8":
        print(task_8())
    elif task_num == "12":
        print(task_12())