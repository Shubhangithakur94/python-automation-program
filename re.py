import os
print("\n....THIS IS WORLD OF AUTOMATION......")
while True:
    print("\n HOW CAN I HELP YOU PLZ SELECT YOUR QUERY")
    print("\n Here we provide some options: ")
    print("""\t option 91: Run date command.""")
    print("""\t option 52: Run time command.""")
    print("\t option 83: check my ip address")
    print("\t option 54: check your files")
    print("\t option 11: get host name ")
    print("\t option 120: get mac address")
    
    

    query = int(input("select your choice: "))
    if query==91:
        date=os.system("date")
        print(date)

    elif query==52:
        time=os.system("time") 
        print(time)

    elif query==83:
        ip=os.system("ipconfig")
        print(ip)

    elif query==54:
        dir=os.system("dir")
        print(dir)
        
    elif query==11:
        hostname=os.system("hostname") 
        print(hostname) 

    elif query==120:
        getmac=os.system("getmac")   
        print(getmac)

    
    '''elif query==138:
        arp=os.system("arp -a")
        print(arp)

    elif query==44:
         assoc=os.system("assoc")    
         print(assoc)

    elif query==55:
         ping=os.system("ping ")    
         print(ping) 

    elif query==45:
         cipher=os.system("cipher")    
         print(cipher)

    elif query==78:
         driverquery=os.system("driverquery")    
         print(driverquery)

    elif query==79:
         netstat=os.system("netstat")    
         print(netstat)     

    elif query==100:
        shutdown=os.system("shutdown")
        print(shutdown)  '''    
    
else:
        print("enter a valid input")



