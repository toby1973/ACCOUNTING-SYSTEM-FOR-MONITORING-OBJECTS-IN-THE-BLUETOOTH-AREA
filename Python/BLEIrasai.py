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

def BIBLE():

    BIL = Toplevel()  # sukuriamas pagrindinis langas uzregistruoti pasiimta langas
    BIL.title('BLE irasai')
    BIL.geometry("450x300")
    
    global irasyti_l
    irasyti_l = Label(BIL)
    
    global MT, BT, VT
    global MT_L, BT_L, VT_L
    MT_L = Label(BIL) 
    #BT_L = Label(BIL)
    #VT_L = Label(BIL)

    
    def tikrinti():
        
        global MT, BT, VT
        MT = BT = VT = False
        
        global MT_L, BT_L, VT_L
        global irasyti_l
        MT_L.destroy()
        #BT_L.destroy()
        #VT_L.destroy()
        irasyti_l.destroy
        
        MT_L = Label(BIL, text= "Neirasita irenginio MacID", fg="red")
        #BT_L = Label(BIL, text= "Neirasita irenginio Busena", fg="red")
        #VT_L = Label(BIL, text= "Neirasita irenginio Vieta", fg="red") 
        
        regex = "[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$"
        
    
        if re.search(regex, MacID.get().lower()): #negali kartotis
            MID = []
            cursor = mydb.cursor()
            cursor.execute("SELECT MacID FROM BLEirenginiai  WHERE MacID =%s", (MacID.get(),))
            myresult = str(cursor.fetchall())
            MID.append(re.sub(r"[\,'(\)]",'',myresult))
            if not MID[0] == "["+MacID.get()+"]":
                print("AAA" + MID[0])
                MT = True
            else:
                tkinter.messagebox.showwarning(title="DUBLIKACIJA", message="Irenginys jau yra pasiimtas")   
        else:
            print(MacID.get().lower())
            MT_L.grid(row=11, column=0, columnspan=2)
        
            
        if MT == True:
            irasyti()
            
            
     # iraso duomenis i duomenu baze
    def irasyti():
        global MT_L, BT_L, VT_L
        global irasyti_l
        MT_L.destroy()
        #BT_L.destroy()
        #VT_L.destroy()
        irasyti_l.destroy
        M = MacID.get()
        B = "Isjungtas"
        V = "Sandelyje"

        
        irasyti_l = Label(BIL, fg="green" ,text="Duomenis irasyti")
        cursor = mydb.cursor()
        cursor.execute("Insert INTO BLEirenginiai (MacID, Busena, Vieta) VALUES (%s, %s, %s)",(M, B, V,))
    
                
        mydb.commit()
        MacID.delete(first=0,last=22)
        #Busena.delete(first=0,last=22)
        #Vieta.delete(first=0,last=22)
        irasyti_l.grid(row = 11, column=0,columnspan=2)
        

    def sarasas():
        saraso_paieska = Toplevel(BIL)
        saraso_paieska.title("Irasu sarasas")
        saraso_paieska.geometry("450x300")
        
        Visu_sarasas_l = LabelFrame(saraso_paieska)
        Visu_sarasas_l.grid(row =0, column = 0)
        
        ID_sarasas_l = LabelFrame(Visu_sarasas_l)
        ID_sarasas_l.grid(row =0, column = 0)
        MS_sarasas_l = LabelFrame(Visu_sarasas_l)
        MS_sarasas_l.grid(row =0, column = 1)
        BS_sarasas_l = LabelFrame(Visu_sarasas_l)
        BS_sarasas_l.grid(row =0, column = 2)
        VS_sarasas_l = LabelFrame(Visu_sarasas_l)
        VS_sarasas_l.grid(row =0, column = 3)

        
        ID_L = Label(ID_sarasas_l, text= "ID", bg="green")
        MS_L = Label(MS_sarasas_l, text= "MacID", bg="green")
        VS_L = Label(VS_sarasas_l, text= "Vieta", bg="green")
        BS_L = Label(BS_sarasas_l, text= "Busena", bg="green")

        
        
        ID_L.grid(row= 0, column = 0)
        MS_L.grid(row= 0, column = 1)
        VS_L.grid(row= 0, column = 2)
        BS_L.grid(row= 0, column = 3)

        
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM BLEirenginiai")
        result = cursor.fetchall()
        for index, x in enumerate(result):
            num = 0
            for y in x:
                if((num+1) == 1):
                    saraso_l = Label(ID_sarasas_l, text=y)
                    saraso_l.grid(row=index+1, column=num)
                if((num+1) == 2):
                    saraso_l = Label(MS_sarasas_l, text=y)
                    saraso_l.grid(row=index+1, column=num)
                if((num+1) == 3):
                    saraso_l = Label(BS_sarasas_l, text=y)
                    saraso_l.grid(row=index+1, column=num)
                if((num+1) == 4):
                    saraso_l = Label(VS_sarasas_l, text=y)
                    saraso_l.grid(row=index+1, column=num)
                num +=1
        
    def ieskoti_irasas():
        global ID_L1, MS_L1, VS_L1, BS_L1
        global RB_sarasas_l1, ID_sarasas_l1, MS_sarasas_l1, VS_sarasas_l1, BS_sarasas_l1
        ieskoti_irasas = Toplevel(BIL)
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
            global RB_sarasas_l1, ID_sarasas_l1,MS_sarasas_l1, VS_sarasas_l1, BS_sarasas_l1, KS_sarasas_l1
            RB_sarasas_l1 =LabelFrame(Visu_sarasas_l1)
            RB_sarasas_l1.grid(row =0, column = 0)
            ID_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            ID_sarasas_l1.grid(row =0, column = 2)
            MS_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            MS_sarasas_l1.grid(row =0, column = 3)
            BS_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            BS_sarasas_l1.grid(row =0, column = 4)
            VS_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            VS_sarasas_l1.grid(row =0, column = 6)

        
            global ID_L1, MS_L1, VS_L1, BS_L1, KS_L1
            ID_L1 = Label(ID_sarasas_l1, text= "ID", bg="green")
            MS_L1 = Label(MS_sarasas_l1, text= "MacID", bg="green")
            VS_L1 = Label(VS_sarasas_l1, text= "Vieta", bg="green")
            BS_L1 = Label(BS_sarasas_l1, text= "Busena", bg="green")

        
        
            ID_L1.grid(row= 0, column = 0)
            MS_L1.grid(row= 0, column = 1)
            VS_L1.grid(row= 0, column = 2)
            BS_L1.grid(row= 0, column = 3)

        
        sukurti_LF()
        global surastas_label
        surastas_label= Label(ieskojimo_f)
        
        
        def istrinti_h():
            global RB_sarasas_l1, ID_sarasas_l1,MS_sarasas_l1, VS_sarasas_l1, BS_sarasas_l1
            global ID_L1, MS_L1, VS_L1, BS_L1
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
                if pasirinktas == "MacID":
                    sql = "DELETE from BLEirenginiai WHERE MacID = %s"
                    T = True
                if pasirinktas == "Vieta":
                    sql = "DELETE from BLEirenginiai WHERE Vieta = %s"
                    T = True
                if pasirinktas == "Busena":
                    sql = "DELETE from BLEirenginiai WHERE Busena = %s"
                    T = True
                if pasirinktas == "BleID":
                    sql = "DELETE from BLEirenginiai WHERE BleID = %s"
                    T = True
                    
                name = (surastas, )
                cursor = mydb.cursor()
                cursor.execute(sql, name)
                mydb.commit()
                
                RB_sarasas_l1.destroy()
                ID_sarasas_l1.destroy()
                MS_sarasas_l1.destroy()
                VS_sarasas_l1.destroy()
                BS_sarasas_l1.destroy()

                sukurti_LF()
 
                if(T == TRUE):
                    result = "Irasas istrintas"
                    surastas_label= Label(ieskojimo_f, text=result, fg ="green")
                    surastas_label.grid(row=2, column=2, padx=10)
                
                
        def redaguoti_n(id, index):
            
            redaguoti_irasas = Toplevel(BIL)
            redaguoti_irasas.title("Irasu redagavimas")
             
            sql2 = "Select * from BLEirenginiai WHERE BleID = %s"
                
            name2 = (id, )
            cursor = mydb.cursor()
            result2 = cursor.execute(sql2, name2)
            result2 = cursor.fetchall()
             
             
            def update():
                
                sql_command ="UPDATE BLEirenginiai SET MacID=%s, Busena=%s, Vieta=%s WHERE BleID=%s"
                
                global ID2_x, MacID2_x, Busena2, Vieta2
                
                
                V = Vieta2.get()
                M = MacID2_x.get()
                B = Busena2.get()
                
                id_value = ID2_x.get()
                inputs=(M, B, V, id_value)
                
                
                
                cursor = mydb.cursor()
                cursor.execute(sql_command, inputs)
                mydb.commit()
                
                redaguoti_irasas.destroy()
                
                
             # sukurti irasimo lenteles
            global ID2_x
            #ID2_x = label(redaguoti_irasas, width=30)
            #ID2_x.grid(row = 0, column=1,padx=20)
            #ID2_x.insert(0, result2[0][0])
            
            global Vieta2
            Vieta2 = Entry(redaguoti_irasas, width=30)
            Vieta2.grid(row = 3, column=1,padx=20)
            Vieta2.insert(0, result2[0][3])
            
            global MacID2_x
            MacID2_x = Entry(redaguoti_irasas, width=30)
            MacID2_x.grid(row = 1, column=1,padx=20)
            MacID2_x.insert(0, result2[0][1])
            
            global Busena2
            Busena2 =Entry(redaguoti_irasas, width=30)
            Busena2.grid(row = 2, column=1,padx=20)
            Busena2.insert(0, result2[0][2])
            


            # sukurti irasimo lenteliu  pavadinimus
            
            #ID_l = Label(redaguoti_irasas, text="BleID")
            #ID_l.grid(row=0, column=0)
            MacID_l = Label(redaguoti_irasas, text="MacID")
            MacID_l.grid(row=1, column=0)
            Vieta_l = Label(redaguoti_irasas, text="Vieta")
            Vieta_l.grid(row=2, column=0)
            Busena_l = Label(redaguoti_irasas, text="Busena")
            Busena_l.grid(row=3, column=0)

                
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
            if pasirinktas == "MacID":
                sql = "Select * from BLEirenginiai WHERE MacID = %s"
            if pasirinktas == "Vieta":
                sql = "Select * from BLEirenginiai WHERE Vieta = %s"
            if pasirinktas == "Busena":
                sql = "Select * from BLEirenginiai WHERE Busena = %s"
            if pasirinktas == "BleID":
                sql = "Select * from BLEirenginiai WHERE BleID = %s"
                
            
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
                            saraso_l = Label(MS_sarasas_l1, text=y)
                            saraso_l.grid(row=index+1, column=num)
                        if((num+1) == 3):
                            saraso_l = Label(BS_sarasas_l1, text=y)
                            saraso_l.grid(row=index+1, column=num)
                        if((num+1) == 4):
                            saraso_l = Label(VS_sarasas_l1, text=y)
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
        drop = ttk.Combobox(ieskojimo_f, value=["Ieskoti pagal ...", "MacID", "Vieta", "Busena", "BleID"])
        drop.current(0)
        drop.grid(row=0, column=2)
        
        

    # sukurti irasimo lenteles
    MacID = Entry(BIL, width=30)
    MacID.grid(row = 0, column=1,padx=20)
    #Busena = Entry(BIL, width=30)
    #Busena.grid(row = 1, column=1,padx=20)
    #Vieta =Entry(BIL, width=30)
    #Vieta.grid(row = 2, column=1,padx=20)


    # sukurti irasimo lenteliu  pavadinimus
    MacID_l = Label(BIL, text="MacID")
    MacID_l.grid(row=0, column=0)
    #Busena_l = Label(BIL, text="Busena")
    #Busena_l.grid(row=1, column=0)
    #Vieta_l = Label(BIL, text="Vieta")
    #Vieta_l.grid(row=2, column=0)

    

    # sukurti mygtukus
    submit_b = Button(BIL, text= "irasyti i duomenu baze", command=tikrinti)
    submit_b.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100, sticky=W )
    # irasu saraso mygtukas
    saraso_b = Button(BIL, text="Perziurieti irasus", command=sarasas)
    saraso_b.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=121, sticky=W)
    #ieskojimo mygtukas
    ieskoti_b = Button(BIL, text="Ieskoti iraso", command=ieskoti_irasas)
    ieskoti_b.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=139, sticky=W)
    
    

    BIL.mainloop()
    