"""
Faça um programa que leia um caractere ‘F’ ou ‘C’, que indica se o próximo valor corresponde à temperatura em Fahrenheit ou Celsius. Em seguida, o programa deve ler o valor
da temperatura e então imprimir o valor correspondente à temperatura na outra unidade
de medida. Observação: (C = 5/9 × (F − 32))."""

def fahrenheit_to_celsius(value_in_fahrenheit):
    return 5 / 9 * (value_in_fahrenheit - 32)


def celsius_to_fahrenheit(value_in_celsius):
    return (value_in_celsius * 9 / 5) + 32


if __name__ == '__main__':
    unidade = ""
    while unidade != "C" and unidade != "F":
        unidade = input("Qual a unidade em grau, C ou F? ")

    value = int(input("Qual a temperatura? "))

    if unidade == "C":
        print(celsius_to_fahrenheit(value))
    else:
        print(fahrenheit_to_celsius(value))
