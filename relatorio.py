from datetime import date
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY , TA_CENTER
from reportlab.lib.pagesizes import letter, inch, portrait
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
class Relatorio(object):
     """docstring for Relatorio"""
     def __init__(self, data,tempo):
        self.data = data
        
        self.tempo = tempo
        doc = SimpleDocTemplate("form_letter.pdf",pagesize=letter,
                                rightMargin=30,leftMargin=30,
                                topMargin=72,bottomMargin=18)
        Story=[]
        logo = "Logo.png"
        magName = "Centro Regional de Porto Velho"





        formatted_time = date.today().strftime("%d/%m/%Y")
        full_name = "Centro Gestor do Sistema de Proteção da Amazônia"
        address_parts = ["Av. Lauro Sodré, 6500", " Aeroporto, Porto Velho - RO"]
         
        im = Image(logo, 1*inch, 1*inch)
        Story.append(im)
        Story.append(Spacer(1, 12))
         
        styles=getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
        ptext = '<font size=12>%s</font>' % formatted_time
         
        #Story.append(Paragraph(ptext, styles["Normal"]))
        #Story.append(Spacer(1, 12))
         
        # Create return address
        #ptext = '<font size=12>%s</font>' % full_name
        #Story.append(Paragraph(ptext, styles["Normal"]))


        #for part in address_parts:
        #    ptext = '<font size=12>%s</font>' % part.strip()
        #    Story.append(Paragraph(ptext, styles["Normal"]))
         
        #Story.append(Spacer(1, 12))
        #ptext = '<font size=12>Caro(a) %s:</font>' % full_name.split()[0].strip()
        #Story.append(Paragraph(ptext, styles["Normal"]))
        #Story.append(Spacer(1, 12))

        ptext = '<font size=12>Relatorio gerado no  %s \
                na data %s, neste relatório estão presentes os dados de %s \
                .</font>' % (magName,ptext,self.tempo)

        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
         

        


        ptext = '<font size=12>%s</font>'%(full_name)
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size=12>%s, %s</font>'%(address_parts[0],address_parts[1])
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ptext = '<font size=12>%s</font>'% self.tempo
        Story.append(Paragraph(ptext, styles["Center"]))
        Story.append(Spacer(1, 12))

        t=Table(self.data)
        t.setStyle(TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 1, colors.black),
                               ]))
        t._argW[1]=3.5*inch
        t._argW[0]=3.5*inch
        Story.append(t)
        # write the document to disk
        doc.build(Story)
        print("DEU")
