import time
import os
from pygame import mixer  # Load the popular external library

sHolyName = ""
nVertiCross = 0
nHoziCross = 0

def checkHorizontalNum(nNum):
    nValue = int(nNum) % 2
    if nValue == 1:
        return True
    else:
        return False

def getCommandDisplay(nMode):
    switcher = {
                    0:'Input Holy Name: ',
                    1:'Input vertical of Cross: ',
                    2:'Input horizontal of Cross:',    
                }
    return switcher.get(nMode,"Invalid string")        

def doCommand(nMode):
    global sHolyName
    global nVertiCross
    global nHoziCross
    while True:
        print(getCommandDisplay(nMode))
        if nMode == 0:
            sHolyName = input()
            if len(sHolyName) > 0:
                break
        elif nMode == 1:
            nVertiCross = input(int)
            if int(nVertiCross) > 11:
                break;
        else:
            nHoziCross = input()
            if int(nHoziCross) * 3 < int(nVertiCross) and checkHorizontalNum(nHoziCross) == True and int(nHoziCross) > 2:
                break
def showCross():
    global sHolyName
    global nVertiCross
    global nHoziCross
    nMaxTopCross = int(nVertiCross) / 4
    nCnt = 0
    nMaxLen = len(sHolyName) * int(nHoziCross)
    for x in range(int(nVertiCross)):
        time.sleep(0.5)
        if x >= round(nMaxTopCross) and x <= round(nMaxTopCross) + 1:
            nCnt += 1
            print(sHolyName * int(nHoziCross))
        else:
            print((sHolyName).center(nMaxLen, ' '))


def main():
    os.system("cls")
    mixer.init()
    mixer.music.load('C:/Users/user/Downloads/SchubertAveMaria.mp3')
    mixer.music.play()
    x = 0
    for x in range(3):
        doCommand(x)
    showCross()             
main()