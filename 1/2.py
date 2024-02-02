# tested on 'gLGкlddАslsёlff'
def task_1(string):
    string = string.lower()
    # 1105 - letter 'ё' code
    print(len(list(filter(lambda symb: True if ord(symb) in list(range(1072, 1103+1)) + [1105,] else False, list(string)))))


while True:
    task_num = input("Enter task num from (1, 9, 18) >> ")

    if task_num == "1":
        task_1(input("Enter string >> "))
    elif task_num == "9":
        task_9()
    elif task_num == "18":
        task_18()