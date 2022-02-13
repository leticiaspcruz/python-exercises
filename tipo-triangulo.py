#Faça um programa que determine qual é o tipo do triângulo a partir dos seus ângulos.
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