#Faça um programa que determina se você pode se aposentar ou não.
if __name__ == 'main':
    sexo = input("sexo (M ou F): ")
    idade = int(input("idade: "))
    tempo = int(input("tempo: "))

    if sexo == "M" and idade >= 65 and tempo >= 10:
        print("Aposentável")
    elif sexo == "M" and idade >= 63 and tempo >= 15:
        print("Aposentável")
    elif sexo == "F" and idade >= 63 and tempo >= 10:
        print("Aposentável")
    elif sexo == "F" and idade >= 61 and tempo >= 15:
        print("Aposentável")
    else:
        print("Não Aposentável")

    print("Guardando o resultado em variável")
    aposentavel = False
    if sexo == "M":
        if idade >= 65 and tempo >= 10:
            aposentavel = True
        elif idade >= 63 and tempo >= 15:
            aposentavel = True
    else:
        if idade >= 63 and tempo >= 10:
            aposentavel = True
        elif idade >= 61 and tempo >= 15:
            aposentavel = True

    if aposentavel:
        print("Aposentável")
    else:
        print("não aposentável")

    print("Restringindo mais o if")

    if sexo == "M" and idade >= 65 and tempo >= 10:
        print("Aposentável")
    if sexo == "M" and 63 <= idade < 65 and tempo >= 15:
        print("Aposentável")
    if sexo == "F" and idade >= 63 and tempo >= 10:
        print("Aposentável")
    if sexo == "F" and 61 <= idade < 63 and tempo >= 15:
        print("Aposentável")


