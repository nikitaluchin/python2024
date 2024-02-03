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
    print(list(map(count_diff, lines)))

    for i in range(n - 1):
        for j in range(i + 1, n):
            if count_diff(lines[i]) > count_diff(lines[j]):
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