# f = open("1ex.txt")
# f = open("27-124a.txt")
f = open("27-124b.txt")
N, K, V, M = list(map(int, f.readline().split()))
packages = [0] * K

for _ in range(N):
    km, post = list(map(int, f.readline().split()))
    # если km = K, то km % K будет 0
    packages[km % K] = post // V + (post % V > 0)

mx = sum(packages)
# если M >= K // 2, то можем доставить во все дома
if M < K // 2:
    # разместим отеделение на километре с номером M
    # т.е. отступаем влево и вправо на M, т.о. суммируем до M*2 + 1
    sum_packages = sum(packages[:M*2 + 1])
    # если тут есть дом, то можем разместить отделение, иначе не можем
    mx = sum_packages if packages[M] else 0

    for i in range(1, K):
        # смещаем границу, обновляются при этом левая и правая границы для суммы (если они ненулевые)
        # если дом есть, обновим максимум
        sum_packages += packages[(i + M * 2) % K] - packages[i - 1]
        if packages[(i + M) % K]:
            mx = max(mx, sum_packages)
print(mx)