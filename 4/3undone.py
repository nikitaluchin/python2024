# оптимизированный черный список
# белый список нужен только ради пересечения
# оно должно их сортировать по порядку
# а затем составлять единый черный список опт-ый

f_input = open("3_4.txt")
f_output = open("3_out.txt", "w")
n = int(f_input.readline())

def encode_subnet(subnet):
    subnet = subnet[1:].split(".")
    subnet[-1] = subnet[-1].split("/")[0]
    subnet = list(map(int, subnet))
    return subnet[0] * 2 ** 24 + subnet[1] * 2 ** 16 + subnet[2] * 2 ** 8 + subnet[3]

def encode_list(list):
    encoded_list = set()
    for subnet in list:
        if subnet.find("/") != -1:
            x = int(subnet.split("/")[1])
            if x == 32:
                encoded_list.add(encode_subnet(subnet))
            else:
                encoded_list = encoded_list.union(set(range(encode_subnet(subnet), encode_subnet(subnet) + 2 ** (32 - x) - 1)))
        else:
            encoded_list.add(encode_subnet(subnet))
    return encoded_list

subnets = sorted([f_input.readline().rstrip() for _ in range(n)], key=encode_subnet)
whitelist = list(filter(lambda subnet: subnet[0] == "+", subnets))
blacklist = list(filter(lambda subnet: subnet[0] == "-", subnets))
print(whitelist, blacklist)
print(encode_list(whitelist))
print(encode_list(blacklist))

# в тексте указан пример:
# Например, подсеть 192.168.0.1/ 24 содержит диапазон из 256 адресов.
# 192.168.0.1 – первый адрес диапазона, а 192.168.0.255 – последний.
# >>> 192*2**24+168*2**16+255
# 3232235775
# print(sorted(list(encode_list(['+192.168.0.1/24']))))

wl_encoded = encode_list(whitelist)
bl_encoded = encode_list(blacklist)

if wl_encoded.intersection(bl_encoded):
    f_output.write("-1")
    exit(0)

