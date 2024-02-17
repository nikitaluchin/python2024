# в 2.txt для теста добавь в конец сначала ')', затем '(' 
f = open("2.txt")
num_opened = 0
for line in list(map(lambda line: line.rstrip(), f.readlines())):
    for symb in line:
        if symb == ")":
            if not num_opened:
                print("Incorrect")
                exit(0)
            num_opened -= 1
        elif symb == "(":
            num_opened += 1
if num_opened:
    print("Incorrect")
else:
    print("Correct")