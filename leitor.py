def lerArquivoDia(data):
    arquivo = open('arquivo.txt', 'r')
    selecionado = []
    for linha in arquivo:
        try:
            filtro = linha.replace('"','').replace("\n","").split(',')
            filtro2 = filtro[0].split()
            if filtro2[0] == data:
               print (filtro)
               print("\n")
            
        except:
            pass
    arquivo.close()


def lerArquivoMes(mes,ano):
    arquivo = open('arquivo.txt', 'r')
    selecionado = []
    for linha in arquivo:
        try:
            filtro = linha.replace('"', '').replace("\n", "").split(',')
            filtro2 = filtro[0].split()
            if filtro2[0][5:7] == mes and filtro2[0][0:4] == ano:
                print (filtro)
                print("\n")

        except:
            pass
    arquivo.close()


data = input("Digite a Data: ")
lerArquivoDia(data)
mes = input("Digite o Mês: ")
ano = input("Digite o Ano: ")
lerArquivoMes(mes,ano)
