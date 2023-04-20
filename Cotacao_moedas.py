import requests
from tkinter import *
from tkinter import ttk

# Cores
cor1 = "#feffff" # white/branca
cor2='#02c292'   # Azul
fundo = "#000000" # black/preta

# Funções

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    
    requisicao_dic = requisicao.json()
    
    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    
    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''
    
    texto_cotacoes['text'] = texto
    
janela = Tk()
janela.title("Cotação Atual das Moedas")
janela.geometry("405x300")
janela.config(bg=fundo)

# Frames

frame_tela = Frame(janela, width=235, height=50)
frame_tela.grid(column=0, row=0)

frame_corpo = Frame(janela, width=405, height=275)
frame_corpo.grid(column=0, row=1)

# Texto inicial

texto_orientacao = Label(frame_tela, text="Clique no botão para ver as cotações das moedas:", height=3, bg=cor2, fg=fundo, font=('Ivy','13','bold'), relief=RAISED)
texto_orientacao.grid(column=0, row=0)

#  Botão

botao = Button(frame_corpo, text="Buscar cotações", command=pegar_cotacoes, width=15, height=2, bg=cor2, fg=fundo, font=('Ivy','13','bold'), relief=RAISED, overrelief=RIDGE)
botao.place(x=125,y=35)

# Resultado

texto_cotacoes = Label(frame_corpo, text="", fg=fundo, font=('Ivy','13','bold'))
texto_cotacoes.place(x=130,y=100)

janela.mainloop()

# Faz a função mais simples 

# Texto inicial

#texto_orientacao = Label(janela, text="Clique no botão para ver as cotações das moedas:")
#texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

#  Botão

#botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
#botao.grid(column=0, row=1)

# Resultado

#texto_cotacoes = Label(janela, text="")
#texto_cotacoes.grid(column=0, row=2)