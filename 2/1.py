file = open("1.txt")
n = int(file.readline())
line = [file.readline().split(), file.readline().rstrip("\n")]
nums = set()
not_nums = set()
# print(line)


while line[0][0] != "HELP":
    if line[1] == "YES":
        nums = nums.intersection(set(line[0])) if nums else set(line[0])
    else:
        not_nums = not_nums.union(set(line[0]))
        nums = nums.difference(not_nums)
    
    line = [file.readline().split(), file.readline().rstrip("\n")]

print(*sorted(nums))