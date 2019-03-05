#________________________________________________________________________________
#   Penguin say
#   23 Feb 2019 
#
#
#
#________________________________________________________________________________
#
#        .---------------------.
#       ' Text show here !!!!!!'
#       '.____________________.'
#       /
#   __
# ( 'v')  
#//-=-\\
#(\_=_/)  
# ^^ ^^
#================================================================================

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("say", help="Talk To The Penguin")
    parser.add_argument("-l","--loop",action="store_true",help="Loop mode: say 'Good bye' to exit")
    parser.add_argument("-m","--mode", help="Modes: kmarxpen, normal, greed, bigeye1, bigeye2,..")
    args = parser.parse_args()
    logger = logging.getLogger() 
    logger.setLevel(logging.CRITICAL)
    chatbot = ChatBot('Penguin', trainer='chatterbot.trainers.ListTrainer')
    talk(chatbot, args) 

def talk(chatbot, args):    
    text = args.say
    response = chatbot.get_response(text)
    printResponse(response.text)
    drawACutePenguin(args.mode)
    if(args.loop):
        text = ''
        print("\033[1;36mYou're in looping mode. Say anything. \nSay 'Good bye' if you want to exit...\033[0m")
        while(text != 'Good bye'):
            text = input()
            response = chatbot.get_response(text)
            printResponse(response.text)
            drawACutePenguin(args.mode)

def drawACutePenguin(mode):
    if(mode == "kmarxpen"):
        print(" \033[1;31m  __\033[0m")
        print(" \033[1;31m(☭\033[1;33m v\033[1;31m☭\033[1;31m)\033[0m")
        print("\033[1;31m/\033[0m/-=-\\\033[1;31m\\\033[0m")
        print("\033[1;31m(\033[0m\\_=_/\033[1;31m)\033[0m")
        print(" \033[1;33m^^ ^^\033[0m")
    elif(mode == "greed"):
        print(" \033[1;34m  __\033[0m")
        print(" \033[1;34m(\033[33m $v$\033[1;34m)\033[0m")
        print("\033[1;34m/\033[0m/-=-\\\033[1;34m\\\033[0m")
        print("\033[1;34m(\033[0m\\_=_/\033[1;34m)\033[0m")
        print(" \033[1;33m^^ ^^\033[0m")
    elif(mode == "bigeye1"):
        print(" \033[1;34m  __\033[0m")
        print(" \033[1;34m(\033[0m @\033[1;33mv\033[0m@\033[1;34m)\033[0m")
        print("\033[1;34m/\033[0m/-=-\\\033[1;34m\\\033[0m")
        print("\033[1;34m(\033[0m\\_=_/\033[1;34m)\033[0m")
        print(" \033[1;33m^^ ^^\033[0m") 
    elif(mode == "bigeye2"):
        print(" \033[1;34m  __\033[0m")
        print(" \033[1;34m(\033[0m 0\033[1;33mv\033[0m0\033[1;34m)\033[0m")
        print("\033[1;34m/\033[0m/-=-\\\033[1;34m\\\033[0m")
        print("\033[1;34m(\033[0m\\_=_/\033[1;34m)\033[0m")
        print(" \033[1;33m^^ ^^\033[0m")
    elif(mode == "bigeye3"):
        print(" \033[1;34m  __\033[0m")
        print(" \033[1;34m(\033[0m O\033[1;33mv\033[0mO\033[1;34m)\033[0m")
        print("\033[1;34m/\033[0m/-=-\\\033[1;34m\\\033[0m")
        print("\033[1;34m(\033[0m\\_=_/\033[1;34m)\033[0m")
        print(" \033[1;33m^^ ^^\033[0m")
    elif(mode == "bigeye4"):
        print(" \033[1;34m  __\033[0m")
        print(" \033[1;34m(\033[0m Q\033[1;33mv\033[0mQ\033[1;34m)\033[0m")
        print("\033[1;34m/\033[0m/-=-\\\033[1;34m\\\033[0m")
        print("\033[1;34m(\033[0m\\_=_/\033[1;34m)\033[0m")
        print(" \033[1;33m^^ ^^\033[0m")
    elif(mode == "samurai"):
        print(" \033[1;33m <<_>>\033[0m")
        print(" \033[1;34m(\033[0m \\\033[1;33mv\033[0m/\033[1;34m)\033[0m")
        print("\033[1;34m/\033[0m/-=-\\\033[1;34m\\\033[0m")
        print("\033[1;34m(\033[0m\\_=_/\033[1;34m)\033[0m")
        print(" \033[1;33m^^ ^^\033[0m")
    else:
        print(" \033[1;34m  __\033[0m")
        print(" \033[1;34m(\033[0m '\033[1;33mv\033[0m\'\033[1;34m)\033[0m")
        print("\033[1;34m/\033[0m/-=-\\\033[1;34m\\\033[0m")
        print("\033[1;34m(\033[0m\\_=_/\033[1;34m)\033[0m")
        print(" \033[1;33m^^ ^^\033[0m")

def printResponse(responseText):
    length = len(responseText)
    i = length if length <= 34 else 34
    edge = '         .' + '-'*i + '.'
    print(edge)
    ttext = responseText.split(" ")
    text = [""]
    for c in ttext:
        if(len(c + text[-1]) > i):
            text[-1] += (i + 1 - len(text[-1]))*' '
            text.append("")
        text[-1]+= ' ' + c
    text[-1] += (i + 1 - len(text[-1]))*' '
    #print(text)
    for x in text:
        print('        \'' + x + '\'')
    edge = '        \'.' + '-'*(i-1) + '.\''
    print(edge.replace('-','_'))
    print('        /')
if __name__ == '__main__': 
    main()
