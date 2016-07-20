#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import math
import re
from mpmath import mp
mp.dps = 50

#definiranje klase tocka
class Point (object):

	def __init__(self,rbr,y,x,z):
		
		self.rbr = str(rbr)
		self.y = float(y)
		self.x = float(x)
		self.z = float(z)

	def smjerni(self,other):
		
		dy = (other.y)-(self.y)
		dx = (other.x)-(self.x)

		if dx==0.:
		
			if dy==0.:
				s_kut=0.
				return s_kut

			elif other.y<self.y:
				s_kut=math.pi/2.
				return s_kut

			elif self.y<other.y:
				s_kut=math.pi+math.pi/2.
				return s_kut

	#1. kvadrant dy+  dx+
		elif dy>=0. and dx>=0. :
			s_kut=mp.atan(dy/dx)
			return s_kut
		

	#2. kvadrant dy+  dx-
		elif dy>=0. and dx<=0.:
			s_kut=mp.atan(dy/dx)+math.pi
			return s_kut
		

	#3. kvadrant dy-  dx-
		elif dy<=0. and dx<=0.:
			s_kut=mp.atan(dy/dx)+math.pi
			return s_kut
		

	#4. kvadrant dy-  dx+
		elif dy<=0. and dx>=0. :
			s_kut=mp.atan(dy/dx)+math.pi*2.
			return s_kut

	#definiranje funkcije duljine
	def duljina(self,other):
		
		dy=(other.y)-(self.y)
		dx=(other.x)-(self.x)
		duljina=math.sqrt(dy**2+dx**2)
		return duljina

	#definiranje zbroja
	def __add__(self,other):
		zbroj = Point("zbroj:"+str(self.rbr)+"_"+str(other.rbr), self.y+other.y, self.x+other.x, self.z+other.z)
		return zbroj

	#definiranje printanja tocke
	def __str__(self):
		return str(self.rbr)+" "+str(self.y)+" "+str(self.x)+" "+str(self.z)

	#definiranje oduzimanja
	def __sub__(self, other):
		minus = Point("minus:"+str(self.rbr)+"_"+str(other.rbr), self.y-other.y, self.x-other.x, self.z-other.z)
		return minus