from relatorio import Relatorio
from datetime import date
from reportlab.pdfgen import canvas

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY , TA_CENTER
from reportlab.lib.pagesizes import letter, inch, portrait
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch



class Leitor():
    def __init__ (self,arquivo, data,tipo = False):
        self.data = data
        self.tipo = tipo
        self.dados = []
        self.caminho = arquivo
        self.arquivo = open(self.caminho, 'r')
        


        self.doc = None
        self.Story = []
        self.logo = "Logo.png"
        self.magName = "Centro Regional de Porto Velho"
        self.formatted_time = date.today().strftime("%d/%m/%Y")
        self.full_name = "Centro Gestor do Sistema de Proteção da Amazônia"
        self.address_parts = ["Av. Lauro Sodré, 6500", " Aeroporto, Porto Velho - RO"]
        self.im = Image(self.logo, 1*inch, 1*inch)
        self.ptext = None
        self.styles=getSampleStyleSheet()
        self.styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        self.styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER,fontSize=15))


        self.colunas = ["TIMESTAMP - TS","RECORD - RN","TempAr - Smp","TempAr_Max - Max","TempAr_TMx - TMx","TempAr_Min - Min","TempAr_TMn - TMn","Umidade - Smp","Umidade_Max - Max","Umidade_TMx - TMx","Umidade_Min - Min","Umidade_TMn - TMn","PontoOrvalho - Smp","PontoOrvalho_Max - Max","PontoOrvalho_TMx - TMx","PontoOrvalho_Min - Min","PontoOrvalho_TMn - TMn","Pressao_Atm - Smp","Pressao_Atm_Max -Max","Pressao_Atm_TMx - TMx","Pressao_Atm_Min - Min","Pressao_Atm_TMn - TMn","VentoVel_WVc(1) - WVc","VentoVel_WVc(2) - WVc","VentoVel_WVc(3) - WVc","VentoVel_Max - Max","VentoVel_TMx - TMx","VentoDir_SMM - SMM","Radiacao_Avg - Avg","Chuva_Tot - Tot","NomeDaPCD - Smp","Bat_Min - Min","TempInterna_Max - Max","TempInterna_Min - Min "]


  

    def relatorioPadrao(self):


        self.doc = SimpleDocTemplate("Relatorio"+self.data+".pdf",pagesize=letter,
                                rightMargin=30,leftMargin=30,
                                topMargin=72,bottomMargin=18)

        self.Story.append(self.im)
        self.Story.append(Spacer(1, 12))
         
       
        self.ptext = '<font size=12>%s</font>' % self.formatted_time
         
        self.ptext = '<font size=12>Relatorio gerado no  %s \
                na data %s, neste relatório estão presentes os dados de %s \
                .</font>' % (self.magName,self.ptext,self.data)

        self.Story.append(Paragraph(self.ptext, self.styles["Justify"]))
        self.Story.append(Spacer(1, 12))      
        self.ptext = '<font size=12>%s</font>'%(self.full_name)
        self.Story.append(Paragraph(self.ptext, self.styles["Justify"]))
        self.ptext = '<font size=12>%s, %s</font>'%(self.address_parts[0],self.address_parts[1])
        self.Story.append(Paragraph(self.ptext, self.styles["Justify"]))
        self.Story.append(Spacer(1, 12))
        self.Story.append(Spacer(1, 12))

        






    def lerArquivoDia(self):
        self.relatorioPadrao()
        for linha in self.arquivo:
            try:
                filtro = linha.replace('"','').replace("\n","").split(',')
                filtro2 = filtro[0].split()
                if filtro2[0] == self.data:
                   x = len(filtro)
                   for i in range(x):
                       self.dados.append([self.colunas[i], filtro[i]])
                
                   
            except Exception as e:
                print(e)
        self.arquivo.close()
        t=Table(self.dados)
        t.setStyle(TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 1, colors.black),
                               ]))
        t._argW[1]=3.5*inch
        t._argW[0]=3.5*inch
        self.Story.append(t)
        self.doc.build(self.Story)


    def lerArquivoMes(self):
        texto=''
        self.relatorioPadrao()
        for linha in self.arquivo:
          
            filtro = linha.replace('"', '').replace("\n", "").split(',')
            filtro2 = filtro[0].split()
            count = 0
            try:
                if filtro2[0][5:7] == self.data[5:7] and filtro2[0][0:4] == self.data[0:4]:
                    for i in filtro:  
                        if count < len(self.colunas):   
                            if self.colunas[count] == "TIMESTAMP - TS":
                                self.Story.append(Spacer(1, 12)) 
                                self.Story.append(Paragraph(i,self.styles["Center"]))
                                self.Story.append(Spacer(1, 12))   

                            texto = self.colunas[count] +"      ->    "+ i
                            self.Story.append(Paragraph(texto,self.styles["Justify"]))
                            self.Story.append(Spacer(1, 12))

                            count+=1
                            
                        else:
                            count=0
                        
            except Exception as e:
                print(e)
        try:
            self.doc.build(self.Story) 
            self.arquivo.close()

        except Exception as e:

            print(e)
    