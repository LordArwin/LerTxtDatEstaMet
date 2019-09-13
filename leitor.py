from datetime import date
from reportlab.pdfgen import canvas
import xlwt
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
        self.worksheet = None
        self.workbook = None



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

            
#####################################################33
            ###########################################################3
                    ###################################################################333
                            #############################################################################3333
            
    def coletaDados(self):
        row = 1
        texto = "erro"
        tempMin = None
        tempMax = None
        umiMax = None
        umiMin = None
        presMin = None
        presMax = None
        tempMed = 0
        vezes = 0
        prep = 0
        presMed = 0
        vezesPres = 0
        umiMed = 0
        vezesUmi=0
        ventoDir= None
        rad=0
        maxVento = None
        vezesVento=0
        mediaVento=0

        

        n =0
        ne=0
        e=0
        se=0
        s=0
        so=0
        o=0
        no=0        
        
        for linha in self.arquivo:
          
            filtro = linha.replace('"', '').replace("\n", "").split(',')
            filtro2 = filtro[0].split()
            count = 0
            
            textIgual = True
            
            try:
                if filtro2[0][5:7] == self.data[5:7] and filtro2[0][0:4] == self.data[0:4]:
                    for i in filtro:  
                        if count < len(self.colunas):
                            

                            if self.colunas[count] == "TIMESTAMP - TS":
                                #data
                                if texto != i.split()[0]:
                                    texto = i.split()[0]
                                    textIgual = False
                                    self.worksheet.write(row, 0, label = '{}'.format(texto))
                                    row +=1
                                    tempMin = None
                                    tempMax = None
                                    umiMax=None
                                    umiMin = None
                                    presMin = None
                                    presMax = None
                                    tempMed= 0
                                    vezes = 0
                                    prep = 0
                                    presMed=0
                                    vezesPres=0
                                    umiMed = 0
                                    vezesUmi=0
                                    ventoDir = None
                                    rad = 0
                                    maxVento = None
                                    vezesVento=0
                                    mediaVento=0



                                    n =0
                                    ne=0
                                    e=0
                                    se=0
                                    s=0
                                    so=0
                                    o=0
                                    no=0



                                   
                                else:
                                    textIgual = True
                                
                            if self.colunas[count] == "TempAr_Min - Min" and textIgual == True:

                                try:
                                    if i != "NAN":
                                        tempMed += float(i)
                                        vezes +=1
                                    pass
                                except:
                                    pass
                                if i == "NAN":
                                    tempMin = None
                                elif tempMin == None:
                                    tempMin = float(i)
                                elif tempMin > float(i):
                                    tempMin = float(i)
                                
                                


                                self.worksheet.write(row-1, 9, label = '{}'.format(tempMin))

                            ############################################

                            if self.colunas[count] == "VentoDir_SMM - SMM" and textIgual == True:
                        
                               
                                try:
                                    
                                    if float(i) >= 0 and float(i)  <=22.5:
                                        n +=1
                                    elif float(i)  >=22.6 and float(i)  <=67.5:
                                        ne +=1
                                    elif float(i)  >= 67.6 and float(i)  <=122.5:
                                        e+=1
                                    elif float(i)  >= 122.6 and float(i)  <= 157.5:
                                        se +=1
                                    elif float(i)  >= 157.6 and float(i)  <= 202.5:
                                        s +=1
                                    elif float(i)  >= 202.6 and float(i) <= 247.5:
                                        so +=1
                                    elif float(i)  >=247.6 and float(i)  <=292.5:
                                        o +=1
                                    elif float(i)  >= 292.6 and float(i)  <= 337.5:
                                        no +=1
                                    elif float(i)  >= 337.6 and float(i)  <= 360:
                                        n +=1

                                    if n > ne and n>e and n>se and n>s and n>so and n>o and n>no:
                                        ventoDir = "N"
                                    elif ne > n and ne>e and ne>se and ne>s and ne>so and ne>o and ne>no:
                                        ventoDir = "NE"
                                    elif e > ne and e> n and e >se and e > s and e > so and e > o and e > no:
                                        ventoDir = "E"
                                    elif se > ne and se >e and se > n and se > s and se > so and se > o and se > no:
                                        ventoDir = "SE"
                                    elif s > ne and s>e and s>se and s>n and s>so and s>o and s>no:
                                        ventoDir = "S"
                                    elif so > ne and so>e and so>se and so>s and so>n and so>o and so>no:
                                        ventoDir = "SO"
                                    elif o > ne and o>e and o>se and o>s and o>so and o>n and o>no:
                                        ventoDir = "O"
                                    elif no > ne and no>e and no>se and no>s and no>so and no>o and no>n:
                                        ventoDir = "NO"

                                except:
                                    pass                            

                                self.worksheet.write(row-1, 5, label = '{}'.format(ventoDir))



                                #######################
                            if self.colunas[count] == "TempAr_Max - Max" and textIgual == True:
                                try:
                                    if i != "NAN":
                                        tempMed += float(i)
                                        vezes +=1
                                    pass
                                except:
                                    pass
                                if i == "NAN":
                                    tempMax = None
                                elif tempMax == None:
                                    tempMax = float(i)
                                elif tempMax < float(i):
                                    tempMax = float(i)
                                


                                self.worksheet.write(row-1, 9, label = '{}'.format(tempMax))


                                ###################################333
                               
                            if self.colunas[count] == "Umidade_Max - Max" and textIgual == True:
                                try:
                                    if i != "NAN":
                                        umiMed += float(i)
                                        vezesUmi +=1
                                    pass
                                except:
                                    pass

                                
                                if i == "NAN":
                                    umiMax = None
                                elif umiMax  == None :
                                    umiMax  = float(i)
                                elif umiMax  < float(i) :
                                    umiMax  = float(i)
                                


                                self.worksheet.write(row-1, 6, label = '{}'.format(umiMax ))

                                ################3
                            if self.colunas[count] == "Umidade_Min - Min" and textIgual == True:
                                try:
                                    if i != "NAN":
                                        umiMed += float(i)
                                        vezesUmi +=1
                                
                                    pass
                                except:
                                    pass
                                
                                if i == "NAN":
                                    umiMin = None
                                elif umiMin == None :
                                    umiMin = float(i)
                                elif umiMin > float(i):
                                    umiMin = float(i)
                                


                                self.worksheet.write(row-1, 7, label = '{}'.format(umiMin))

                                ####################3
                            
                            if self.colunas[count] == "Pressao_Atm_Min - Min" and textIgual == True:
                                try:
                                    if i != "NAN":
                                        presMed += float(i)
                                        vezesPres +=1
                                    pass
                                except:
                                    pass

                                
                                if i == "NAN":
                                    presMin = None
                                elif presMin == None:
                                    presMin = float(i)
                                elif presMin > float(i):
                                    presMin = float(i)
                                


                                self.worksheet.write(row-1, 13, label = '{}'.format(presMin))

                                ########################

                            if self.colunas[count] == "Pressao_Atm_Max -Max" and textIgual == True:
                                try:
                                    if i != "NAN":
                                        presMed += float(i)
                                        vezesPres +=1
                                    pass
                                except:
                                    pass

                                
                                
                                if i == "NAN":
                                    presMax = None
                                elif presMax  == None:
                                    presMax  = float(i)
                                elif presMax  < float(i):
                                    presMax  = float(i)
                                


                                self.worksheet.write(row-1, 12, label = '{}'.format(presMax ))


                            if self.colunas[count] == "Chuva_Tot - Tot" and textIgual == True:

                                if i == "NAN":
                                    i = 0
                                try:
                                    prep +=float(i)
                                except:
                                    pass
                                


                                self.worksheet.write(row-1, 1, label = '{:.2f}'.format(prep))




                            if self.colunas[count] == "Radiacao_Avg - Avg" and textIgual == True:

                                if i == "NAN":
                                    i = 0
                                try:
                                    rad +=float(i)
                                except:
                                    pass
                                


                                self.worksheet.write(row-1, 15, label = '{:.2f}'.format(rad))




                            if self.colunas[count] == "VentoVel_Max - Max" and textIgual == True:
                                try:
                                    if i != "NAN":
                                        mediaVento += float(i)
                                        vezesVento +=1
                                    pass
                                except:
                                    pass
                                if i == "NAN":
                                    maxVento = None
                                elif maxVento == None:
                                    maxVento = float(i)
                                elif maxVento < float(i):
                                    maxVento = float(i)
                                


                                self.worksheet.write(row-1, 2, label = '{}'.format(maxVento))




                            



                            



                            try:
                                self.worksheet.write(row-1, 3, label = '{:.2f}'.format(float(mediaVento/vezesVento)))
                                self.worksheet.write(row-1, 4, label = '{:.2f}'.format(float(mediaVento)))
                                self.worksheet.write(row-1, 14, label = '{:.2f}'.format(float(presMed/vezesPres)))
                                self.worksheet.write(row-1,8, label = '{:.2f}'.format(float(umiMed/vezesUmi)))
                                self.worksheet.write(row-1, 11, label = '{:.2f}'.format(float(tempMed/vezes)))
                            except:
                                pass


                            count+=1

                            
                            
                        else:
                            count=0
                        
            except Exception as e:
                pass




    def escreverXls(self):
        try:
            
            c = xlwt.Style.easyxf('font: bold on; align: horiz center;align:vert centre;pattern: pattern solid;')
            c.pattern.pattern_fore_colour = 7
            c.alignment.wrap = 1
            
            self.workbook = xlwt.Workbook()
            self.worksheet = self.workbook.add_sheet(u'Dados',cell_overwrite_ok=True)
            self.worksheet.row(0).height_mismatch = True
            self.worksheet.row(0).height = 256 * 2

            self.worksheet.col(0).width = 256 * 15            
            self.worksheet.col(1).width = 256 * 15
            self.worksheet.col(2).width = 256 * 15
            self.worksheet.col(3).width = 256 * 15
            self.worksheet.col(4).width = 256 * 15
            self.worksheet.col(5).width = 256 * 15
            self.worksheet.col(6).width = 256 * 15
            self.worksheet.col(7).width = 256 * 10
            self.worksheet.col(8).width = 256 * 10
            self.worksheet.col(9).width = 256 * 10
            self.worksheet.col(10).width = 256 * 15
            self.worksheet.col(11).width = 256 * 15
            self.worksheet.col(12).width = 256 * 15
            self.worksheet.col(13).width = 256 * 15
            self.worksheet.col(14).width = 256 * 15
            self.worksheet.col(15).width = 256 * 15

             
            self.worksheet.write(0, 0, label = 'Dia',style = c)
            self.worksheet.write(0, 1, label = 'Precipitação',style = c)
            self.worksheet.write(0, 2, label = 'Vel. Vento(MAX)',style = c)
            self.worksheet.write(0, 3, label = 'Vel. Vento(MEDIA)',style = c)
            self.worksheet.write(0, 4, label = 'Vel. Vento(TOTAL)',style = c)
            self.worksheet.write(0, 5, label = 'Dir. Vento',style = c)
            self.worksheet.write(0, 6, label = 'Umid. Relat. AR (Max) %',style = c)
            self.worksheet.write(0, 7, label = 'Umid. Relat. AR (Min) %',style = c)
            self.worksheet.write(0, 8, label = 'Umid. Relat. AR (Média)%',style = c)
            self.worksheet.write(0, 9, label = 'Temp. Max. ºC Dia',style = c)
            self.worksheet.write(0, 10, label = 'Temp. Min. ºC Dia',style = c)
            self.worksheet.write(0, 11, label = 'Temp. Med. ºC do Ar',style = c)
            self.worksheet.write(0, 12, label = 'Pressão Atm. Max',style = c)
            self.worksheet.write(0, 13, label = 'Pressão Atm. Min',style = c)
            self.worksheet.write(0, 14, label = 'Pressão Atm. Med',style = c)
            self.worksheet.write(0, 15, label = 'Radiação AVG',style = c)

            self.coletaDados()
            self.workbook.save('planilha.xls')

        except  Exception as e:
            print(e)

            
    
