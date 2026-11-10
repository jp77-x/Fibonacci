def generar_fibonacci(limite):
    a, b = 0, 1
    print(a)
    print(b)

    for i in range(limite-2):
        a, b = b, a + b # Python calcula el lado derecho primero y luego asigna ambos a la vez
        print(b)

generar_fibonacci(5)