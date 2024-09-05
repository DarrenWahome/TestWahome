import random

char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy1234567890~!@#$%^&*()_+=-`{][}\|:;/?.><,'


PassCount = 0
AllPass = []

def makepass(LenOfPSWD):
    global PassCount

    passwd = ''
    i = 0
    PassCount += 1
    while i < LenOfPSWD:
        passwd = passwd + random.choice(char)
        i += 1

    return passwd
def SavePass(Passwd,count):
    global AllPass

    AllPass.append(f"Password {count}: {Passwd}")

while True:
    lenofpswd = int(input('Length of password: '))
    if lenofpswd == 0:
        print('')
        for i in AllPass:
            print(i)
        exit()
    SavePass(makepass(lenofpswd),PassCount)
