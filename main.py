from tkinter import messagebox
import tkinter as tk
import tkinter.ttk
from tkinter import Canvas
from tkinter import PhotoImage
import pyodbc

# Funcionalidades
dadosconnect = "Driver={SQL Server};Server=DESKTOP-AB1DE95;Database=BDCatalogo;"
connection = pyodbc.connect(dadosconnect)
cursor = connection.cursor()


def adicionar():
    if len(EntNome.get()) < 1 or len(EntIdade.get()) < 0 or len(EntJog.get()) < 0 or len(EntEdit.get()) < 0:
        messagebox.showerror(
            "Erro 2",
            'Preencha todos os campos')
        return

    cursor.execute(f'''
    INSERT INTO 
        Catalogo (
        Nome,
        Idade,
        Jogadores,
        Editora,
        Obs)
    VALUES(
        '{EntNome.get().strip().upper()}',
        '{EntIdade.get().strip().upper()}',
        '{EntJog.get().strip().upper()}',
        '{EntEdit.get().strip().upper()}',
        '{EntDesc.get(
            '1.0',
            'end')}')''')
    cursor.commit()


def limpar():
    EntId.delete(
        '0',
        'end')
    EntNome.delete(
        '0',
        'end')
    EntIdade.delete(
        '0',
        'end')
    EntJog.delete(
        '0',
        'end')
    EntEdit.delete(
        '0',
        'end')
    EntDesc.delete(
        '1.0',
        'end')


def deletar():
    if len(EntId.get()) < 0:
        messagebox.showerror(
            "Erro 1",
            'Adicione o Id do jogo...')
        return

    cursor.execute(f'''
    DELETE FROM 
        Catalogo 
    WHERE 
        Id='{EntId.get()}' ''')
    cursor.commit()


def procurar():
    if len(EntId.get()) < 0:
        messagebox.showerror(
            "Erro 1",
            'Adicione o Id do jogo...')
        return

    cursor.execute(f'''
    SELECT 
        Id,
        Nome,
        Idade,
        Jogadores,
        Editora,
        Obs        
    FROM 
        Catalogo 
    WHERE
        Id='{EntId.get()}' OR
        Nome='{EntNome.get().strip().upper()}' 
    ''')
    busca = cursor.fetchone()
    EntId.delete(
        '0',
        'end')
    EntNome.delete(
        '0',
        'end')
    EntIdade.delete(
        '0',
        'end')
    EntJog.delete(
        '0',
        'end')
    EntEdit.delete(
        '0',
        'end')
    EntDesc.delete(
        '1.0',
        'end')
    EntId.insert(
        0,
        '{}'.format(busca[0]))
    EntNome.insert(
        0,
        '{}'.format(busca[1]))
    EntIdade.insert(
        0,
        '{} ANOS'.format(busca[2]))
    EntJog.insert(
        0,
        '{} JOGADORES'.format(busca[3]))
    EntEdit.insert(
            0,
            '{}'.format(busca[4]))
    EntDesc.insert(
        '1.0',
        '{}'.format(busca[5]))


def jan2():
    global Bg3, BtFech, tree
    janela2 = tk.Toplevel()
    janela2.title('Catálogo de Boardgames')
    janela2.geometry("750x500")
    janela2.configure(bg="#9a1818")
    canvas1 = Canvas(
        janela2,
        bg="#9a1818",
        height=700,
        width=600,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas1.place(
        x=0,
        y=0)
    janela2.resizable(
        True,
        True)
    Bg3 = PhotoImage(file='CatTT/Bg3.png')
    canvas1.create_image(
        350,
        250,
        image=Bg3)

    BtFech = PhotoImage(file='CatTT/BtFech.png')
    btfech = tk.Button(
        janela2,
        image=BtFech,
        command=janela2.destroy)
    btfech.place(
        x=590,
        y=430)
    # TREE
    tree = tkinter.ttk.Treeview(
        janela2,
        columns=[
            '0',
            '1',
            '2',
            '3',
            '4'],
        show='headings')

    tree.column(
        '0',
        width=5)
    tree.column(
        '1',
        width=120)
    tree.column(
        '2',
        width=80)
    tree.column(
        '3',
        width=80)
    tree.column(
        '4',
        width=100)
    tree.heading(
        '0',
        text='Id')
    tree.heading(
        '1',
        text='Nome')
    tree.heading(
        '2',
        text='Classificação Etária')
    tree.heading(
        '3',
        text='Número de Jogadores')
    tree.heading(
        '4',
        text='Editora')
    tree.place(
        x=135,
        y=80,
        width=600,
        height=325)

    busca2 = cursor.execute('''
    SELECT 
        *
    FROM 
        Catalogo
    ORDER BY 
        Nome''')
    a = cursor.fetchall()
    cursor.commit()
    for row in a:
        tree.insert("", tk.END, values=(row[0],
                                        row[1],
                                        row[2],
                                        row[3],
                                        row[4]))


# Interface gráfica
# Janela 1
janela = tk.Tk()
janela.title('Catálogo de Boardgames')
janela.geometry("750x500")
janela.configure(bg="#9a1818")
canvas = Canvas(
    janela,
    bg="#9a1818",
    height=700,
    width=600,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(
    x=0,
    y=0)
janela.resizable(
    False,
    False)

Bg2 = PhotoImage(file='CATALOGO/Bg2.png')
canvas.create_image(
    350,
    250,
    image=Bg2)

# Entradas
EntId = tk.Entry()
EntId.place(
    x=160,
    y=70,
    width=50,
    height=30)

EntNome = tk.Entry()
EntNome.place(
    x=280,
    y=70,
    width=430,
    height=30)

EntIdade = tk.Entry()
EntIdade.place(
    x=160,
    y=110,
    width=550,
    height=30)

EntJog = tk.Entry()
EntJog.place(
    x=160,
    y=150,
    width=550,
    height=30)

EntEdit = tk.Entry()
EntEdit.place(
    x=160,
    y=190,
    width=550,
    height=30)

EntDesc = tk.Text()
EntDesc.place(
    x=160,
    y=230,
    width=550,
    height=170)

# Botões
BtAdicionar = PhotoImage(file='CATALOGO/BtAdicionar.png')
btAdicionar = tk.Button(
    image=BtAdicionar,
    command=adicionar)
btAdicionar.place(
    x=160,
    y=430)

BtProcurar = PhotoImage(file='CATALOGO/BtProcurar.png')
btProcurar = tk.Button(
    image=BtProcurar,
    command=procurar)
btProcurar.place(
    x=310,
    y=430)

BtDeletar = PhotoImage(file='CATALOGO/BtDeletar.png')
btDeletar = tk.Button(
    image=BtDeletar,
    command=deletar)
btDeletar.place(
    x=460,
    y=430)

BtLimpar = PhotoImage(file='CATALOGO/BtLimpar.png')
btLimpar = tk.Button(
    image=BtLimpar,
    command=limpar)
btLimpar.place(
    x=610,
    y=430)

BtCol = PhotoImage(file='CATALOGO/BtCat.png')
btCol = tk.Button(
    image=BtCol,
    command=jan2)
btCol.place(
    x=20,
    y=398)

janela.mainloop()

# Fechamento
connection.close()
cursor.close()
