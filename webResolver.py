import socket, time, os, random

szinVege = '\x1b[0m'
os.system("cls")
def main():
    elsosor = '\x1b[0;30;47m'+"copyright: yrogerg#1834"+szinVege
    print(elsosor)
    print("Adj meg egy weboldal címet, http(s) nélkül!\nLásd például: \"google.com\" vagy \"www.google.com\"\n")
    hostname = input("Weboldal címe: "+'\033[95m')
    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        os.system("cls")
        print(szinVege+'\033[91m'+"Helytelen kiszolgálónév, próbáld újra!"+'\033[0m')
        main()
    def continyu():
        print(szinVege+"IP cím: "+'\033[96m'+ip+szinVege+"\n\nSzeretnéd folytatni? (Y,N)")
        con = input("Te: "+'\033[93m')
        if con.lower() == "y":
            os.system("cls")
            main()
        elif con.lower() == "n":
            i = 3
            while i != 0:
                os.system("cls")
                print(szinVege+"A program "+'\033[96m'+str(i)+szinVege+" másodpercen belül leáll.")
                time.sleep(1)
                i -= 1
            if i == 0:
                os.system("cls")
                exit()
        list = ["y","n"]
        if con.lower() not in list:
            def continyu2():
                os.system("cls")
                print('\x1b[0;30;47m'+"copyright: yrogerg#1834"+szinVege)
                print("Adj meg egy weboldal címet, http(s) nélkül!\nLásd például: \"google.com\" vagy \"www.google.com\"\n")
                print("Weboldal címe: "+'\033[95m'+hostname)
                print(szinVege+"IP cím: "+'\033[96m'+ip+szinVege+"\n\nSzeretnéd folytatni?"+'\033[91m'+" (Y,N)"+szinVege)
                con = input("Te: "+'\033[93m')
                if con == "y" or con == "Y":
                    os.system("cls")
                    main()
                elif con == "n" or con == "N":
                    i = 3
                    while i != 0:
                        os.system("cls")
                        print(szinVege+"A program "+'\033[96m'+str(i)+szinVege+" másodpercen belül leáll.")
                        time.sleep(1)
                        i -= 1
                    if i == 0:
                        os.system("cls")
                if con not in list:
                    continyu2()
            continyu2()
    continyu()
main()
def exit():
    exit()
