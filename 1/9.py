n = int(input("Enter amount of lines >> "))
lines = [input() for i in range(n)]

# 6 lines
# 11
# 1111
# 1 
# 111111
# 111
# 111111
for i in range(n - 1):
    for j in range(i + 1, n):
        if len(lines[i]) > len(lines[j]):
            lines[i], lines[j] = lines[j], lines[i]

print(lines)
