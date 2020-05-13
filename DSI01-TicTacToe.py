from tkinter import *
from tkinter import messagebox
from Application import *
from Datenbank import *
from TicTacToePlayer import *
import time 

DEFAULTPLAYERNAME1 = "Player 1"
DEFAULTPLAYERCHAR1 = "X"
DEFAULTPLAYERNAME2 = "Player 2"
DEFAULTPLAYERCHAR2 = "O"


#region Function

def spielerEingabe():
    text = eingabe.get()

#Startet ein neues Spiel mit Messagebox Abfrage
def starteNeuesSpiel():
    wert = messagebox.askquestion('Neues Spiel?','Möchten sie ein neues Spiel beginnen?')
    if wert=='yes':
        spielFrame.grid_forget()
        spielFrame.grid(row=1)
        CreateNewGameGuiLayout()
        return TRUE
    else:
        return FALSE
    
#Checkbox die das verändern des Spielernamens und Zeichens von Spieler2 erlauben
def checkEnableSpielernameZwei():
    if checkboxSpielerZweiEnabled.get():
        eingabeSpielernameZwei.config(state='normal')
    else:
        eingabeSpielernameZwei.config(state='disabled')

#Wenn es keinen Gewinner gibt wird der Aktuelle Spieler gewechselt
def spielerWechselObjekt():
    global AktuellerSpielerObjekt,lblAktuellerSpielerName
    if pruefeGewinner():
        messagebox.showinfo("Gewinner!","Gewinner "+AktuellerSpielerObjekt.name+"!")
        return
    if AktuellerSpielerObjekt== TicTacToePlayer1:
        lblAktuellerSpielerName
        AktuellerSpielerObjekt=TicTacToePlayer2
        lblAktuellerSpielerName['text']=AktuellerSpielerObjekt.name
        #wert = messagebox.showinfo('Neues Spiel?','Switch1')
        return
    if AktuellerSpielerObjekt== TicTacToePlayer2:
        AktuellerSpielerObjekt=TicTacToePlayer1
        
        lblAktuellerSpielerName['text']=AktuellerSpielerObjekt.name
        #wert = messagebox.showinfo('Neues Spiel?','Switch2')
        return 

#prüft ob es einen Gewinner gibt
def pruefeGewinner():
    global lbl1,lbl2,lbl3,lbl4,lbl5,lbl6,lbl7,lbl8,lbl9
    if(AktuellerSpielerObjekt.char==lbl1['text'] and AktuellerSpielerObjekt.char == lbl2['text'] and AktuellerSpielerObjekt.char==lbl3['text']):
        return TRUE
    if(AktuellerSpielerObjekt.char==lbl4['text'] and AktuellerSpielerObjekt.char == lbl5['text'] and AktuellerSpielerObjekt.char==lbl6['text']):
        return TRUE
    if(AktuellerSpielerObjekt.char==lbl7['text'] and AktuellerSpielerObjekt.char == lbl8['text'] and AktuellerSpielerObjekt.char==lbl9['text']):
        return TRUE
    if(AktuellerSpielerObjekt.char==lbl1['text'] and AktuellerSpielerObjekt.char == lbl4['text'] and AktuellerSpielerObjekt.char==lbl7['text']):
        return TRUE
    if(AktuellerSpielerObjekt.char==lbl2['text'] and AktuellerSpielerObjekt.char == lbl5['text'] and AktuellerSpielerObjekt.char==lbl8['text']):
        return TRUE
    if(AktuellerSpielerObjekt.char==lbl3['text'] and AktuellerSpielerObjekt.char == lbl6['text'] and AktuellerSpielerObjekt.char==lbl9['text']):
        return TRUE
    if(AktuellerSpielerObjekt.char==lbl1['text'] and AktuellerSpielerObjekt.char == lbl5['text'] and AktuellerSpielerObjekt.char==lbl9['text']):
        return TRUE
    if(AktuellerSpielerObjekt.char==lbl3['text'] and AktuellerSpielerObjekt.char == lbl5['text'] and AktuellerSpielerObjekt.char==lbl7['text']):
        return TRUE
    return FALSE     

#Event für lbl1-lbl9
def mouseClickinEntry(event,widget):
    global lbl1,lbl2,lbl3,lbl4,lbl5,lbl6,lbl7,lbl8,lbl9
    
    #Spiel ist vorbei
    if(pruefeGewinner()):
        starteNeuesSpiel()
        return
    
    # Hier die Logik des Spiels einbauen :)
    if widget== 'lbl1':
        if lbl1['text']=="1":
            lbl1.config(text=AktuellerSpielerObjekt.char)
            spielerWechselObjekt()
        else:
            messagebox.showinfo("Feld besetzt!","Besetzt von "+AktuellerSpielerObjekt.name+"!")
        return
    if widget== 'lbl2':
        if lbl2['text']=="2":
            lbl2.config(text=AktuellerSpielerObjekt.char)
            spielerWechselObjekt()
        else:
            messagebox.showinfo("Feld besetzt!","Besetzt von "+AktuellerSpielerObjekt.name+"!")
        return
    if widget== 'lbl3':
        if lbl3['text']=="3":
            lbl3.config(text=AktuellerSpielerObjekt.char)
            spielerWechselObjekt()
        else:
            messagebox.showinfo("Feld besetzt!","Besetzt von "+AktuellerSpielerObjekt.name+"!")
        return
    if widget== 'lbl4':
        if lbl4['text']=="4":
            lbl4.config(text=AktuellerSpielerObjekt.char)
            spielerWechselObjekt()
        else:
            messagebox.showinfo("Feld besetzt!","Besetzt von "+AktuellerSpielerObjekt.name+"!")
        return
    if widget== 'lbl5':
        if lbl5['text']=="5":
            lbl5.config(text=AktuellerSpielerObjekt.char)
            spielerWechselObjekt()
        else:
            messagebox.showinfo("Feld besetzt!","Besetzt von "+AktuellerSpielerObjekt.name+"!")
        return
    if widget== 'lbl6':
        if lbl6['text']=="6":
            lbl6.config(text=AktuellerSpielerObjekt.char)
            spielerWechselObjekt()
        else:
            messagebox.showinfo("Feld besetzt!","Besetzt von "+AktuellerSpielerObjekt.name+"!")
        return
    if widget== 'lbl7':
        if lbl7['text']=="7":
            lbl7.config(text=AktuellerSpielerObjekt.char)
            spielerWechselObjekt()
        else:
            messagebox.showinfo("Feld besetzt!","Besetzt von "+AktuellerSpielerObjekt.name+"!")
        return
    if widget== 'lbl8':
        if lbl8['text']=="8":
            lbl8.config(text=AktuellerSpielerObjekt.char)
            spielerWechselObjekt()
        else:
            messagebox.showinfo("Feld besetzt!","Besetzt von "+AktuellerSpielerObjekt.name+"!")
        return
    if widget== 'lbl9':
        if lbl9['text']=="9":
            lbl9.config(text=AktuellerSpielerObjekt.char)
            spielerWechselObjekt()
        else:
            messagebox.showinfo("Feld besetzt!","Besetzt von "+AktuellerSpielerObjekt.name+"!")
        return
   
#Erstellt bei Programmstart, Nach Button Klick "Neues Spiel starten" und am Ende des Spiels ein neues Spielfeld
def CreateNewGameGuiLayout():
    global lbl1,lbl2,lbl3,lbl4,lbl5,lbl6,lbl7,lbl8,lbl9,spielFrame
    lbl1 = Label(spielFrame,text="1",bg="yellow",fg="blue",font=("Helvetica",32))
    lbl2 = Label(spielFrame,text="2",bg="yellow",fg="blue",font=("Helvetica",32))
    lbl3 = Label(spielFrame,text="3",bg="yellow",fg="blue",font=("Helvetica",32))
    lbl4 = Label(spielFrame,text="4",bg="yellow",fg="blue",font=("Helvetica",32))
    lbl5 = Label(spielFrame,text="5",bg="yellow",fg="blue",font=("Helvetica",32))
    lbl6 = Label(spielFrame,text="6",bg="yellow",fg="blue",font=("Helvetica",32))
    lbl7 = Label(spielFrame,text="7",bg="yellow",fg="blue",font=("Helvetica",32))
    lbl8 = Label(spielFrame,text="8",bg="yellow",fg="blue",font=("Helvetica",32))
    lbl9 = Label(spielFrame,text="9",bg="yellow",fg="blue",font=("Helvetica",32))

    lbl1.grid(row = 0, column = 0)
    lbl2.grid(row = 0, column = 1)
    lbl3.grid(row = 0, column = 2)
    lbl4.grid(row = 1, column = 0)
    lbl5.grid(row = 1, column = 1)
    lbl6.grid(row = 1, column = 2)
    lbl7.grid(row = 2, column = 0)
    lbl8.grid(row = 2, column = 1)
    lbl9.grid(row = 2, column = 2)

    lbl1.bind("<Button-1>", lambda event: mouseClickinEntry(event, "lbl1"))
    lbl2.bind("<Button-1>", lambda event: mouseClickinEntry(event, "lbl2"))
    lbl3.bind("<Button-1>", lambda event: mouseClickinEntry(event, "lbl3"))
    lbl4.bind("<Button-1>", lambda event: mouseClickinEntry(event, "lbl4"))
    lbl5.bind("<Button-1>", lambda event: mouseClickinEntry(event, "lbl5"))
    lbl6.bind("<Button-1>", lambda event: mouseClickinEntry(event, "lbl6"))
    lbl7.bind("<Button-1>", lambda event: mouseClickinEntry(event, "lbl7"))
    lbl8.bind("<Button-1>", lambda event: mouseClickinEntry(event, "lbl8"))
    lbl9.bind("<Button-1>", lambda event: mouseClickinEntry(event, "lbl9"))    

def CreateProgramStartLayout():
    global root,HeaderFrame,spielFrame,FooterFrame, AktuellerSpielerObjekt,lblAktuellerSpielerName,HeaderFrame,spielFrame,lblSpielername
    root = Tk()
    root.title("Tic Tac Toe v.1.0.0")
    HeaderFrame = Frame(root,width=300, height = 200)
    spielFrame = Frame(root,width=300, height = 500)
    HeaderFrame.grid(row=0)
    spielFrame.grid(row=1)
    lblSpielername = Label(HeaderFrame,text="Spielername eingeben",font=("Helvetica",12))
    lblSpielername.grid(row=0,column=0)
    eingabeSpielernameEins = Entry(HeaderFrame,font=("Helvetica",12),fg="red",width=10,textvariable=TicTacToePlayer1.name)
    eingabeSpielernameEins.insert(0,TicTacToePlayer1.name)
    eingabeSpielernameEins.grid(row=0,column=1)
    eingabeSpielerZeichenEins = Entry(HeaderFrame,font=("Helvetica",12),fg="red",width=10,textvariable=TicTacToePlayer1.char)
    eingabeSpielerZeichenEins.insert(0,TicTacToePlayer1.char)
    eingabeSpielerZeichenEins.grid(row=0,column=2)
    eingabeSpielernameZwei = Entry(HeaderFrame,font=("Helvetica",12),fg="red",width=10,state='normal',textvariable=TicTacToePlayer2.name)
    eingabeSpielernameZwei.insert(END,TicTacToePlayer2.name)
    eingabeSpielernameZwei.grid(row=1,column=1)
    eingabeSpielerZeichenZwei = Entry(HeaderFrame,font=("Helvetica",12),fg="red",width=10,textvariable=TicTacToePlayer2.char)
    eingabeSpielerZeichenZwei.insert(END,TicTacToePlayer2.char)
    eingabeSpielernameZwei.config(state='disabled')
    eingabeSpielerZeichenZwei.config(state='disabled')
    eingabeSpielerZeichenZwei.grid(row=1,column=2)

    #Variable um checkbox status zu checken
    checkboxSpielerZweiEnabled = IntVar()
    checkpielerZwei = Checkbutton(HeaderFrame,text="Spieler 2 aktivieren",font=("Helvetica",12),command=checkEnableSpielernameZwei, variable=checkboxSpielerZweiEnabled)
    checkpielerZwei.grid(row=1,column=0)

    btnSpielStarten = Button(HeaderFrame,text="Spiel beginnen",font=("Helvetica",12),command=starteNeuesSpiel)
    btnSpielStarten.grid(row=2,column=0)


    
    


#endregion

TicTacToePlayer1 = TicTacToePlayer(DEFAULTPLAYERNAME1,DEFAULTPLAYERCHAR1)
TicTacToePlayer2 = TicTacToePlayer(DEFAULTPLAYERNAME2,DEFAULTPLAYERCHAR2)
AktuellerSpielerObjekt = TicTacToePlayer1

CreateProgramStartLayout()

CreateNewGameGuiLayout()
app=Application(master=root)
app.mainloop()


#res = db=DB()
#app=Application(master=root)
#w = Label(root, text="Tic Tac Toe!")
#w.pack()
#button1 = Button(root, text = "Klick mich an").place(x=20,y=30,width = 100, height = 100)
#btnTime =  Button(root,text="1",bg="yellow",fg="blue",font=("Helvetica",32), command=aktion)
#btnTime.pack()

#resuuuult = db.schreibeDB("a","b")
#result = db.leseDB()


