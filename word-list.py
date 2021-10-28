print("\nEsse algoritmo vai concatenar o nome da pessoa e todas as combinações de dias e meses, antes e depois do nome dela,"
    " por exemplo \'0510Joao\' \n\n")

nome = input("Digite o nome da pessoa:")

arquivo = open('word-list.txt', 'w')

for c in range(1, 13, +1):
    for i in range(1, 32, +1):

        numtxt1 = str(i)
        numtxt2 = str(c)

        if (c < 10):
            numtxt2 = (f"0{c}")
        if (i < 10):
            numtxt1 = (f"0{i}")

        txtNumFinal1 = str(f"{numtxt1}{numtxt2}{nome}\n")#nome depois maiusculo
        txtNumFinal2 = str(f"{numtxt1}{numtxt2}{nome}\n")#nome depois minusculo

        txtNumFinal3 = str(f"{nome}{numtxt1}{numtxt2}\n")#nome antes maiusculo
        txtNumFinal4 = str(f"{nome}{numtxt1}{numtxt2}\n")#nome antes minusculo

        arquivo.write(txtNumFinal1)
        arquivo.write(txtNumFinal2)
        arquivo.write(txtNumFinal3)
        arquivo.write(txtNumFinal4)

arquivo.close()
