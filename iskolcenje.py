#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import math
from koordinate import *

#A->B

staro=open(("gps.txt"),"r")
novo=open("elementi.txt","w+")


razdjelnik=" "

a=staro.readline()
rbr, y, x, z=a.split(razdjelnik)
s=Point(rbr,float(y),float(x),float(z))

a=staro.readline()
rbr, y, x, z=a.split(razdjelnik)
o=Point(rbr,float(y),float(x),float(z))


novo.write(s.rbr+"-->"+o.rbr)
novo.write("\n")
novo.write("koordinate stajalista:")
novo.write(str(s.y)+" "+str(s.x))
novo.write("\n")
novo.write("koordinate orijentacije:")
novo.write(str(o.y)+" "+str(o.x))
novo.write("\n"*2)

while True:
	
	a=staro.readline()

	if not a:
		break


	#definiranje detaljne tocke
	
	rbr, y, x, z=a.split(razdjelnik)
	c=Point(rbr,float(y),float(x),float(z))

	#racunanje pravca
	alfa=s.smjerni(c)-s.smjerni(o)
	if alfa==0.:
		alfa=0.
	elif alfa<0.:
		alfa+=math.pi*2.
	elif alfa>=2.*math.pi:
		alfa-=math.pi*2.

	#racunanje duljine
	d=round(s.duljina(c),3)
	
	#alfa je za stajaliste svaki pravac jer je duljina 0
	kut_DEG=alfa*180./math.pi
	
	kut_D=int(kut_DEG)
	temp=60.*(kut_DEG-kut_D)
	kut_M=int(temp)
	kut_S=int(math.ceil(60.*(temp-kut_M)))
	kut=str(kut_D)+"-"+str(kut_M)+"-"+str(kut_S)


	novo.write(c.rbr)
	novo.write("|")
	novo.write(str(d))
	novo.write("|")
	novo.write(str(kut))
	novo.write("|")
	novo.write("\n")

staro.close()
novo.close()


