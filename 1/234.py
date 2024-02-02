# tested on 'gLGкlddАslsёlff'
def task_1(string):
    string = string.lower()
    # 1105 - letter 'ё' code
    return len(list(filter(lambda symb: True if ord(symb) in list(range(1072, 1103+1)) + [1105,] else False, list(string))))

# tested on 'kfk', 'kffk', 'kfgk'
# abdABdba
def task_9(string):
    for i in range(len(string)):
        # isalpha() - check Latin
        # if both symmetric letters are in uppercase or not Latin, it's ok
        if string[i] != string[-1 - i] and (string[i].islower() and string[i].isalpha() or string[-1 - i].islower() and string[-1 - i].islower()):
                return "nope"
    return "yup"

# tested on kfk31.03.2034gkgkfk36.05.2034gkgkfk02.12.2034gkg
# kfk31.03.2034gkgkfk36.05.2034gkgkfk02.12.20
# 1.03.2034gkgkfk36.05.2034gkgkfk02.12.2034kgk
def task_18(string):
    dates = []
    for month in ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"):
        index = string.find("." + month + ".")
        if index == -1:
            continue
        if string[index-2:index].isnumeric() and int(string[index-2:index]) < 32 and string[index+4:index+8].isnumeric() and len(string[index+4:index+8]) == 4:
            dates += [string[index-2:index+8]]
            string = string.replace(string[index-2:index+8], "")
    return dates

while True:
    task_num = input("Enter task num from (1, 9, 18) >> ")

    if task_num == "1":
        print(task_1(input("Enter string >> ")))
    elif task_num == "9":
        print(task_9(input("Enter string >> ")))
    elif task_num == "18":
        print(task_18(input("Enter string >> ")))