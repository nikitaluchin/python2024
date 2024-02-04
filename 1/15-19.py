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

while True:
    task_num = input("Enter task num from (7, 19, 31, 43, 55) >> ")

    if task_num == "7":
        print(task_7([1,2,3,4,5]))
    elif task_num == "19":
        print(task_19([1,2,3,4,5]))
    elif task_num == "31":
        print(task_31())
    elif task_num == "43":
        print(task_43())
    elif task_num == "55":
        print(task_55())