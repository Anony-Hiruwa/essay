                    #CODE BY HIRUWA
from colorama import Fore, init

#color
init()
colours = {
     'green' : Fore.LIGHTGREEN_EX,
     'darkgreen' : Fore.GREEN,
     'cyan' : Fore.LIGHTCYAN_EX,
     'red' : Fore.LIGHTRED_EX,
     'magenta' : Fore.LIGHTMAGENTA_EX,
     'yellow' : Fore.LIGHTYELLOW_EX,
     'white' : Fore.LIGHTWHITE_EX,
     'darkyellow' : Fore.YELLOW
}

#banner
ban = '''

\033[31m███████╗███████╗███████╗ █████╗ ██╗   ██╗
\033[93m██╔════╝██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝
\033[93m█████╗  ███████╗███████╗███████║ ╚████╔╝ 
\033[93m██╔══╝  ╚════██║╚════██║██╔══██║  ╚██╔╝  
\033[93m███████╗███████║███████║██║  ██║   ██║   
\033[31m╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝     V1.0
                                         
'''
det = '''\033[91m===================================================================
|                                                                  |
|                            \033[93mESSAY TOOL                            \033[91m|
\033[91m|                                                                  |
\033[91m|\033[93m[+] OWNER : HIRUWA                                                \033[91m|
\033[91m|                                                                  |
\033[91m|\033[93m[+] THIS TOOL BE GENERATE 100 WORD ESSAY...                       \033[91m|
\033[91m|                                                  V1.0            |
==================================================================='''
print(ban)
print(det)
wel=( '\033[92m' "")
print (wel.center(70))
fname=input( '\033[33m'  "What is Your FIRST NAME : ")
lname=input( '\033[33m' "What is Your LAST NAME  : ")
print("")
agey=int(input( '\033[33m'  "What is Your Birth Year  : "))
age = 2021 - (agey)
ad=input('\033[33m' "What is your Addres : ")
ju=int(input( '\033[33m'  "You junior or senior student in your School : "))
print("")
print(' \033[33m' "MY SELF".center(70))
print('"')
print('\033[92m' "My name is",fname,lname,".","I am a",ju,"in my school.I am also the youngest child in my family.","I have two older brothers and two older sisters.")
