# tested on 'gLGкlddАslsёlff'
def task_1(string):
    string = string.lower()
    # 1105 - letter 'ё' code
    return len(list(filter(lambda symb: True if ord(symb) in list(range(1072, 1103+1)) + [1105,] else False, list(string))))

# tested on 'kfk', 'kffk', 'kfgk'
def task_9(string):
    for i in range(len(string)):
        if string[i] != string[-1 - i]:
            return "nope"
    return "yup"


while True:
    task_num = input("Enter task num from (1, 9, 18) >> ")

    if task_num == "1":
        print(task_1(input("Enter string >> ")))
    elif task_num == "9":
        print(task_9(input("Enter string >> ")))
    elif task_num == "18":
        print(task_18(input("Enter string >> ")))