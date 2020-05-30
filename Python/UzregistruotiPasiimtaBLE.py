from tkinter import *
import tkinter.font
from tkinter import messagebox
import mysql.connector
import datetime
from tkinter import ttk
#from GUI import mydb

# uzregistruoti pasiimta BLE
mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        passwd="laukas12",
        database="BLE"
        )

def UPBLE():

    UPL = Toplevel()  # sukuriamas pagrindinis langas uzregistruoti pasiimta langas
    UPL.title('Uzregistruoti pasiimta BLE')
    UPL.geometry("450x300")
    
    global irasyti_l
    irasyti_l = Label(UPL)
    
    global DT, OT, BT, KT
    global DT_L, OT_L, BT_L, KT_L, KT_LF
    DT_L = Label(UPL)
    OT_L = Label(UPL) 
    BT_L = Label(UPL)
    KT_L = Label(UPL)
    KT_LF = Label(UPL)
    
    def tikrinti():
        
        global DT, OT, BT, KT
        DT = OT = BT = KT = False
        
        global DT_L, OT_L, BT_L, KT_L
        global irasyti_l
        DT_L.destroy()
        OT_L.destroy()
        BT_L.destroy()
        KT_L.destroy()
        irasyti_l.destroy
        
        DT_L = Label(UPL, text= "Neirasitas arba blogai ivestas DarbuotojoID", fg="red")
        OT_L = Label(UPL, text= "Neirasitas arba blogai ivestas ObjektoID", fg="red")
        BT_L = Label(UPL, text= "Neirasitas arba blogai ivestas BLEID", fg="red")
        #KT_L = Label(UPL, text= "Neirasita KadaPasiimtas", fg="red") #0000-00-00
        
        
        if len(DarbID.get()) == 0 or DarbID.get().isalpha():
            DT_L.grid(row=7, column=0,columnspan=2)
        else :
            DID = []
            cursor = mydb.cursor()
            cursor.execute("SELECT ID FROM Darbuotojai  WHERE ID =%s", (DarbID.get(),))
            myresult = str(cursor.fetchall())
            DID.append(re.sub(r"[\,'(\)]",'',myresult))
            if DID[0] == "["+DarbID.get()+"]":
                DT = True
            else:
                tkinter.messagebox.showwarning(title="NEEGZITUOJA", message="Darbuotojas NEEGZITUOJA")
            
        if len(ObjektoID.get()) == 0 or ObjektoID.get().isalpha(): #negali kartotis
            OT_L.grid(row=8, column=0, columnspan=2)
        else :
            OID = []
            cursor = mydb.cursor()
            cursor.execute("SELECT ObjektoID FROM PasiimtoObjektoInformacija  WHERE ObjektoID =%s", (ObjektoID.get(),))
            myresult = str(cursor.fetchall())
            OID.append(re.sub(r"[\,'(\)]",'',myresult))
            if not OID[0] == "["+ObjektoID.get()+"]":
                OID = []
                cursor = mydb.cursor()
                cursor.execute("SELECT ID FROM Objektai  WHERE ID =%s", (ObjektoID.get(),))
                myresult = str(cursor.fetchall())
                OID.append(re.sub(r"[\,'(\)]",'',myresult))
                if OID[0] == "["+ObjektoID.get()+"]":
                    OT = True
                else:
                    tkinter.messagebox.showwarning(title="NEEGZITUOJA", message="Objektas NEEGZITUOJA")
            else:
                tkinter.messagebox.showwarning(title="DUBLIKACIJA", message="Objektas jau yra pasiimtas")    
        if len(BleID.get()) == 0 or BleID.get().isalpha(): #negali kartotis
            BT_L.grid(row=9, column=0,columnspan=2)
        else :
            BID = []
            cursor = mydb.cursor()
            cursor.execute("SELECT BleID FROM PasiimtoObjektoInformacija  WHERE BleID =%s", (BleID.get(),))
            myresult = str(cursor.fetchall())
            BID.append(re.sub(r"[\,'(\)]",'',myresult))
            if not BID[0] == "["+BleID.get()+"]":
                BID = []
                cursor = mydb.cursor()
                cursor.execute("SELECT BleID FROM BLEirenginiai WHERE BleID =%s", (BleID.get(),))
                myresult = str(cursor.fetchall())
                BID.append(re.sub(r"[\,'(\)]",'',myresult))
                if BID[0] == "["+BleID.get()+"]":
                    BT = True
                else:
                    tkinter.messagebox.showwarning(title="NEEGZISTUOJA", message="BLE irenginys NEEGZISTUOJA")
            else:
                tkinter.messagebox.showwarning(title="DUBLIKACIJA", message="BLE irenginys jau yra pasiimtas")
        #if len(KadaPasiimtas.get()) == 0:
            #KT_L.grid(row=10, column=0, columnspan=2)
        #else :
            #KT = True
            
        if DT and OT and BT: #and KT == True:
            irasyti()
            
            
     # iraso duomenis i duomenu baze
    def irasyti():
        global DT_L, OT_L, BT_L, KT_L
        global irasyti_l
        DT_L.destroy()
        OT_L.destroy()
        BT_L.destroy()
        #KT_L.destroy()
        irasyti_l.destroy
        D = DarbID.get()
        O = ObjektoID.get()
        B = BleID.get()
        #K = KadaPasiimtas.get()
        now = datetime.datetime.now()
        data = str(now.strftime("%Y-%m-%d:%H:%M"))
        
        irasyti_l = Label(UPL, fg="green" ,text="Duomenis irasyti")
        cursor = mydb.cursor()
        cursor.execute("Insert INTO PasiimtoObjektoInformacija (DarbID, ObjektoID, BleID, KadaPasiimtas) VALUES (%s, %s, %s, %s)",(D, O, B, data,))
    
                
        mydb.commit()
        DarbID.delete(first=0,last=22)
        ObjektoID.delete(first=0,last=22)
        BleID.delete(first=0,last=22)
        #KadaPasiimtas.delete(first=0,last=22)
        irasyti_l.grid(row = 11, column=0,columnspan=2)
        

    def sarasas():
        saraso_paieska = Toplevel(UPL)
        saraso_paieska.title("Irasu sarasas")
        saraso_paieska.geometry("450x300")
        
        Visu_sarasas_l = LabelFrame(saraso_paieska)
        Visu_sarasas_l.grid(row =0, column = 0)
        
        ID_sarasas_l = LabelFrame(Visu_sarasas_l)
        ID_sarasas_l.grid(row =0, column = 0)
        DS_sarasas_l = LabelFrame(Visu_sarasas_l)
        DS_sarasas_l.grid(row =0, column = 1)
        OS_sarasas_l = LabelFrame(Visu_sarasas_l)
        OS_sarasas_l.grid(row =0, column = 2)
        DS_sarasas_l = LabelFrame(Visu_sarasas_l)
        DS_sarasas_l.grid(row =0, column = 3)
        BS_sarasas_l = LabelFrame(Visu_sarasas_l)
        BS_sarasas_l.grid(row =0, column = 4)
        KS_sarasas_l = LabelFrame(Visu_sarasas_l)
        KS_sarasas_l.grid(row =0, column = 5)
        
        ID_L = Label(ID_sarasas_l, text= "ID", bg="green")
        DS_L = Label(DS_sarasas_l, text= "DarbuotojoID", bg="green")
        OS_L = Label(OS_sarasas_l, text= "ObjektoID", bg="green")
        BS_L = Label(BS_sarasas_l, text= "BLeID", bg="green")
        KS_L = Label(KS_sarasas_l, text= "KadaPasiimtas", bg="green")
        
        
        ID_L.grid(row= 0, column = 0)
        DS_L.grid(row= 0, column = 1)
        OS_L.grid(row= 0, column = 2)
        BS_L.grid(row= 0, column = 3)
        KS_L.grid(row= 0, column = 4)
        
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM PasiimtoObjektoInformacija")
        result = cursor.fetchall()
        for index, x in enumerate(result):
            num = 0
            for y in x:
                if((num+1) == 1):
                    saraso_l = Label(ID_sarasas_l, text=y)
                    saraso_l.grid(row=index+1, column=num)
                if((num+1) == 2):
                    saraso_l = Label(DS_sarasas_l, text=y)
                    saraso_l.grid(row=index+1, column=num)
                if((num+1) == 3):
                    saraso_l = Label(OS_sarasas_l, text=y)
                    saraso_l.grid(row=index+1, column=num)
                if((num+1) == 4):
                    saraso_l = Label(BS_sarasas_l, text=y)
                    saraso_l.grid(row=index+1, column=num)
                if((num+1) == 5):
                    saraso_l = Label(KS_sarasas_l, text=y)
                    saraso_l.grid(row=index+1, column=num)
                num +=1
        
    def ieskoti_irasas():
        global ID_L1, DS_L1, OS_L1, BS_L1, KS_L1
        global RB_sarasas_l1, ID_sarasas_l1,DS_sarasas_l1, OS_sarasas_l1, BS_sarasas_l1, KS_sarasas_l1
        ieskoti_irasas = Toplevel(UPL)
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
            global RB_sarasas_l1, ID_sarasas_l1,DS_sarasas_l1, OS_sarasas_l1, BS_sarasas_l1, KS_sarasas_l1
            RB_sarasas_l1 =LabelFrame(Visu_sarasas_l1)
            RB_sarasas_l1.grid(row =0, column = 0)
            ID_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            ID_sarasas_l1.grid(row =0, column = 2)
            DS_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            DS_sarasas_l1.grid(row =0, column = 3)
            OS_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            OS_sarasas_l1.grid(row =0, column = 4)
            #DS_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            #DS_sarasas_l1.grid(row =0, column = 5)
            BS_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            BS_sarasas_l1.grid(row =0, column = 6)
            KS_sarasas_l1 = LabelFrame(Visu_sarasas_l1)
            KS_sarasas_l1.grid(row =0, column = 7)
        
            global ID_L1, DS_L1, OS_L1, BS_L1, KS_L1
            ID_L1 = Label(ID_sarasas_l1, text= "ID", bg="green")
            DS_L1 = Label(DS_sarasas_l1, text= "DarbuotojoID", bg="green")
            OS_L1 = Label(OS_sarasas_l1, text= "ObjektoID", bg="green")
            BS_L1 = Label(BS_sarasas_l1, text= "BLeID", bg="green")
            KS_L1 = Label(KS_sarasas_l1, text= "KadaPasiimtas", bg="green")
        
        
            ID_L1.grid(row= 0, column = 0)
            DS_L1.grid(row= 0, column = 1)
            OS_L1.grid(row= 0, column = 2)
            BS_L1.grid(row= 0, column = 3)
            KS_L1.grid(row= 0, column = 4)
        
        sukurti_LF()
        global surastas_label
        surastas_label= Label(ieskojimo_f)
        
        
        def istrinti_h():
            global RB_sarasas_l1, ID_sarasas_l1,DS_sarasas_l1, OS_sarasas_l1, BS_sarasas_l1, KS_sarasas_l1
            global ID_L1, DS_L1, OS_L1, BS_L1, KS_L1
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
                if pasirinktas == "DarbuotojoID":
                    sql = "DELETE from PasiimtoObjektoInformacija WHERE DarbID = %s"
                    T = True
                if pasirinktas == "BleID":
                    sql = "DELETE from PasiimtoObjektoInformacija WHERE BleID = %s"
                    T = True
                if pasirinktas == "ObjektoID":
                    sql = "DELETE from PasiimtoObjektoInformacija WHERE ObjektoID = %s"
                    T = True
                    
                name = (surastas, )
                cursor = mydb.cursor()
                cursor.execute(sql, name)
                mydb.commit()
                
                RB_sarasas_l1.destroy()
                ID_sarasas_l1.destroy()
                DS_sarasas_l1.destroy()
                OS_sarasas_l1.destroy()
                DS_sarasas_l1.destroy()
                BS_sarasas_l1.destroy()
                KS_sarasas_l1.destroy()
                sukurti_LF()
 
                if(T == TRUE):
                    result = "Irasas istrintas"
                    surastas_label= Label(ieskojimo_f, text=result, fg ="green")
                    surastas_label.grid(row=2, column=2, padx=10)
                
                
        def redaguoti_n(id, index):
            
            redaguoti_irasas = Toplevel(UPL)
            redaguoti_irasas.title("Irasu redagavimas")
             
            sql2 = "Select * from PasiimtoObjektoInformacija WHERE ID = %s"
                
            name2 = (id, )
            cursor = mydb.cursor()
            result2 = cursor.execute(sql2, name2)
            result2 = cursor.fetchall()
             
             
            def update():
                
                sql_command ="UPDATE PasiimtoObjektoInformacija SET DarbID=%s, ObjektoID=%s, BleID=%s, KadaPasiimtas=%s WHERE ID=%s"
                
                global ID2_x, ObjektoID2_x, BleID2_x, KadaPasiimtas2_x, DarbID2_x
                
                
                D = DarbID2_x.get()
                O = ObjektoID2_x.get()
                B = BleID2_x.get()
                K = KadaPasiimtas2_x.get()
                
                id_value = ID2_x.get()
                inputs=(D, O, B, K, id_value)
                
                
                
                cursor = mydb.cursor()
                cursor.execute(sql_command, inputs)
                mydb.commit()
                
                redaguoti_irasas.destroy()
                
                
             # sukurti irasimo lenteles
            global ID2_x
            #ID2_x = Entry(redaguoti_irasas, width=30)
            #ID2_x.grid(row = 0, column=1,padx=20)
            #ID2_x.insert(0, result2[0][0])
            
            global DarbID2_x
            DarbID2_x = Entry(redaguoti_irasas, width=30)
            DarbID2_x.grid(row = 1, column=1,padx=20)
            DarbID2_x.insert(0, result2[0][1])
            
            global ObjektoID2_x
            ObjektoID2_x = Entry(redaguoti_irasas, width=30)
            ObjektoID2_x.grid(row = 2, column=1,padx=20)
            ObjektoID2_x.insert(0, result2[0][2])
            
            global BleID2_x
            BleID2_x =Entry(redaguoti_irasas, width=30)
            BleID2_x.grid(row = 3, column=1,padx=20)
            BleID2_x.insert(0, result2[0][3])
            
            global KadaPasiimtas2_x
            KadaPasiimtas2_x =Entry(redaguoti_irasas, width=30)
            KadaPasiimtas2_x.grid(row = 4, column=1,padx=20)
            KadaPasiimtas2_x.insert(0, result2[0][4])
            
            #KT_LF = Label(UPL, text= "Datos formatas : MMMM-mm-dd", bg="blue")
            #KT_LF.grid(row = 4, column=1,padx=20)

            # sukurti irasimo lenteliu  pavadinimus
            
            #ID_l = Label(redaguoti_irasas, text="ID")
            #ID_l.grid(row=0, column=0)
            DarbID_l = Label(redaguoti_irasas, text="Darbuotojo ID")
            DarbID_l.grid(row=1, column=0)
            ObjektoID_l = Label(redaguoti_irasas, text="Objekto ID")
            ObjektoID_l.grid(row=2, column=0)
            BleID_l = Label(redaguoti_irasas, text="BLE ID")
            BleID_l.grid(row=3, column=0)
            KadaPasiimtas_l = Label(redaguoti_irasas, text="Kada Pasiimtas")
            KadaPasiimtas_l.grid(row=4, column=0)
                
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
            if pasirinktas == "DarbuotojoID":
                sql = "Select * from PasiimtoObjektoInformacija WHERE DarbID = %s"
            if pasirinktas == "BleID":
                sql = "Select * from PasiimtoObjektoInformacija WHERE BleID = %s"
            if pasirinktas == "ObjektoID":
                sql = "Select * from PasiimtoObjektoInformacija WHERE ObjektoID = %s"
            
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
                            saraso_l = Label(DS_sarasas_l1, text=y)
                            saraso_l.grid(row=index+1, column=num)
                        if((num+1) == 3):
                            saraso_l = Label(OS_sarasas_l1, text=y)
                            saraso_l.grid(row=index+1, column=num)
                        if((num+1) == 4):
                            saraso_l = Label(BS_sarasas_l1, text=y)
                            saraso_l.grid(row=index+1, column=num)
                        if((num+1) == 5):
                            saraso_l = Label(KS_sarasas_l1, text=y)
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
        drop = ttk.Combobox(ieskojimo_f, value=["Ieskoti pagal ...", "DarbuotojoID", "BleID", "ObjektoID"])
        drop.current(0)
        drop.grid(row=0, column=2)
        
        

    # sukurti irasimo lenteles
    DarbID = Entry(UPL, width=30)
    DarbID.grid(row = 0, column=1,padx=20)
    ObjektoID = Entry(UPL, width=30)
    ObjektoID.grid(row = 1, column=1,padx=20)
    BleID =Entry(UPL, width=30)
    BleID.grid(row = 2, column=1,padx=20)
    #KadaPasiimtas =Entry(UPL, width=30)
    #KadaPasiimtas.grid(row = 3, column=1,padx=20)
    #KT_LF = Label(UPL, text= "Datos formatas : MMMM-mm-dd", bg="blue")
    #KT_LF.grid(row = 4, column=1,padx=20)

    # sukurti irasimo lenteliu  pavadinimus
    DarbID_l = Label(UPL, text="Darbuotojo ID")
    DarbID_l.grid(row=0, column=0)
    ObjektoID_l = Label(UPL, text="Objekto ID")
    ObjektoID_l.grid(row=1, column=0)
    BleID_l = Label(UPL, text="BLE ID")
    BleID_l.grid(row=2, column=0)
    #KadaPasiimtas_l = Label(UPL, text="Kada Pasiimtas")
    #KadaPasiimtas_l.grid(row=3, column=0)
    

    # sukurti mygtukus
    submit_b = Button(UPL, text= "irasyti i duomenu baze", command=tikrinti)
    submit_b.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100, sticky=W )
    # irasu saraso mygtukas
    saraso_b = Button(UPL, text="Perziurieti irasus", command=sarasas)
    saraso_b.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=121, sticky=W)
    #ieskojimo mygtukas
    ieskoti_b = Button(UPL, text="Ieskoti iraso", command=ieskoti_irasas)
    ieskoti_b.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=139, sticky=W)
    
    

    UPL.mainloop()
    