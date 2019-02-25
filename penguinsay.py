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
#   _
# ('v')
#//-=-\\
#(\_=_/)
# ^^ ^^
#================================================================================

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

def main():
    logger = logging.getLogger() 
    logger.setLevel(logging.CRITICAL)
    chatbot = ChatBot('Penguin', trainer='chatterbot.trainers.ListTrainer')
    text = ''
    #text = input()
    #response = chatbot.get_response(text)
    #printResponse(response.text)
    #print(response)
    #drawACutePenguin('-n')
    while(text != 'Good bye'):
        text = input()
        response = chatbot.get_response(text)
        printResponse(response.text)
        drawACutePenguin('-n')

def drawACutePenguin(mode):
    if(mode == "-n"):
        print(" \033[1;34m  _\033[0m")
        print(" \033[1;34m(\033[0m\'\033[1;33mv\033[0m\'\033[1;34m)\033[0m")
        print("\033[1;34m/\033[0m/-=-\\\033[1;34m\\\033[0m")
        print("\033[1;34m(\033[0m\\_=_/\033[1;34m)\033[0m")
        print(" \033[1;33m^^ ^^\033[0m")
    if(mode == "-marxism"):
        print(" \033[1;31m  __\033[0m")
        print(" \033[1;31m(☭\033[1;33m v\033[1;31m☭\033[1;31m)\033[0m")
        print("\033[1;31m/\033[0m/-=-\\\033[1;31m\\\033[0m")
        print("\033[1;31m(\033[0m\\_=_/\033[1;31m)\033[0m")
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
    #printResponse("haha432423 33333333333 33333333333333 333333333333333333")
    #drawACutePenguin('-n') 
    main()
