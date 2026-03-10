m = []
for x in range(1, 32001):
    a = 75 ** 314 + 75 ** 118 - x
    k = 0
    while a > 0:
        if a % 75 == 0:
            k += 1
        a = a // 75
    m.append(k)

print(min(m))

# задача №27295 
