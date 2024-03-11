a = eval(input("Digite o lado 1: \n"))
b = eval(input("Digite o lado 2: \n"))
c = eval(input("Digite o lado 3: \n"))

maior_lado = max(a, b, c)

if maior_lado < a + b + c -maior_lado:
    print('Os lados formam um triângulo! ')
    if a == b and b == c and a == c:
        print('Triangulo equilátero')
    elif a != b and b != c and a !=c:
        print('Triângulo escaleno')
    else:
        print('Triângulo isósceles')
else:
    print('Os lados nao formam um trângulo')