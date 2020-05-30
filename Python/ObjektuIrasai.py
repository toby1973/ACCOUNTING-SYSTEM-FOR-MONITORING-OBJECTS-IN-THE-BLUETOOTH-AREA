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

def OIBLE():

    OIL = Toplevel()  # sukuriamas pagrindinis langas uzregistruoti pasiimta langas
    OIL.title('BLE irasai')
    OIL.geometry("450x300")
    
    global irasyti_l
    irasyti_l = Label(OIL)
    
    global OT
    global OT_L
    OT_L = Label(OIL) 
    #BT_L = Label(OIL)
    #VT_L = Label(OIL)

    
    def tikrinti():
        
        global OT
        OT = False
        
        global OT_L
        global irasyti_l
        OT_L.destroy()
        #BT_L.destroy()
        #VT_L.destroy()
        irasyti_l.destroy
        
        OT_L = Label(OIL, text= "Neirasitas arba blogai ivestas Objektas", fg="red")
        #BT_L = Label(OIL, text= "Neirasita irenginio Busena", fg="red")
        #VT_L = Label(OIL, text= "Neirasita irenginio Vieta", fg="red") 
        
        
        
    
        if len(Pavadinimas.get()) == 0 or Pavadinimas.get().isnumeric(): #negali kartotis
            OT_L.grid(row=11, column=0, columnspan=2)
        else:
            OT = True
            
        if OT == True:
            irasyti()
            
            
     # iraso duomenis i duomenu baze
    def irasyti():
        global OT_L
        global irasyti_l
        OT_L.destroy()
        #BT_L.destroy()
        #VT_L.destroy()
        irasyti_l.destroy
        O = Pavadinimas.get()
        #B = "Isjungtas"
        #V = "Sandelyje"

        
        irasyti_l = Label(OIL, fg="green" ,text="Duomenis irasyti")
        cursor = mydb.cursor()
        cursor.execute("Insert INTO Objektai (Pavadinimas) VALUE (%s)",(O,))
    
                
        mydb.commit()
        Pavadinimas.delete(first=0,last=22)
        #Busena.delete(first=0,last=22)
        #Vieta.delete(first=0,last=22)
        irasyti_l.grid(row = 11, column=0,columnspan=2)
        

    def sarasas():
        saraso_paieska = Toplevel(OIL)
        saraso_paieska.title("Irasu sarasas")
        saraso_paieska.geometry("450x300")
        
        Visu_sarasas_l = LabelFrame(saraso_paieska)
        Visu_sarasas_l.grid(row =0, column = 0)
        
        ID_sarasas_l = LabelFrame(Visu_sarasas_l)
        ID_sarasas_l.grid(row =0, column = 0)
        OS_sarasas_l = LabelFrame(Visu_sarasas_l)
        OS_sarasas_l.grid(row =0, column = 1)
        #VS_sarasas_l = LabelFrame(Visu_sarasas_l)
        #VS_sarasas_l.grid(row =0, column = 2)
        #BS_sarasas_l = LabelFrame(Visu_sarasas_l)
        #BS_sarasas_l.grid(row =0, column = 3)

        
        ID_L = Label(ID_sarasas_l, text= "ID", bg="green")
        OS_L = Label(OS_sarasas_l, text= "Pavadinimas", bg="green")
        #VS_L = Label(VS_sarasas_l, text= "Vieta", bg="green")
        #BS_L = Label(BS_sarasas_l, text= "Busena", bg="green")

        
        
        ID_L.grid(row= 0, column = 0)
        OS_L.grid(row= 0, column = 1)
        #VS_L.grid(row= 0, column = 2)
        #BS_L.grid(row= 0, column = 3)

        
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM Objektai")
        result = cursor.fetchall()
        for index, x in enumerate(result):
            num = 0
            for y in x:
                if((num+1) == 1):
                    saraso_l = Label(ID_sarasas_l, text=y)
                    saraso_l.grid(row=index+1, column=num)
                if((num+1) == 2):
                    saraso_l = Label(OS_sarasas_l, text=y)
                    saraso_l.grid(row=index+1, column=num)
                num +=1
        
    def ieskoti_irasas():
        global ID_L1, OS_L1
        global RB_sarasas_l1, ID_sarasas_l1, OS_sarasas_l1, VS_sarasas_l1, BS_sarasas_l1
        ieskoti_irasas = Toplevel(OIL)
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
            global RB_sarasas_l1, ID_sarasas_l1,OS_sarasas_l1, VS_sarasas_l1, BS_sarasas_l1, KS_sarasas_l1
            RB_sarasas_l1 =LabelFrame(Visu_sarasas_l1)
            RB_sarasas_l1.grid(row =0, column = 0)
            ID_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            ID_sarasas_l1.grid(row =0, column = 2)
            OS_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            OS_sarasas_l1.grid(row =0, column = 3)
            #VS_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            #VS_sarasas_l1.grid(row =0, column = 4)
            #BS_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            #BS_sarasas_l1.grid(row =0, column = 6)

        
            global ID_L1, OS_L1, VS_L1, BS_L1, KS_L1
            ID_L1 = Label(ID_sarasas_l1, text= "ID", bg="green")
            OS_L1 = Label(OS_sarasas_l1, text= "Pavadinimas", bg="green")
            #VS_L1 = Label(VS_sarasas_l1, text= "Vieta", bg="green")
            #BS_L1 = Label(BS_sarasas_l1, text= "Busena", bg="green")

        
        
            ID_L1.grid(row= 0, column = 0)
            OS_L1.grid(row= 0, column = 1)
            #VS_L1.grid(row= 0, column = 2)
            #BS_L1.grid(row= 0, column = 3)

        
        sukurti_LF()
        global surastas_label
        surastas_label= Label(ieskojimo_f)
        
        
        def istrinti_h():
            global RB_sarasas_l1, ID_sarasas_l1,OS_sarasas_l1, VS_sarasas_l1, BS_sarasas_l1
            global ID_L1, OS_L1, VS_L1, BS_L1
            result1 = tkinter.messagebox.askquestion("Delete", "Ar tikrai norite istrinti irasa ?", icon='warning')
            global surastas_label
            T = False
            
            if(result1 == "yes"):
                surastas_label.destroy()
                surastas = ieskoti_box.get()
                pasirinktas = drop.get()
                if pasirinktas == "Ieskoti pagal ...":
                    surastas_label = Label(ieskojimo_f, fg="red", text="Nepasirinkta paieska")
                    surastas_label.grid(row=3,column=0)
                if pasirinktas == "Pavadinimas":
                    sql = "DELETE from Objektai WHERE Pavadinimas = %s"
                    T = True
                if pasirinktas == "ID":
                    sql = "DELETE from Objektai WHERE ID = %s"
                    T = True
                    
                name = (surastas, )
                cursor = mydb.cursor()
                cursor.execute(sql, name)
                mydb.commit()
                
                RB_sarasas_l1.destroy()
                ID_sarasas_l1.destroy()
                OS_sarasas_l1.destroy()
                #VS_sarasas_l1.destroy()
                #BS_sarasas_l1.destroy()

                sukurti_LF()
 
                if(T == TRUE):
                    result = "Irasas istrintas"
                    surastas_label= Label(ieskojimo_f, text=result, fg ="green")
                    surastas_label.grid(row=2, column=2, padx=10)
                
                
        def redaguoti_n(id, index):
            
            redaguoti_irasas = Toplevel(OIL)
            redaguoti_irasas.title("Irasu redagavimas")
             
            sql2 = "Select * from Objektai WHERE ID = %s"
                
            name2 = (id, )
            cursor = mydb.cursor()
            result2 = cursor.execute(sql2, name2)
            result2 = cursor.fetchall()
             
             
            def update():
                
                sql_command ="UPDATE Objektai SET Pavadinimas=%s WHERE ID=%s"
                
                global ID2_x, Pavadinimas2_x, Busena2, Vieta2
                
                
                #V = Vieta2.get()
                M = Pavadinimas2_x.get()
                #B = Busena2.get()
                
                id_value = ID2_x.get()
                inputs=(M, id_value)
                
                
                
                cursor = mydb.cursor()
                cursor.execute(sql_command, inputs)
                mydb.commit()
                
                redaguoti_irasas.destroy()
                
                
             # sukurti irasimo lenteles
            global ID2_x
            #ID2_x = label(redaguoti_irasas, width=30)
            #ID2_x.grid(row = 0, column=1,padx=20)
            #ID2_x.insert(0, result2[0][0])
            
            
            
            global Pavadinimas2_x
            Pavadinimas2_x = Entry(redaguoti_irasas, width=30)
            Pavadinimas2_x.grid(row = 1, column=1,padx=20)
            Pavadinimas2_x.insert(0, result2[0][1])
            
            
            


            # sukurti irasimo lenteliu  pavadinimus
            
            #ID_l = Label(redaguoti_irasas, text="BleID")
            #ID_l.grid(row=0, column=0)
            Pavadinimas_l = Label(redaguoti_irasas, text="Pavadinimas")
            Pavadinimas_l.grid(row=1, column=0)
            

                
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
            if pasirinktas == "Pavadinimas":
                sql = "Select * from Objektai WHERE Pavadinimas = %s"
            if pasirinktas == "ID":
                sql = "Select * from Objektai WHERE ID = %s"
                
            
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
                            saraso_l = Label(OS_sarasas_l1, text=y)
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
        drop = ttk.Combobox(ieskojimo_f, value=["Ieskoti pagal ...", "Pavadinimas", "ID"])
        drop.current(0)
        drop.grid(row=0, column=2)
        
        

    # sukurti irasimo lenteles
    Pavadinimas = Entry(OIL, width=30)
    Pavadinimas.grid(row = 0, column=1,padx=20)
    #Busena = Entry(OIL, width=30)
    #Busena.grid(row = 1, column=1,padx=20)
    #Vieta =Entry(OIL, width=30)
    #Vieta.grid(row = 2, column=1,padx=20)


    # sukurti irasimo lenteliu  pavadinimus
    Pavadinimas_l = Label(OIL, text="Pavadinimas")
    Pavadinimas_l.grid(row=0, column=0)
    #Busena_l = Label(OIL, text="Busena")
    #Busena_l.grid(row=1, column=0)
    #Vieta_l = Label(OIL, text="Vieta")
    #Vieta_l.grid(row=2, column=0)

    

    # sukurti mygtukus
    submit_b = Button(OIL, text= "irasyti i duomenu baze", command=tikrinti)
    submit_b.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100, sticky=W )
    # irasu saraso mygtukas
    saraso_b = Button(OIL, text="Perziurieti irasus", command=sarasas)
    saraso_b.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=121, sticky=W)
    #ieskojimo mygtukas
    ieskoti_b = Button(OIL, text="Ieskoti iraso", command=ieskoti_irasas)
    ieskoti_b.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=139, sticky=W)
    
    

    OIL.mainloop()
    