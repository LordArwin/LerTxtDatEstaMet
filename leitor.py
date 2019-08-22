from relatorio import Relatorio
class Leitor(object):
    def __init__ (self,arquivo, data,tipo = False):
        self.data = data
        self.tipo = tipo
        self.caminho = arquivo
        
        self.colunas = ["TIMESTAMP - TS","RECORD - RN","TempAr - Smp","TempAr_Max - Max","TempAr_TMx - TMx","TempAr_Min - Min","TempAr_TMn - TMn","Umidade - Smp","Umidade_Max - Max","Umidade_TMx - TMx","Umidade_Min - Min","Umidade_TMn - TMn","PontoOrvalho - Smp","PontoOrvalho_Max - Max","PontoOrvalho_TMx - TMx","PontoOrvalho_Min - Min","PontoOrvalho_TMn - TMn","Pressao_Atm - Smp","Pressao_Atm_Max -Max","Pressao_Atm_TMx - TMx","Pressao_Atm_Min - Min","Pressao_Atm_TMn - TMn","VentoVel_WVc(1) - WVc","VentoVel_WVc(2) - WVc","VentoVel_WVc(3) - WVc","VentoVel_Max - Max","VentoVel_TMx - TMx","VentoDir_SMM - SMM","Radiacao_Avg - Avg","Chuva_Tot - Tot","NomeDaPCD - Smp","Bat_Min - Min","TempInterna_Max - Max","TempInterna_Min - Min "]

        self.dataDividida = []





    def lerArquivoDia(self):
        arquivo = open(self.caminho, 'r')
        selecionado = []
        data = []
        for linha in arquivo:
            try:
                filtro = linha.replace('"','').replace("\n","").split(',')
                filtro2 = filtro[0].split()
                if filtro2[0] == self.data:
                   print('')
                   x = len(filtro)
                   for i in range(x):
                    data.append([self.colunas[i], filtro[i]])

                   
                   for c in data:
                        print(c[0])  

                   r = Relatorio(data,self.data)
            except:
                pass

        arquivo.close()


    def lerArquivoMes(self):
        arquivo = open('arquivo.txt', 'r')
        selecionado = []
        for linha in arquivo:
            try:
                filtro = linha.replace('"', '').replace("\n", "").split(',')
                filtro2 = filtro[0].split()
                if filtro2[0][5:7] == self.data[5:7] and filtro2[0][0:4] == self.data[0:4]:
                    print (filtro)
                    print("\n")

            except:
                pass
        arquivo.close()
