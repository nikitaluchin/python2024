n = int(input("Enter amount of lines >> "))
lines = [input() for _ in range(n)]

# 6
# aa a aa aaa  
# aaaa
# a aaa
# aaa aa aa aa aa aaa
# aa 
# aaaa aa aaa
for i in range(n - 1):
    for j in range(i + 1, n):
        if len(lines[i].split()) > len(lines[j].split()):
            lines[i], lines[j] = lines[j], lines[i]

print(lines)