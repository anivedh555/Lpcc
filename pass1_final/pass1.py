import os

LC=0

mnemonics={'STOP':('00','IS',0),'ADD':('01','IS',2),'SUB':('02','IS',2),'MUL':('03','IS',2),'MOVER':('04','IS',2),'MOVEM':('05','IS',2),'COMP':('06','IS',2),'BC':('07','IS',2),'DIV':('08','IS',2),'READ':('09','IS',1),'PRINT':('10','IS',1),'LTORG':('05','AD',0),'ORIGIN':('03','AD',1),'START':('01','AD',1),'EQU':('04','AD',2),'DS':('01','DL',1),'DC':('02','DL',1),'END':('AD',0)}

file=open("input.txt","a")

ifp=open("intermed.txt","a")

ifp.truncate(0)

REG={'AREG':1,'BREG':2,'CREG':3,'DREG':4}

lit=open("literals.txt","a+")
lit.truncate(0)

tmp=open("tmp.txt","a+")

tmp.truncate(0)

symtab={}
pooltab=[]
words=[]


#literal_tab
def littab():
    print("literal table:")
    lit.seek(0,0)
    for x in lit:
        print(x)

def pooltab2():
    global pooltab
    print("Pool Table:")
    print(pooltab)

def symbol():
    global symtab
    print("Symbol Table:")
    print(symtab)

def END():
    global LC
    pool=0
    z=0
    ifp.write("\t(AD,02)\n")
    lit.seek(0,0)
    for x in lit:
        if "**" in x:
            pool+=1
            if pool==1:
                pooltab.append(z)
            y=x.split()
            tmp.write(y[0]+"\t"=str(LC)+"\n")
            LC+=1
        else:
            tmp.write(x)
        z+=1
        lit.truncate(0)
        tmp.seek(0,0)
        for x in tmp:
            lit.write(x)
        tmp.truncate(0)

def LTORG():
    global LC
    pool=0
    z=0
    lit.seek(0,0)
    x=lit.readlines()
    i=0
    while(i<len(x)):
        f=[]
        if("**" in x[i])




