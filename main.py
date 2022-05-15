from ast import Sub
from fpdf import FPDF
from datetime import date
import PySimpleGUI as sg

pdf_w = 215.9
pdf_h = 279.4

class PDF(FPDF):
    def Date_text(self):
        today = date.today()
        d1 = today.strftime("%m/%d/%Y")
        self.set_font('Arial', '', 12)
        self.cell(25, 25, 'La Estrella, '+d1)
        self.ln(20)

    def Greetings(self, cx):
        self.set_font('Arial', '', 12)
        self.cell(0, 0, "Señor(a)")
        self.ln(5)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 0, cx)
        self.ln(5)
        self.set_font('Arial', '', 12)
        self.cell(0, 0, "Cordial saludo.")
        self.ln(20)
        self.cell(0, 0, "De acuerdo con su solicitud adjunto la cotización: " )
        self.ln(20)

    def Add_part(self, pname, val):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 0, pname+": "+val)
        self.ln(20)
    
    def Add_tval(self, tval):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 0, "TOTAL: "+tval)
        self.ln(20)
    
    def Add_invtext(self, tent):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 0, "TIEMPO DE ENTREGA: "+tent+" dias despues de aprovada al cotización")
        self.ln(20)
        self.set_font('Arial', '', 12)
        self.cell(0, 0, "FORMA DE PAGO: 50% al recibir la aprobación y 50% al entregar el producto.")
        self.ln(20)
        self.multi_cell(0, 10, "OBSERVACION: La cotización puede variar un 20 % más por inconvenientes en la impresión. \n Quedo atento a sus comentarios.", 0, 'J')
        self.ln(20)

    def Contact(self):
        self.set_font('Arial', 'B', 12)
        self.multi_cell(0, 10, "Eddy Moncada Garcia \n Cel: 3137089201 \n e- mail: eddymoncadagarcia@gmail.com", 0, "J")



        

pdf=PDF(orientation='P', unit='mm', format='Letter')

sg.theme('DarkAmber')

layout = [
    [sg.Text("Script para crear PDF de cotización")],
    [sg.Text("Nombre del Cliente: "), sg.InputText()], 
    [sg.Text("Nombre de la Pieza: "), sg.InputText()], 
    [sg.Text("Peso (gr): "), sg.InputText()], 
    [sg.Text("Tiempo (hrs): "), sg.InputText()],
    [sg.Text("Pulido (min): "), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window("Invoice", layout)



while True:
    event, values = window.read()
    Vmat = int(values[2])*106
    Vtime = float(values[3])*300
    Vpul = int(values[4])*130
    Subtot = Vmat+Vtime+Vpul
    Tot = int(Subtot + (Subtot*0.5))
    Tim = float(values[3])
    Tent = int((Tim+(Tim*0.8))/12)
    pdf.add_page()
    pdf.Date_text()
    pdf.Greetings(str(values[0]))
    pdf.Add_part(str(values[1]), str(Tot))
    pdf.Add_tval(str(Tot))
    pdf.Add_invtext(str(Tent))
    pdf.Contact()
    pdf.output('COTIZACION.pdf','F')
    break

window.close()

