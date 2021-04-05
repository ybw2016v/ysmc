#!/usr/bin/python3

import time
import subprocess
import sys
import json

dfile=sys.argv[1]

divdog={}
with open('default.json') as cdog:
    jsondog=cdog.read()
    divdog=json.loads(jsondog)
X0=divdog['x0']
Y0=divdog['y0']
dX=divdog['dx']
dY=divdog['dy']

def tapdog(N):
    """
    按键
    """
    y,x=divmod(N,7)
    tx=x*dX + X0
    ty=Y0 + dY*y 
    subprocess.Popen('adb shell input tap {} {}'.format(tx,ty), shell=True)
    print([tx,ty])
    pass



# P='1155665 4433221 5544332 5544332 1155665 4433221'

# for sd in P:
#     print(sd)
#     if sd.isdigit():
#         tapdog(int(sd)+6)
#         # pass
#     # tapdog(int(sd)+6)
#     time.sleep(0.3)
#     pass

def tandog(pudog):
    """
    按键与延时
    """
    lidog=pudog[0]
    for skk in lidog:
        tapdog(skk)
        pass
    time.sleep(pudog[1])
    pass
dT=0.15
sl = open(dfile)
lli=sl.readlines()
uo=[]
for cj in lli:
    if cj[0]=='T':
        ddT=cj.split('=')
        dT=float(ddT[1])
        print(cj)
    elif cj[0]=='\n' or cj[0]=='#':
        pass
    else:
        llo =[]
        for iiu in cj.split():
            if iiu[0]=='\n':
                pass
            elif iiu[0]=='0':
                # llo.append([[],dT])
                pass
            elif iiu[0]=='+':
                jj=int(iiu[1])+13
                # llo.append([[jj],dT])
                llo.append(jj)
            elif iiu[0]=='-':
                jj=int(iiu[1])-1
                # llo.append([[jj],dT])
                llo.append(jj)
            else:
                jj=int(iiu[0])+6
                # llo.append([[jj],dT])
                llo.append(jj)
        uo.append([llo,dT])

print(uo)
for ppo in uo:
    tandog(ppo)