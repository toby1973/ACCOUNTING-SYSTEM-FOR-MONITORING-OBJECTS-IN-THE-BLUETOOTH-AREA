from tkinter import *
import tkinter.font
import mysql.connector
from functools import partial
from bluetooth.ble import DiscoveryService
from time import time
# regex
import re
# DATA
import subprocess
import datetime
# Mygtuku kodo prieiga
from UzregistruotiPasiimtaBLE import *
from DarbuotojuIrasai import *
from BLEIrasai import *
from ObjektuIrasai import *
# Elektroniniui pastui
import smtplib, ssl


# Prisijungimas prie duomenu bazes
mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        passwd="laukas12",
        database="BLE"
        )



# Is duomenu bazes istraukiami MacID BLED = BLUETOOT LOW ENERGY DATABASE
def DBS():
    BLED = []
    BLED1 = []

    for x in range(2):
        cursor = mydb.cursor()
        databases = ("show databases")
        cursor.execute("SELECT MacID FROM BLEirenginiai")
        myresult = str(cursor.fetchall()[x])
        BLED1.append(myresult)
        BLED.append(re.sub(r"[\,'(\)]",'',BLED1[x]))

    return BLED


def TrukstaB(BLED, BLE):
    TrukstaB =[]   # issaugojamas sarasas jeigu skanuoti rez != duomenu bazes
    TrukstaB = list(set(BLED) - set(BLE))
    return TrukstaB

def TrukstaSK(BLED, BLE):
    TrukstaSK = 0 # issaugoajams skaicius trukstamu BLE irenginiu
    TrukstaSK = len(list(set(BLED) - set(BLE)))
    return TrukstaSK

def NetrukstaB(BLED, BLE):
    NetrukstaB =[]   # issaugojamas sarasas jeigu skanuoti rez != duomenu bazes
    NetrukstaB = list(set(BLED) & set(BLE))
    return NetrukstaB

def NetrukstaSK(BLED, BLE):
    NetrukstaSK = 0 # issaugoajams skaicius trukstamu BLE irenginiu
    NetrukstaSK = len(list(set(BLED) & set(BLE)))
    return NetrukstaSK








def main():
    
    # sukuriamas pagrindinis langas
    root1 = Tk()
    root1.title('Bluetooth Skenavimas')
    root1.geometry("970x650")
    
    
    
    
    
    #globals
    global Mainframe
    global frame
    global after_id
    global label_Stop
    global T
    global PMACID
    
    PMACID = ""
    T = False
    after_id = None # loop sustabdymas
    #frames
    Mainframe = LabelFrame(root1, text="BLE Skenavimas",padx=60,pady=60)
    Mainframe.grid(row=2, column=0)
    frame = Frame(Mainframe)
    Secondframe = LabelFrame(root1,text="Menu",padx=60,pady=60)
    Secondframe.grid(row=0, column=0)
    Thirdframe = LabelFrame(root1,text="BLEirasai",padx=60,pady=60)
    Thirdframe.grid(row=0, column=1) 
    label_Stop= Label(Mainframe)
    
    # menu mygtukai
    Button(Secondframe, text= "Uzregistruoti pasiimta BLE", command=UPBLE).grid(row=0, column=0, columnspan= 2,pady=10, padx=10, ipadx=10)
    Button(Secondframe, text= "Darbuotoju irasai", command=DIBLE).grid(row=1, column=0, columnspan= 1,pady=10, padx=50, ipadx=42)
    Button(Secondframe, text= "BLE irasai", command=BIBLE).grid(row=2, column=0, columnspan= 1,pady=10, padx=50, ipadx=68)
    Button(Secondframe, text= "Objektu irasai", command=OIBLE).grid(row=3, column=0, columnspan= 1,pady=10, padx=50, ipadx=52)


    
     # issiusti gmail zinute
    def GmailS():
        
        now = datetime.datetime.now()
        data = str(now.strftime("%Y-%m-%d %H:%M"))
                                    
        global PMACID
        print ("WTF")
        print (PMACID)
        smtp_server = "smtp.gmail.com"
        sender_email = "mantas.me7921@go.kauko.lt"
        receiver_email = "mantas.me7921@go.kauko.lt"
        TEXT = "NERASTAS BLE IRENGINYS \n"  + PMACID + "\n " + data
        
        SUBJECT = "NERASTAS BLE IRENGINYS" 
        
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    

        port = 587  # For SSL
        password = "Laukas33"

        # Create a secure SSL context


        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server, port)
        server
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        
        server.sendmail(sender_email, receiver_email, message)
    
    
    
# funkcijos
    def BLETikrinti():# tikrina ar BLE irenginys buvo pasiimtias jei taip uzfiksuojama duomenu
        BLEID = []
        PBLEID = ["999"]
        snum = 0
        
        cursor = mydb.cursor()
        cursor.execute("SELECT BleID FROM BLEirenginiai")
        myresult = cursor.fetchall()
        for index, x in enumerate(myresult):
            num = 0
            id_reference = str(x[0])
            for y in x:
                BLEID.append(y)
                num += 1
                snum = num
             
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM PasiimtoObjektoInformacija")
        myresult1 = cursor.fetchall()
        for index, x in enumerate(myresult1):
            num = 0
            id_reference = str(x[0])
            for y in x:
                if(num == 3):
                    mydb.commit()
                    PBLEID.append(y)
                    #print(BLEID)
                num += 1
                
                
        for x in BLEID:
            num = 0
            for y in PBLEID:
                #print( x, y)
                if( x == y):
                    cursor = mydb.cursor()
                    cursor.execute("Update BLEirenginiai SET Vieta = %s WHERE BleID = %s", ("Pasiimtas", y,))
                    mydb.commit()               
                #else:
                    #cursor = mydb.cursor()
                   #cursor.execute("Update BLEirenginiai SET Vieta = %s WHERE BleID = %s", ("Sandelyje", x,))
                    #mydb.commit()
                    
                    #print (num)
                num +=1 
        
        #return BLEID
    global GL, RL, JL
    GL = Label(Thirdframe)
    RL = Label(Thirdframe)
    JL = Label(Thirdframe)
    
    def Stebeti():
        BLETikrinti()
        global GL, RL, JL
        GL.destroy()
        JL.destroy()
        RL.destroy()
        ID = ""
        Mac = ""
        Vieta = ""
        Busena = ""
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM BLEirenginiai")
        myresult = cursor.fetchall()
        for index, x in enumerate(myresult):
            num = 0
            id_reference = str(x[0])
            for y in x:
                if((num) == 0):
                    ID = y
                    
                if((num) == 1):
                    Mac = y
                    
                if((num) == 2):
                    #str(y)
                    Busena = y
                    #print(Busena)
                    
                if((num) == 3):
                    Vieta = y
                
                
                
                if(str(Vieta) == "{'Sandelyje'}" and num == 3):
                    Vieta = "Sandelyje"
                    GL = Label(Thirdframe, text=str(Mac) + " "+ Vieta , fg = "green")
                    GL.grid(row=index, column=0)
                    Vieta = ""
                if(str(Vieta) == "{'Pasiimtas'}" and num == 3):
                    Vieta = "Pasiimtas"
                    JL = Label(Thirdframe, text=str(Mac) + " "+ Vieta) 
                    JL.grid(row=index, column=0)
                    Vieta = ""
                if(str(Vieta) == "{'Truksta'}" and num == 3):
                    Vieta = "Truksta"
                    GL = Label(Thirdframe, text=str(Mac) + " "+ Vieta, fg = "red") 
                    GL.grid(row=index, column=0)
                    Vieta = ""

                
                
                    
                num +=1
                
                
        
        
        #JL = Label(Thirdframe, text="aa",)
        #JL.grid(row=1, column=0)
        
        #RL = Label(Thirdframe, text="aa", fg = "Red")
        #RL.grid(row=2, column=0)

    #Button update
    Button(Thirdframe, text= "Atnaujinti", command=Stebeti).grid(row=10, column=0, columnspan= 2,pady=10, padx=10, ipadx=10)
    Stebeti()
    
    
    def Start():
        global T
        T = True          # pradeda pagrindini algoritma
        BLEmain()
        Stebeti()
        

    def Stop():
        global T
        global Mainframe
        global frame
        global label_Stop
        global after_id
        frame.destroy()
        label_Stop.destroy()
        frame = LabelFrame(Mainframe)
        label_Stop = Label(Mainframe, text="Skenavimas sustabdytas ")
        label_Stop.grid(row=5,column=0)
        root1.after_cancel(after_id)
        T = False
        


    # start ir stop mygtukai
    startB = Button(Mainframe, text= "start",command=Start)
    stopB = Button(Mainframe, text= "stop",command=Stop)
    startB.grid(row=6, column=0, columnspan= 1,pady=10, padx=10, ipadx=100)
    stopB.grid(row=7, column=0, columnspan= 1,pady=10, padx=10, ipadx=100)

    # skaiciuojamas laikas
    def SKL():
        global label_Stop
        global label
        global after_id
        global frame
        global T
        BLETikrinti()
        #root1.after_cancel(after_id)
        frame = LabelFrame(Mainframe)
        label_Stop= Label(Mainframe)
        start = time()
        if T == True:
            #root1.after_cancel(after_id)
            after_id = root1.after(20000, Start)
            T == False

    def Skenavimas():
        global Mainframe
        global frame
        global label_Stop
        label_Stop.destroy()
        frame.destroy()
        frame = LabelFrame(Mainframe)
        BLE = []
        i=0
        now = datetime.datetime.now()
        data = str(now.strftime("%Y-%m-%d %H:%M"))
        frame.grid(row=0,column=0)
        label1 = Label(frame, text=data + "   BLE irenginiai: ")
        label3 = Label(frame, text="   BLE irenginiu nerasta")
        service = DiscoveryService("hci0")
        devices = service.discover(4)
        #print(data + " BLE irenginiai: ")
        label1.grid(row=0,column=0)
        x = 1
        for address, name in devices.items():
            #print("name: {}, address: {}".format(name, address))
            x =  x + 1
            Label(frame, text="Mac ID : " + address).grid(row=x+1,column=0)
            #label2
            i = i+1
            BLE.append(address .format(address))

        if(i == 0):
            label3.grid(row=x,column=0)

        return BLE

# pagrindine funkicja
    def BLEmain():

        if mydb.is_connected():
            global label_Stop
            global after_id
            label_Stop.destroy()
            print('Connected to MySQL database')
            subprocess.call(["rfkill", "unblock", "bluetooth"])
            BLED = DBS()
            BLE = Skenavimas()
            if list(set(BLED) & set(BLE)) in BLED :
                for x1 in BLED:  # 2 = kiek BLE irenginiu yra naudojama
                    T2 = []
                    idg = str(x1)  # MACID
                    #print(hello)
                    #print(idg)
                    cursor = mydb.cursor()
                    cursor.execute("SELECT BleID FROM BLEirenginiai WHERE MacID =%s", (idg,))
                    myresult = str(cursor.fetchone())
                    TR2.append(re.sub(r"[\,'(\)]",'',myresult))
                    id3 = str(TR2[0])
                    cursor = mydb.cursor()
                    cursor.execute("Update BLEtruksta SET Data = %s, Matytas = %s, Truksta = %s, Pavojus = %s WHERE MacID = %s", ("0000-00-00", "0", "Ne", "Nera", id3,))
                    mydb.commit()
                    cursor = mydb.cursor()
                    cursor.execute("Update BLEirenginiai SET Busena = %s, Vieta = %s WHERE MacID = %s", ("Ijungtas", "Sandelyje", id2,))
                    mydb.commit()
                    T = True
                else:
                    T = False
                
            else:
                TB = []
                TSK = 0
                NSK = 0
                NB = []
                NB = NetrukstaB(BLED, BLE)
                NSK = NetrukstaSK(BLED, BLE)
                TB = TrukstaB(BLED, BLE)
                TSK = TrukstaSK(BLED, BLE)
                #print(NB)
                if(NSK > 0):  # Tikrina kiek buvo rastu  BLE irenginiiu
                    for i1 in BLED:
                        for j1 in range(NSK):
                            if(i1 == NB[j1]):
                                TR5 = []
                                id2 = NB[j1]
                                id2 = str(id2)
                                cursor = mydb.cursor()
                                cursor.execute("SELECT BleID FROM BLEirenginiai WHERE MacID =%s", (id2,))
                                myresult = str(cursor.fetchone())
                                TR5.append(re.sub(r"[\,'(\)]",'',myresult))
                                id5 = str(TR5[0])
                                print("cbb")
                                print(id5)
                                cursor = mydb.cursor()
                                cursor.execute("Update BLEtruksta SET Data = %s, Matytas = %s, Truksta = %s, Pavojus = %s WHERE MacID = %s", ("0000-00-00", "0", "Ne", "Nera", id5,))
                                mydb.commit()
                                cursor = mydb.cursor()
                                cursor.execute("Update BLEirenginiai SET Busena = %s, Vieta = %s WHERE MacID = %s", ("Ijungtas", "Sandelyje", id2,))
                                mydb.commit()
                                T = True
                    else:
                        T = False
                    
                if(TSK > 0): # Tikrina kiek buvo nerastu BLE irenginiu
                    for i1 in BLED:
                        for j1 in range(TSK):
                            if(i1 == TB[j1]):
                                global PMACID  # PMACID nusiusti per gmail jeigu pavojus
                                PMACID = TB[j1]
                                PMACID = str(PMACID)
                                DATA = []
                                kiek = []
                                TR= []
                                TR1= []
                                id1 = TB[j1]
                                id1 = str(id1)
                                cursor = mydb.cursor()
                                cursor.execute("SELECT BleID FROM BLEirenginiai WHERE MacID =%s", (id1,))
                                myresult = str(cursor.fetchone())
                                TR1.append(re.sub(r"[\,'(\)]",'',myresult))
                                id1 = str(TR1[0])
                                #print("ayayaya")
                                #print(id1)
                                cursor.execute("SELECT Truksta FROM BLEtruksta WHERE MacID =%s", (id1,))
                                myresult = str(cursor.fetchone())
                                TR.append(re.sub(r"[\,'(\)]",'',myresult))
                                tr = TR[0]
                                cursor.execute("SELECT Matytas FROM BLEtruksta WHERE MacID = %s", (id1,))
                                myresult = str(cursor.fetchone())
                                kiek.append(re.sub(r"[\,'(\)]",'',myresult))
                                sk = kiek[0]
                                #print(kiek)
                                sk = int(sk)
                                sk = sk+1
                                sk = str(sk)
                                cursor.execute("SELECT Data FROM BLEtruksta WHERE MacID = %s", (id1,))
                                myresult = str(cursor.fetchone())
                                DATA.append(re.sub(r"[\,'(\)]",'',myresult))
                                data = str(DATA[0])
                                #print(data, sk, id1)
                                cursor.execute("Update BLEtruksta SET Matytas = %s WHERE MacID = %s", (sk, id1))
                                mydb.commit()
                                if(sk == "1" and data == "0000-00-00"): # Kliausia ar 4 kartus is eiles buvo nerastas ireginys i rparaso kad truksta irenginio
                                    DATA = []
                                    VIETA = []
                                    BUSENA = []
                                    Pavojus = []
                                    #cursor.execute("Update BLEtruksta SET Truksta = %s WHERE MacID = %s", ("Taip", id1))
                                    #mydb.commit()
                                    ##print(data)
                                    #if(tr == "Taip" and sk == "4" and data == ""):
                                    now = datetime.datetime.now()
                                    data = str(now.strftime("%Y-%m-%d %H:%M"))
                                    cursor.execute("Update BLEtruksta SET Data = %s, Matytas = %s, Truksta = %s WHERE MacID = %s", (data, "0", "Taip", id1,))
                                    mydb.commit()
                                    #cursor.execute("Update BLEtruksta SET Matytas = %s WHERE MacID = %s", ("0", id1))
                                    #mydb.commit()
                        
                                    cursor.execute("SELECT Vieta FROM BLEirenginiai WHERE BleID = %s", (id1,))
                                    myresult = str(cursor.fetchone())
                                    VIETA.append(re.sub(r"[\,'(\)]",'',myresult))
                                    Vieta = str(VIETA[0])
                                    
                                    cursor.execute("SELECT Busena FROM BLEirenginiai WHERE BleID = %s", (id1,))
                                    myresult = str(cursor.fetchone())
                                    BUSENA.append(re.sub(r"[\,'(\)]",'',myresult))
                                    Busena = str(BUSENA[0])
                                    
                                    cursor.execute("SELECT Pavojus FROM BLEtruksta WHERE MacID = %s", (id1,))
                                    myresult = str(cursor.fetchone())
                                    Pavojus.append(re.sub(r"[\,'(\)]",'',myresult))
                                    Pavojus = str(Pavojus[0])
                                    
                                    T = True
                                    #print(Busena)
                                    if(Busena == "{Ijungtas}" and Vieta == "{Sandelyje}"):
                                        #padarom kad yra pavojus
                                        if Pavojus == "{Nera}":
                                            cursor.execute("Update BLEtruksta SET Pavojus = %s WHERE MacID = %s", ("Issiusta", id1,))
                                            mydb.commit()
                                            cursor = mydb.cursor()
                                            cursor.execute("Update BLEirenginiai SET Vieta = %s WHERE BleID = %s", ("Truksta", id1,))
                                            mydb.commit()
                                            #padarom kad yra pavojus
                                            #padarom kad pavojus = isssiusta
                                            #send MAIL GmailS()
                                            GmailS()
                                
                                else:
                                    if not(sk == "4" or sk == "0" or sk == "1" or sk == "2" or sk == "3"):
                                        cursor.execute("Update BLEtruksta SET Matytas = %s WHERE MacID = %s", ("0", id1))
                                        mydb.commit()
                                    T = True
                                    
                    else:
                        T = False                    #print("nezinau")
                    
        else:
            print("Nepavyko prisijungti prie duomenu bazes")

        SKL()
        
    #def on_closing():
        #root1.destroy()
        #DIBLE.destroy()

    #root1.protocol("WM_DELETE_WINDOW", on_closing)
    #DIBLE.protocol("WM_DELETE_WINDOW", on_closing)
    root1.mainloop()

    
