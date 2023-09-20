from tkinter import *
from tkinter import filedialog
import qrcode

###### Cores #####

preto ='#000000'
cinza ='#4F4F4F'
cinza_escuro ='#1C1C1C'
prata='#C0C0C0'

#Variavel para Salvar os Arquivos

SALVAR_ARQUIVOS = []

##### Iniciando APP ####

app = Tk()
app.title('')
app.geometry('1200x450')
app.configure(bg=cinza)
app.resizable(width=False,height=False)

#### Criando os Frames ####

frame_esquerda = Frame(app,width=670, height=800, bg=cinza, padx=0, relief='flat', border='20')
frame_esquerda.grid(row=1,column=0)

frame_direta = Frame(app,width=680,height=800,bg=cinza_escuro,padx=0,relief=FLAT,border=-4)
frame_direta.grid(row=1,column=1)

#### Função para Salvar os Arquivos ####

def Salvar_Arquivos():
    salvar_arquivos = filedialog.askdirectory()
    SALVAR_ARQUIVOS = salvar_arquivos

    salvar_text['text']=f'{SALVAR_ARQUIVOS}'

    nome_qrcode = Label(frame_esquerda, text='Nome do Qrcode', font='Time 10 ', border=4)
    nome_qrcode.place(y=130, x=-2)

    nome_qrcode_inserir = Entry(frame_esquerda, border=4, bd='2', width=20, font='Time 10')
    nome_qrcode_inserir.place(y=130, x=150)

    def Gerar_QRCode():

        caminho = salvar_arquivos
        nome = nome_qrcode_inserir.get()

        code = url_inserir.get()

        qr = qrcode.make(code)
        qr.save(f'{caminho}/{nome}.png')

        imagem_label = PhotoImage(file=f'{caminho}/{nome}.png')

        label = Label(frame_direta,image=imagem_label).place(x=10,y=2)
        label.pack()

    botao_gerar = Button(frame_esquerda, text='QRCODE', command=Gerar_QRCode, background='white', font='Time 15 ',
                         border=6)
    botao_gerar.place(y=200, x=300)


#### Inserindo as Labels ####

url= Label(frame_esquerda,text='Digite seu QRCode:', compound=LEFT, relief=FLAT,bg=cinza, anchor='center', border=10,font='Time 10 ',background='white',borderwidth=10)
url.place(y=10, x=-2)

url_inserir = Entry(frame_esquerda, width=40, bd='2',bg='white',border=5)
url_inserir.place(y=14, x=140)

salvar = Button(frame_esquerda, text='SALVAR', command=Salvar_Arquivos, background='white',font='Time 10',border=4)
salvar.place(y=70, x=-2)

salvar_text = Label(frame_esquerda,text='',border=2)
salvar_text.place(y=72, x=70)


app.mainloop()

