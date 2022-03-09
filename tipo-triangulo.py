"""
Faça um programa que leia os valores correspondentes aos três lados a, b e c de um triângulo. O programa então deve determinar se o triângulo é isósceles, escaleno ou equilátero,
informando isto para o usuário, e em seguida o programa deve imprimir a área A do
triângulo utilizando a fórmula de Heron."""

if __name__ == '__main__':
    a = int(input("digite a: "))
    b = int(input("digite b: "))
    c = int(input("digite c: "))
    if a == b or b == c or c == a:
        print("é isósceles")
    if a != b and b != c and c != a:
        print("é escaleno")
    if a == b and b == c and c == a:
        print("é equilatero")
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print(area)