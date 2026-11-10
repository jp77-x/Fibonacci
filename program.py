a, b = 0, 1
print(a)
print(b)

for i in range(1, 49):
    a, b = b, a + b # Python calcula el lado derecho primero y luego asigna ambos a la vez
    print(b)