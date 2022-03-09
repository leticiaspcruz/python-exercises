"""
Suponha que uma pessoa possa se aposentar pelo INSS caso atenda alguma das situações abaixo:
• É do sexo masculino, possui pelo menos 65 anos e pelo menos 10 anos de contribuição.
• É do sexo masculino, possui pelo menos 63 anos e pelo menos 15 anos de contribuição.
• É do sexo feminino, possui pelo menos 63 anos e pelo menos 10 anos de contribuição.
• É do sexo feminino, possui pelo menos 61 anos e pelo menos 15 anos de contribuição.
Crie um programa que leia um caractere (M ou F), que representa o sexo de um indivíduo, e dois inteiros, que representam a idade e o tempo de contribuição. O programa
deverá então imprimir “Aposentável” se o indivíduo atenda uma das situações acima. Caso contrário, o programa deverá imprimir “Não Aposentável”."""

if __name__ == '__main__':
    sexo = input("digite o sexo (M/F): ")
    idade = int(input("digite a idade: "))
    tempo = int(input("digite o tempo: "))
    if sexo == "F":
        if idade >= 63 and tempo >= 10:
            print("Aposentável")
        elif idade >= 61 and tempo >= 15:
            print("Aposentável")
        else:
            print("Não Aposentável")
    elif sexo == "M":
        if idade >= 65 and tempo >= 10:
            print("Aposentável")
        elif idade >= 63 and tempo >= 15:
            print("Aposentável")
        else:
            print("Não Aposentável")
    else:
        print("Não-binários não aposentam no Brasil")

