#Faça um programa que determina se você pode se aposentar ou não.
if __name__ == '__main__':
    sexo = input("digite o sexo (M/F): ")
    idade = int(input("digite a idade: "))
    tempo = int(input("digite o tempo: "))
    if sexo == "F":
        if idade >= 63 and tempo >= 10:
            print("pode se aposentar")
        elif idade >= 61 and tempo >= 15:
            print("pode se aposentar")
        else:
            print("não pode se aposentar")
    elif sexo == "M":
        if idade >= 65 and tempo >= 10:
            print("pode se aposentar")
        elif idade >= 63 and tempo >= 15:
            print("pode se aposentar")
        else:
            print("não pode se aposentar")
    else:
        print("não-binários não aposentam no brasil")

