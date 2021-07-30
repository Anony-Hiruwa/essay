# CODE BY HIRUWA
from os import system as sys
import time

# banner
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
print( ban )
print( det )

# essay quizz
wel = ('\033[92m' "WELCOME TO ESSAY TOOL BY HIRUWA")
print( wel.center( 70 ) )

fname = input( '\033[93m'"What is Your FIRST NAME : " )
lname = input( '\033[93m'"What is Your LAST NAME  : " )
agey = int( input( '\033[93m'"What is Your Birth Year  : " ) )
age = 2021 - (agey)
if age < 100 :
    print( '\033[091m', fname,"Your Age is : ",age )
else:
    print('\033[091m',fname,"YOU ENTERD WRONG ANSWER !!!!!" )
    agey = int( input( '\033[93m'"What is Your Birth Year  : " ) )
    if age < 100 :
        print( '\033[091m',fname,"Your Age is : ",age )
    else :
        print("YOU ENTERD WRONG ANSWER !!!!!  PROGRAM HAS STOPED")
        time.sleep(2)
        sys("exit")

ad = input( '\033[93m' "What is your Addres : " )
ju = input( '\033[93m'"You junior or senior student in your School : " )
mj = input( "Your mother Job : " )
fj = input( "Your father Job : " )
fs = input( "What is your favourit subject : " )
pn = input( "What is your favourit name in your name ' PET NAME ' : " )

# system cmd
sys( "clear" )

# output
print( "YOUR ESSAY IS ON PROGRESS ... Please wait few sec.........".center( 50 ) )
time.sleep( 4 )
print( ' \033[92m' "MY SELF".center( 70 ) )
print( "" )
print( '\033[92m' "My name is",fname,lname,".","I am a",ju,"in my school.I am also the youngest child in my family.",
       "I live in",ad,"My mum is a",mj,"and my dad is a",fj,
       "\nIt is a common knowledge that I am a good student and I love to study a lot.","My favorite subjects is",fs,
       "I’m what a lot of people call a",pn,
       "I have every intention of applying to a reputable university and obtaining a degree in one of these fields.I am responsible and hardworking, so I study hard to obtain good grades.\n\n",
       "I have always been treated like a baby, by my parents, siblings, teachers and basically everyone who is not in my age group.Sometimes even my friends talk to me like I am a child, which is why I basically love school and reading books.Books don’t talk back at you and they make me feel important in this gigantic universe.\n\nThis is not to say that I don’t love all the care and attention. I do, it’s just that sometimes it can get stifling. However, I am quite content with my life." )
