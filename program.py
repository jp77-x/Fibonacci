a = 0
b = 1

print(a)
print(b)

for i in range(1, 49):
    siguiente = a + b
    print(siguiente)

    a = b
    b = siguiente

