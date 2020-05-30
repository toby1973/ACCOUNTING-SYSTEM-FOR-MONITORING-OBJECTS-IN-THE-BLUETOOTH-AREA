from tkinter import *
import tkinter.font
from tkinter import messagebox
import mysql.connector
import datetime
from tkinter import ttk
import re
#from GUI import mydb

# uzregistruoti pasiimta BLE
mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        passwd="laukas12",
        database="BLE"
        )

def DIBLE():

    DIL = Toplevel()  # sukuriamas pagrindinis langas uzregistruoti pasiimta langas
    DIL.title('Darbuotoju irasai')
    DIL.geometry("500x450")
    
    global irasyti_l
    irasyti_l = Label(DIL)
    
    global VT, PT, EPL, DVT
    global VT_L, PT_L, EPL_L, DVT_L, DVT_LF
    VT_L = Label(DIL)
    PT_L = Label(DIL) 
    EPL_L = Label(DIL)
    DVT_L = Label(DIL)
    #DVT_LF = Label(DIL)
    
    def tikrinti():
        
        global VT, PT, EPL, DVT
        VT = PT = EPL = DVT = False
        
        global VT_L, PT_L, EPL_L, DVT_L
        global irasyti_l
        VT_L.destroy()
        PT_L.destroy()
        EPL_L.destroy()
        DVT_L.destroy()
        irasyti_l.destroy
        
        VT_L = Label(DIL, text= "Neirasitas darbuotojo vardas", fg="red")
        PT_L = Label(DIL, text= "Neirasita darbuotojo pavardė", fg="red")
        EPL_L = Label(DIL, text= "Neirasita darbuotojo elektroninis pastas", fg="red")
        DVT_L = Label(DIL, text= "Neirasita Darbuotojo darbo vieta", fg="red")
        
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        
        if len(Vardas.get()) == 0 or Vardas.get().isnumeric():
            VT_L.grid(row=10, column=0,columnspan=2)
        else :
            VT = True
        if len(Pavarde.get()) == 0 or Pavarde.get().isnumeric(): 
            PT_L.grid(row=11, column=0, columnspan=2)
        else :
            PT = True
        if len(Epastas.get()) > 0 and re.search(regex,Epastas.get()):
            EPL = True
        else :
            EPL_L.grid(row=12, column=0,columnspan=2)
        if len(DarboVieta.get()) == 0 or DarboVieta.get().isnumeric():
            DVT_L.grid(row=13, column=0, columnspan=2)
        else :
            DVT = True
            
        if VT and PT and EPL and DVT == True:
            irasyti()
            
            
     # iraso duomenis i duomenu baze
    def irasyti():
        global VT_L, PT_L, EPL_L, DVT_L
        global irasyti_l
        VT_L.destroy()
        PT_L.destroy()
        EPL_L.destroy()
        DVT_L.destroy()
        irasyti_l.destroy
        V = Vardas.get()
        P = Pavarde.get()
        EP = Epastas.get()
        DV = DarboVieta.get()
       
        
        irasyti_l = Label(DIL, fg="green" ,text="Duomenis irasyti")
        cursor = mydb.cursor()
        cursor.execute("Insert INTO Darbuotojai (Vardas, Pavarde, Elektroninispastas, DarboVieta) VALUES (%s, %s, %s, %s)",(V, P, EP, DV,))
    
                
        mydb.commit()
        Vardas.delete(first=0,last=22)
        Pavarde.delete(first=0,last=22)
        Epastas.delete(first=0,last=22)
        DarboVieta.delete(first=0,last=22)
        irasyti_l.grid(row = 11, column=0,columnspan=2)
        

    def sarasas():
        saraso_paieska = Toplevel(DIL)
        saraso_paieska.title("Irasu sarasas")
        saraso_paieska.geometry("500x450")
        
        Visu_sarasas_l = LabelFrame(saraso_paieska)
        Visu_sarasas_l.grid(row =0, column = 0)
        
        ID_sarasas_l = LabelFrame(Visu_sarasas_l)
        ID_sarasas_l.grid(row =0, column = 0)
        VS_sarasas_l = LabelFrame(Visu_sarasas_l)
        VS_sarasas_l.grid(row =0, column = 1)
        PS_sarasas_l = LabelFrame(Visu_sarasas_l)
        PS_sarasas_l.grid(row =0, column = 2)
        VS_sarasas_l = LabelFrame(Visu_sarasas_l)
        VS_sarasas_l.grid(row =0, column = 3)
        EPS_sarasas_l = LabelFrame(Visu_sarasas_l)
        EPS_sarasas_l.grid(row =0, column = 4)
        DVS_sarasas_l = LabelFrame(Visu_sarasas_l)
        DVS_sarasas_l.grid(row =0, column = 5)
        
        ID_L = Label(ID_sarasas_l, text= "ID", bg="green")
        VS_L = Label(VS_sarasas_l, text= "Vardas", bg="green")
        PS_L = Label(PS_sarasas_l, text= "Pavarde", bg="green")
        EPS_L = Label(EPS_sarasas_l, text= "BLeID", bg="green")
        DVS_L = Label(DVS_sarasas_l, text= "DarboVieta", bg="green")
        
        
        ID_L.grid(row= 0, column = 0)
        VS_L.grid(row= 0, column = 1)
        PS_L.grid(row= 0, column = 2)
        EPS_L.grid(row= 0, column = 3)
        DVS_L.grid(row= 0, column = 4)
        
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM Darbuotojai")
        result = cursor.fetchall()
        for index, x in enumerate(result):
            num = 0
            for y in x:
                if((num+1) == 1):
                    saraso_l = Label(ID_sarasas_l, text=y)
                    saraso_l.grid(row=index+1, column=num)
                if((num+1) == 2):
                    saraso_l = Label(VS_sarasas_l, text=y)
                    saraso_l.grid(row=index+1, column=num)
                if((num+1) == 3):
                    saraso_l = Label(PS_sarasas_l, text=y)
                    saraso_l.grid(row=index+1, column=num)
                if((num+1) == 4):
                    saraso_l = Label(EPS_sarasas_l, text=y)
                    saraso_l.grid(row=index+1, column=num)
                if((num+1) == 5):
                    saraso_l = Label(DVS_sarasas_l, text=y)
                    saraso_l.grid(row=index+1, column=num)
                num +=1
        
    def ieskoti_irasas():
        global ID_L1, VS_L1, PS_L1, EPS_L1, DVS_L1
        global RB_sarasas_l1, ID_sarasas_l1, VS_sarasas_l1, PS_sarasas_l1, EPS_sarasas_l1, DVS_sarasas_l1
        ieskoti_irasas = Toplevel(DIL)
        ieskoti_irasas.title("Irasu sarasas")
        #iconbitmap
        ieskoti_irasas.geometry("800x250")
        
        ieskojimo_f =LabelFrame(ieskoti_irasas)
        ieskojimo_f.grid(row =0, column = 0)
        
        #redagavimo_f =LabelFrame(ieskoti_irasas)
        #redagavimo_f.grid(row =0, column = 2)
        
        Visu_sarasas_l1 = LabelFrame(ieskoti_irasas)
        Visu_sarasas_l1.grid(row =3, column = 0)
        
        def sukurti_LF():
            global RB_sarasas_l1, ID_sarasas_l1,VS_sarasas_l1, PS_sarasas_l1, EPS_sarasas_l1, DVS_sarasas_l1
            RB_sarasas_l1 =LabelFrame(Visu_sarasas_l1)
            RB_sarasas_l1.grid(row =0, column = 0)
            ID_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            ID_sarasas_l1.grid(row =0, column = 2)
            VS_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            VS_sarasas_l1.grid(row =0, column = 3)
            PS_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            PS_sarasas_l1.grid(row =0, column = 4)
            #VS_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            #VS_sarasas_l1.grid(row =0, column = 5)
            EPS_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            EPS_sarasas_l1.grid(row =0, column = 6)
            DVS_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            DVS_sarasas_l1.grid(row =0, column = 7)
        
            global ID_L1, VS_L1, PS_L1, EPS_L1, DVS_L1
            ID_L1 = Label(ID_sarasas_l1, text= "ID", bg="green")
            VS_L1 = Label(VS_sarasas_l1, text= "Vardas", bg="green")
            PS_L1 = Label(PS_sarasas_l1, text= "Pavarde", bg="green")
            EPS_L1 = Label(EPS_sarasas_l1, text= "ElektroninisPastas", bg="green")
            DVS_L1 = Label(DVS_sarasas_l1, text= "DarboVieta", bg="green")
        
        
            ID_L1.grid(row= 0, column = 0)
            VS_L1.grid(row= 0, column = 1)
            PS_L1.grid(row= 0, column = 2)
            EPS_L1.grid(row= 0, column = 3)
            DVS_L1.grid(row= 0, column = 4)
        
        sukurti_LF()
        global surastas_label
        surastas_label= Label(ieskojimo_f)
        
        
        def istrinti_h():
            global RB_sarasas_l1, ID_sarasas_l1,VS_sarasas_l1, PS_sarasas_l1, EPS_sarasas_l1, DVS_sarasas_l1
            global ID_L1, VS_L1, PS_L1, EPS_L1, DVS_L1
            result1 = tkinter.messagebox.askquestion("delete" "Ar tikrai norite istrinti irasa ?", icon='warning')
            global surastas_label
            T = False
            
            if(result1 == "yes"):
                surastas_label.destroy()
                surastas = ieskoti_box.get()
                pasirinktas = drop.get()
                if pasirinktas == "Ieskoti pagal ...":
                    surastas_label = Label(ieskojimo_f, fg="red", text="Nepasirinkta paieska")
                    surastas_label.grid(row=3,column=0)
                if pasirinktas == "Vardas":
                    sql = "DELETE from Darbuotojai WHERE Vardas = %s"
                    T = True
                if pasirinktas == "ElektroninisPastas":
                    sql = "DELETE from Darbuotojai WHERE ElektroninisPastas = %s"
                    T = True
                if pasirinktas == "Pavarde":
                    sql = "DELETE from Darbuotojai WHERE Pavarde = %s"
                    T = True
                if pasirinktas == "DarboVieta":
                    sql = "DELETE from Darbuotojai WHERE DarboVieta = %s"
                    T = True
                if pasirinktas == "ID":
                    sql = "DELETE from Darbuotojai WHERE ID = %s"
                    T = True
                    
                name = (surastas, )
                cursor = mydb.cursor()
                cursor.execute(sql, name)
                mydb.commit()
                
                RB_sarasas_l1.destroy()
                ID_sarasas_l1.destroy()
                VS_sarasas_l1.destroy()
                PS_sarasas_l1.destroy()
                VS_sarasas_l1.destroy()
                EPS_sarasas_l1.destroy()
                DVS_sarasas_l1.destroy()
                sukurti_LF()
 
                if(T == TRUE):
                    result = "Irasas istrintas"
                    surastas_label= Label(ieskojimo_f, text=result, fg ="green")
                    surastas_label.grid(row=2, column=2, padx=10)
                
                
        def redaguoti_n(id, index):
            
            redaguoti_irasas = Toplevel(DIL)
            redaguoti_irasas.title("Irasu redagavimas")
             
            sql2 = "Select * from Darbuotojai WHERE ID = %s"
                
            name2 = (id, )
            cursor = mydb.cursor()
            result2 = cursor.execute(sql2, name2)
            result2 = cursor.fetchall()
             
             
            def update():
                
                sql_command ="UPDATE Darbuotojai SET Vardas=%s, Pavarde=%s, ElektroninisPastas=%s, DarboVieta=%s WHERE ID=%s"
                
                global ID2_x, Pavarde2_x, Epastas2_x, DarboVieta2_x, Vardas2_x
                
                
                V = Vardas2_x.get()
                P = Pavarde2_x.get()
                EP = Epastas2_x.get()
                DV = DarboVieta2_x.get()
                
                id_value = ID2_x.get()
                inputs=(V, P, EP, DV, id_value)
                
                
                
                cursor = mydb.cursor()
                cursor.execute(sql_command, inputs)
                mydb.commit()
                
                redaguoti_irasas.destroy()
                
                
             # sukurti irasimo lenteles
            global ID2_x
            #ID2_x = Entry(redaguoti_irasas, width=30)
            #ID2_x.grid(row = 0, column=1,padx=20)
            #ID2_x.insert(0, result2[0][0])
            
            global Vardas2_x
            Vardas2_x = Entry(redaguoti_irasas, width=30)
            Vardas2_x.grid(row = 1, column=1,padx=20)
            Vardas2_x.insert(0, result2[0][1])
            
            global Pavarde2_x
            Pavarde2_x = Entry(redaguoti_irasas, width=30)
            Pavarde2_x.grid(row = 2, column=1,padx=20)
            Pavarde2_x.insert(0, result2[0][2])
            
            global Epastas2_x
            Epastas2_x =Entry(redaguoti_irasas, width=30)
            Epastas2_x.grid(row = 3, column=1,padx=20)
            Epastas2_x.insert(0, result2[0][3])
            
            global DarboVieta2_x
            DarboVieta2_x =Entry(redaguoti_irasas, width=30)
            DarboVieta2_x.grid(row = 4, column=1,padx=20)
            DarboVieta2_x.insert(0, result2[0][4])
            
            #DVT_LF = Label(DIL, text= "Datos formatas : MMMM-mm-dd", bg="blue")
            #DVT_LF.grid(row = 4, column=1,padx=20)

            # sukurti irasimo lenteliu  pavadinimus
            
            #ID_l = Label(redaguoti_irasas, text="ID")
            #ID_l.grid(row=0, column=0)
            Vardas_l = Label(redaguoti_irasas, text="Vardas")
            Vardas_l.grid(row=1, column=0)
            Pavarde_l = Label(redaguoti_irasas, text="Pavarde")
            Pavarde_l.grid(row=2, column=0)
            Epastas_l = Label(redaguoti_irasas, text="ElektroninisPastas")
            Epastas_l.grid(row=3, column=0)
            DarboVieta_l = Label(redaguoti_irasas, text="DarboVieta")
            DarboVieta_l.grid(row=4, column=0)
                
            isaugoti_irasa = Button(redaguoti_irasas, text= "issaugoti irasa", command=update)
            isaugoti_irasa.grid(row=5, column=0,padx=10,columnspan=2)
        
        def ieskoti_h():
            global surastas_label
            
            #urastas_label = Label(ieskojimo_f)
            surastas_label.destroy()
            surastas = ieskoti_box.get()
            
            pasirinktas = drop.get()
            
            if pasirinktas == "Ieskoti pagal ...":
                surastas_label = Label(ieskojimo_f, fg="red", text="Nepasirinkta paieska")
                surastas_label.grid(row=2,column=2)
            if pasirinktas == "Vardas":
                sql = "Select * from Darbuotojai WHERE Vardas = %s"
            if pasirinktas == "ElektroninisPastas":
                sql = "Select * from Darbuotojai WHERE ElektroninisPastas = %s"
            if pasirinktas == "DarboVieta":
                sql = "Select * from Darbuotojai WHERE DarboVieta = %s"
            if pasirinktas == "ID":
                sql = "Select * from Darbuotojai WHERE ID = %s"
            if pasirinktas == "Pavarde":
                sql = "Select * from Darbuotojai WHERE Pavarde = %s"
            
            
            
            name = (surastas, )
            cursor = mydb.cursor()
            result = cursor.execute(sql, name)
            result=cursor.fetchall()
            
            if not result:
                result = "Irasas neegzistuoja"
                surastas_label= Label(ieskojimo_f, text=result, fg ="red")
                surastas_label.grid(row=2, column=2, padx=10)
            else:
                for index, x in enumerate(result):
                    num = 0
                    id_reference = str(x[0])
                    Redguoti_b = Button(RB_sarasas_l1, text="Redaguoti irasa", command=lambda: redaguoti_n(id_reference, index))
                    Redguoti_b.grid(row=index+1,column=num)
                    for y in x:
                        if((num+1) == 1):
                            saraso_l = Label(ID_sarasas_l1, text=y)
                            saraso_l.grid(row=index+1, column=num)
                        if((num+1) == 2):
                            saraso_l = Label(VS_sarasas_l1, text=y)
                            saraso_l.grid(row=index+1, column=num)
                        if((num+1) == 3):
                            saraso_l = Label(PS_sarasas_l1, text=y)
                            saraso_l.grid(row=index+1, column=num)
                        if((num+1) == 4):
                            saraso_l = Label(EPS_sarasas_l1, text=y)
                            saraso_l.grid(row=index+1, column=num)
                        if((num+1) == 5):
                            saraso_l = Label(DVS_sarasas_l1, text=y)
                            saraso_l.grid(row=index+1, column=num)
                        num +=1
    
    
    
        # input
        ieskoti_box = Entry(ieskojimo_f)
        ieskoti_box.grid(row=0, column =1,padx = 10, pady=10)
        # label
        ieskoti_l = Label(ieskojimo_f, text = "ieskoti iraso")
        ieskoti_l.grid(row=0, column =0,padx = 10, pady=10)
        #mygtukai
        ieskoti_b = Button(ieskojimo_f, text="ieskoti", command=ieskoti_h)
        ieskoti_b.grid(row=1, column =0,padx = 10, pady=10)
        
        istrinti_b = Button(ieskojimo_f, text="Istrinti irasa", command=istrinti_h)
        istrinti_b.grid(row=2, column =1,padx = 10, pady=10)
        # drop down box
        drop = ttk.Combobox(ieskojimo_f, value=["Ieskoti pagal ...", "ID", "Vardas", "Pavarde", "ElektroninisPastas", "DarboVieta"])
        drop.current(0)
        drop.grid(row=0, column=2)
        
        

    # sukurti irasimo lenteles
    Vardas = Entry(DIL, width=30)
    Vardas.grid(row = 0, column=1,padx=20)
    Pavarde = Entry(DIL, width=30)
    Pavarde.grid(row = 1, column=1,padx=20)
    Epastas =Entry(DIL, width=30)
    Epastas.grid(row = 2, column=1,padx=20)
    DarboVieta =Entry(DIL, width=30)
    DarboVieta.grid(row = 3, column=1,padx=20)
    #DVT_LF = Label(DIL, text= "Datos formatas : MMMM-mm-dd", bg="blue")
    #DVT_LF.grid(row = 4, column=1,padx=20)

    # sukurti irasimo lenteliu  pavadinimus
    Vardas_l = Label(DIL, text="Vardas")
    Vardas_l.grid(row=0, column=0)
    Pavarde_l = Label(DIL, text="Pavarde")
    Pavarde_l.grid(row=1, column=0)
    Epastas_l = Label(DIL, text="ElektroninisPastas")
    Epastas_l.grid(row=2, column=0)
    DarboVieta_l = Label(DIL, text="DarboVieta")
    DarboVieta_l.grid(row=3, column=0)
    

    # sukurti mygtukus
    submit_b = Button(DIL, text= "irasyti i duomenu baze", command=tikrinti)
    submit_b.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100, sticky=W )
    # irasu saraso mygtukas
    saraso_b = Button(DIL, text="Perziurieti irasus", command=sarasas)
    saraso_b.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=121, sticky=W)
    #ieskojimo mygtukas
    ieskoti_b = Button(DIL, text="Ieskoti iraso", command=ieskoti_irasas)
    ieskoti_b.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=139, sticky=W)
    
    

    DIL.mainloop()
    