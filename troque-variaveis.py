"""Faça um programa que leia dois valores inteiros nas variáveis x e y e troque o conteúdo
das variáveis. Por exemplo, supondo que x = 2 e y = 10 foram os valores lidos, o seu
programa deve fazer com que x = 10 e y = 2. Refaça este problema usando apenas x e y
como variáveis."""

def parte1():
    x = int(input("digite x: "))
    y = int(input("digite y: "))
    aux = x
    x = y
    y = aux
    print(x)
    print(y)

def parte2():
    x = int(input("digite x: "))
    y = int(input("digite y: "))
    x = x + y
    print('x+y',x)
    y = x - y
    print('x+y-y',y)
    x = x - y
    print('x+y-x+y-y',x)
    print('-------')
    print(x)
    print(y)

if __name__ == '__main__':
    parte1()
    parte2()