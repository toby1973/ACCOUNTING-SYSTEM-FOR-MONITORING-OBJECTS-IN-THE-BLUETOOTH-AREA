import smtplib, ssl




def GmailS():
    global Yolo
    print (Yolo)
    smtp_server = "smtp.gmail.com"
    sender_email = "mantas.me7921@go.kauko.lt"
    receiver_email = "Juppy.u@gmail.com"
    TEXT = "NERASTAS BLE IRENGINYS"
    
    SUBJECT = "NERASTAS BLE IRENGINYS \n" + Yolo 
    
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
        
    #server.sendmail(sender_email, receiver_email, message)
    
#GmailS(PMACID)