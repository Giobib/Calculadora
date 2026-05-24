from tkinter import*
from tkinter import ttk

# CORES
roxo_escuro = '#3d0a49'
roxo_claro = '#5015bd'
azul_escuro = '#027fe9'
azul_claro = '#00caf8'
branco = '#e0daf7'
fonte = 'Arial 25 bold'

janela = Tk()
janela.title("Calculadora")
janela.geometry("480x705")
janela.config(bg=roxo_escuro)

#frames de fundo

frame_tela = Frame(janela, width=480, height=120, bg=roxo_escuro)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=480, height=585, bg=branco)
frame_corpo.grid(row=1, column=0)

#LÓGICA

todos_valores = ''
valor_texto = StringVar()

# LÓGICA

todos_valores = ''
valor_texto = StringVar()
resultado_mostrado = False  # ← flag nova

def entrada(event):
    global todos_valores, resultado_mostrado

    # Se acabou de calcular e o usuário digita um número, começa do zero
    # Se digitar um operador, continua usando o resultado anterior
    if resultado_mostrado:
        if str(event) in '0123456789.':
            todos_valores = str(event)   # ← substitui em vez de acrescentar
        else:
            todos_valores = todos_valores + str(event)  # ← continua com o resultado
        resultado_mostrado = False
    else:
        todos_valores = todos_valores + str(event)

    valor_texto.set(todos_valores)

def calcular():
    global todos_valores, resultado_mostrado

    resultado = eval(todos_valores)
    todos_valores = str(resultado)   # ← guarda o resultado como base
    valor_texto.set(todos_valores)
    resultado_mostrado = True        # ← ativa a flag

def limpar_tela():
    global todos_valores, resultado_mostrado

    todos_valores = ''
    resultado_mostrado = False       # ← reseta a flag
    valor_texto.set('')


#label

app_label = Label(frame_tela, textvariable=valor_texto, width=23, height=3, relief=FLAT, padx=8, anchor="e", justify=RIGHT, font=(fonte), bg=roxo_escuro, fg='#fff')
app_label.place(x=0, y=0)

#botoes (b)

#  0  % /
# 7 8 9 *
# 4 5 6 -
# 1 2 3 +
#  0  . =

#1º row ( 0  % / )

b_1 = Button(frame_corpo, command= limpar_tela, text='C', width=12, height=3, bg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, command= lambda: entrada('%'),text='%', width=6, height=3, bg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_2.place(x=240, y=0)

b_3 = Button(frame_corpo, command= lambda: entrada('/'), text='/', width=6, height=3, bg=azul_escuro, fg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_3.place(x=360, y=0)

#2º row ( 7 8 9 * )

b_4 = Button(frame_corpo, command= lambda: entrada('7'), text='7', width=6, height=3, bg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=120)

b_5 = Button(frame_corpo, command= lambda: entrada('8'), text='8', width=6, height=3, bg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_5.place(x=120, y=120)

b_6 = Button(frame_corpo, command= lambda: entrada('9'), text='9', width=6, height=3, bg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_6.place(x=240, y=120)

b_7 = Button(frame_corpo, command= lambda: entrada('*'), text='*', width=6, height=3, bg=azul_escuro, fg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_7.place(x=360, y=120)

#3º row ( 4 5 6 - )

b_8 = Button(frame_corpo, command= lambda: entrada('4'), text='4', width=6, height=3, bg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=240)

b_9 = Button(frame_corpo, command= lambda: entrada('5'), text='5', width=6, height=3, bg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_9.place(x=120, y=240)

b_10 = Button(frame_corpo, command= lambda: entrada('6'), text='6', width=6, height=3, bg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_10.place(x=240, y=240)

b_11 = Button(frame_corpo, command= lambda: entrada('-'), text='-', width=6, height=3, bg=azul_escuro, fg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_11.place(x=360, y=240)

#4º row ( 1 2 3 + )

b_12 = Button(frame_corpo, command= lambda: entrada('1'), text='1', width=6, height=3, bg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=360)

b_13 = Button(frame_corpo, command= lambda: entrada('2'), text='2', width=6, height=3, bg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_13.place(x=120, y=360)

b_14 = Button(frame_corpo, command= lambda: entrada('3'), text='3', width=6, height=3, bg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_14.place(x=240, y=360)

b_15 = Button(frame_corpo, command= lambda: entrada('+'), text='+', width=6, height=3, bg=azul_escuro, fg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_15.place(x=360, y=360)

#5º row ( 0 . = )

b_16 = Button(frame_corpo, command= lambda: entrada('0'), text='0', width=12, height=2, bg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=480)

b_17 = Button(frame_corpo, command= lambda: entrada('.'), text='.', width=6, height=2, bg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_17.place(x=240, y=480)

b_18 = Button(frame_corpo, command = calcular, text='=', width=6, height=2, bg=azul_escuro, fg=branco, font=(fonte), relief=RAISED, overrelief=RIDGE)
b_18.place(x=360, y=480)

entrada('')

janela.mainloop()