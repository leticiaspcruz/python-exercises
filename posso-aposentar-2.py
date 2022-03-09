"""
Suponha que uma pessoa possa se aposentar pelo INSS caso atenda alguma das situações abaixo:
• É do sexo masculino, possui pelo menos 65 anos e pelo menos 10 anos de contribuição.
• É do sexo masculino, possui pelo menos 63 anos e pelo menos 15 anos de contribuição.
• É do sexo feminino, possui pelo menos 63 anos e pelo menos 10 anos de contribuição.
• É do sexo feminino, possui pelo menos 61 anos e pelo menos 15 anos de contribuição.
Crie um programa que leia um caractere (M ou F), que representa o sexo de um indivíduo, e dois inteiros, que representam a idade e o tempo de contribuição. O programa
deverá então imprimir “Aposentável” se o indivíduo atenda uma das situações acima. Caso contrário, o programa deverá imprimir “Não Aposentável”."""
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


