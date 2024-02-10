file = open("2.txt")
n = int(file.readline())
cities = {}

for _ in range(n):
    line = file.readline().split()
    # print(line)
    for city in line[1:]:
        cities[city] = line[0]

m = int(file.readline())

for _ in range(m):
    city = file.readline().rstrip("\n")
    print(cities[city])