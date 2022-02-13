#Faça um programa que leia dois valores inteiros nas variáveis x e y e troque o conteúdo das variáveis.
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