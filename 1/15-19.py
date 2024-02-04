def task_7(l):
    for _ in range(2):
        l_copy = l.copy()
        for i in range(len(l)):
            l[i] = l_copy[i - 1]
    return l

def task_19(l):
    l_copy = l.copy()
    for i in range(len(l)):
        l[i] = l_copy[i - 1]
    return l

def task_31(l):
    return len(list(filter(lambda el: True if el % 2 == 0 else False, l)))

    # count = 0
    # for el in l:
    #     if el % 2 == 0:
    #         count += 1
    # return count

def task_43(l):
    return l.count(min(l))

while True:
    task_num = input("Enter task num from (7, 19, 31, 43, 55) >> ")

    if task_num == "7":
        print(task_7([1,2,3,4,5]))
    elif task_num == "19":
        print(task_19([1,2,3,4,5]))
    elif task_num == "31":
        print(task_31([1,2,3,4,5]))
    elif task_num == "43":
        print(task_43([1,3,6,1,7,1,8,1]))
    elif task_num == "55":
        print(task_55())