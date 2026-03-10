m = []
for x in range(1, 9430):
    a = 39 ** 483 + 39**235 - x
    k = 0
    while a > 0:
        if a % 39 == 0:
            k += 1
        a = a // 39
    m.append(k)

print(max(m))

# задача №27294 