# tested on fhf4747ghgj833jffj7575758
# 8448
# jfffj
# fhf4747ghgj833jffj
# fffjf45.88fkk45.89
# 45.88fjfjfk45.87jdjd
def task_1(string):
    flag = False
    num = ""

    for symb in string:
        if symb.isdecimal():
            num += symb
        elif symb == ".":
            if num:
                if num[-1] == ".":
                    mx = max(mx, float(num[:-1]))
                    num = "" 
                else:
                    num += symb
            else:
                continue
        elif flag and num:
            mx = max(mx, float(num))
            num = ""
        elif num:
            mx = float(num)
            flag = True
            num = ""
    if flag and num:
        mx = max(mx, float(num))
    elif not flag:
        if num:
            return float(num)
        return "There're no numbers"
    return mx

# tested on fhf4747ghgj833jffj7575758
# 8448
# jfffj
# fhf4747ghgj833jffj
# fffjf45.88fkk45.89
# 45.88fjfjfk45.87jdjd
# 45.88fjfjfk45.87
# 45.88fjfjfk
def task_9(string):
    flag = False
    num = ""

    for symb in string:
        if symb.isdecimal():
            num += symb
        elif symb == ".":
            if num:
                if num[-1] == ".":
                    mn = min(mn, float(num[:-1]))
                    num = "" 
                else:
                    num += symb
            else:
                continue
        elif flag and num:
            mn = min(mn, float(num))
            num = ""
        elif num:
            mn = float(num)
            flag = True
            num = ""
    if flag and num:
        mn = min(mn, float(num))
    elif not flag:
        if num:
            return float(num)
        return "There're no numbers"
    return mn


while True:
    task_num = input("Enter task num from (1, 9, 18) >> ")

    if task_num == "1":
        print(task_1(input("Enter string >> ")))
    elif task_num == "9":
        print(task_9(input("Enter string >> ")))
    elif task_num == "18":
        print(task_18(input("Enter string >> ")))