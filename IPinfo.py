import requests  as reqs 
import socket , time 
from colorama import Fore , init
init()

a1 = "██╗██████╗░  ██╗███╗░░██╗███████╗░█████╗░\n "
a2 = "██║██╔══██╗  ██║████╗░██║██╔════╝██╔══██╗\n "
a3 = "██║██████╔╝  ██║██╔██╗██║█████╗░░██║░░██║\n "
a4 = "██║██╔═══╝░  ██║██║╚████║██╔══╝░░██║░░██║\n "
a5 = "██║██║░░░░░  ██║██║░╚███║██║░░░░░╚█████╔╝\n "
a6 = "╚═╝╚═╝░░░░░  ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░   "
credit = "------  [+] Tool by GHOSTH4CK3R -------\n"

asciiart = a1 + a2 + a3 + a4 + a5 + a6
print(Fore.GREEN + "\n",asciiart)
print(Fore.LIGHTBLUE_EX + "\n",credit)

try: 
    ip = socket.gethostbyname("www.google.com")
    print(Fore.LIGHTGREEN_EX + "# Internet : Active")    
except Exception as e:
    
    print(Fore.LIGHTRED_EX + "  !!No Internet !! \nExitting in 10 seconds")  
    time.sleep(10)
    exit()
print(Fore.LIGHTCYAN_EX + "")
url = "https://ipinfo.io"
print("1. Check your ip info ")
print("2. Check somene's ip info  \n")

choice = input("Choice (1 or 2) > ")

if choice == "1":
    print(Fore.LIGHTBLUE_EX + "\n****Your Ip Info****\n")
    resp = reqs.get(url)
    alldata = resp.json()
    
    IP = alldata.get('ip')
    CT = alldata.get('city')
    RG = alldata.get('region')
    CY = alldata.get('country')
    LOC = alldata.get('loc')
    POS = alldata.get('postal')
    TZ = alldata.get('timezone')
    
    print(Fore.LIGHTCYAN_EX + "IP Address :",IP)
    print("City :",CT)
    print("Region :",RG)
    print("Country :",CY)
    print("Location :",LOC)
    print("Postal Code :",POS)
    print("Time Zone :",TZ)

elif choice == "2":
    print(Fore.LIGHTBLUE_EX + "\n***Someone's Ip Info****\n")
    Sip = input("Enter ip address : ")
    url = url+"/"+Sip
    
    resp = reqs.get(url)
    alldata = resp.json()
    
    IP = alldata.get('ip')
    CT = alldata.get('city')
    RG = alldata.get('region')
    CY = alldata.get('country')
    LOC = alldata.get('loc')
    POS = alldata.get('postal')
    TZ = alldata.get('timezone')
    
    print(Fore.LIGHTCYAN_EX + "\nIP Address :",IP)
    print("City :",CT)
    print("Region :",RG)
    print("Country :",CY)
    print("Location :",LOC)
    print("Postal Code :",POS)
    print("Time Zone :",TZ)

else:
    print("Invalid choice , input 1 or 2")    



input("\nExit >")