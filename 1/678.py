# tested on fhf4747ghgj833jffj7575758
# 8448
# jfffj
# fhf4747ghgj833jffj
def task_1(string):
    flag = False
    num = ""

    for symb in string:
        if symb.isdecimal():
            num += symb
        elif flag and num:
            mx = max(mx, int(num))
            num = ""
        elif num:
            mx = int(num)
            flag = True
            num = ""
    if flag and num:
        mx = max(mx, int(num))
    elif not flag:
        if num:
            return num
        return "There're no numbers"
    return mx


while True:
    task_num = input("Enter task num from (1, 9, 18) >> ")

    if task_num == "1":
        print(task_1(input("Enter string >> ")))
    elif task_num == "9":
        print(task_9(input("Enter string >> ")))
    elif task_num == "18":
        print(task_18(input("Enter string >> ")))