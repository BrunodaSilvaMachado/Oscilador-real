#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

class Oscilador(object):

	def __init__(self,dt = 0.01):
		self.x = [1] 	#Amplitude
		self.v = [0] 	#Velocidade inicial
		self.e = [0.5] 	#energia inicial
		self.t = [0] 	#tempo
		self.dt = dt	#variacao de tempo
		self.km = 1		#w^2 quadrado da velocidade
		self.fat = 0 	#forca de atrito
	#setter
	def setRanger(self,rng):
		self._rng = rng
	def setdt(self,dt):
		self.dt = dt
	def setX(self,x):
		self.x = [x]
	def setV(self,v):
		self.v = [v]
	def setE(self,e):
		self.e = [e]
	def setKM(self,km):
		self.km = km
	def setT(self,t):
		self.t = [t]
	def setFat(self,fat):
		self.fat = fat
	#getter
	def getT(self):
		return self.t
	#functions
	
	#public
	def euler_cromer(self):
		while(self.t[-1]<10):
			self.v.append(self.v[-1]-self.x[-1]*self.km*self.dt)
			self.x.append(self.x[-1] + self.v[-1]*self.dt +np.sign(self.x[-1])*(self.fat/self.km))
			self.e.append(((0.5*(self.v[-1]**2 + self.x[-1]**2))))
			self.t.append(self.t[-1]+self.dt)

	def verlet(self):
		while(self.t[-1]<10):
			v_0 = self.v[-1]-self.x[-1]*self.km*self.dt/2
			self.x.append(self.x[-1] +v_0*self.dt -np.sign(self.x[-1])*(self.fat/self.km))
			self.v.append(v_0-self.x[-1]*self.km*self.dt/2)
			self.e.append(((0.5*(self.v[-1]**2 + self.x[-1]**2))))
			self.t.append(self.t[-1]+self.dt)
		
	def resetT(self):
		self.t = [0]

def grafics(_tlist,_dlist,_fileName,_title,_xLabel,_yLabel,_cor,_modeAx = -1):
	print 'processando...'
	plt.figure(figsize=(4,4),dpi=96)
	
	ax = plt.gca()
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.spines['bottom'].set_position(('data',0))
	ax.yaxis.set_ticks_position('left')
	ax.spines['left'].set_position(('data',0))
	ax.autoscale()
	
	plt.rc('text',usetex = True)
	plt.rc('font',**{'sans-serif':'Arial','family':'sans-serif'})
	plt.xlabel(_xLabel)
	plt.ylabel(_yLabel)
	
	if(_modeAx == 0):
		plt.xticks(np.linspace(0,3*np.pi,7,endpoint = True),
		[r' ',r'$\frac{\pi}{2}$',r'$\pi$',r'$\frac{3\pi}{2}$',r'$2\pi$',r'$\frac{5\pi}{2}$',r'$3\pi$'])
	elif(_modeAx == 1):
		plt.yticks(np.linspace(-3*np.pi,3*np.pi,13,endpoint = True),
			[r'$-3\pi$',r'$\frac{-5\pi}{2}$',r'$-2\pi$',r'$\frac{-3\pi}{2}$',r'$-\pi$',r'$\frac{-\pi}{2}$',r' ',r'$\frac{\pi}{2}$',r'$\pi$',r'$\frac{3\pi}{2}$',r'$2\pi$',r'$\frac{5\pi}{2}$',r'$3\pi$'])
		plt.xticks(np.linspace(0,3*np.pi,7,endpoint = True),
		[r' ',r'$\frac{\pi}{2}$',r'$\pi$',r'$\frac{3\pi}{2}$',r'$2\pi$',r'$\frac{5\pi}{2}$',r'$3\pi$'])
	
	plt.title(_title,fontsize = 16)
	plt.plot(_tlist,_dlist,_cor,linewidth = 2)
	plt.savefig(_fileName,dpi=96)
		
def main():
	#variables
	
	grpVlt0 = Oscilador()
	grpVlt1 = Oscilador()
	
	#program	
	
	grpVlt0.setKM(5)
	grpVlt0.setX(3)
	grpVlt0.setFat(0.003*9.8)
	grpVlt0.verlet()
	
	grpVlt1.setKM(5)
	grpVlt1.setX(3)
	grpVlt1.setFat(0.003*1.625)
	grpVlt1.verlet()
	
	grafics(grpVlt0.t,grpVlt0.x,'image1_1',r'Oscilador real-posi\c{c}\~{a}o',r'\textit{tempo}(s)',r'\textit{posi\c{c}\~{a}o} (m)','k-',0)
	
	grafics(grpVlt0.t,grpVlt0.v,'image1_2',r'Oscilador real-velocidade',r'\textit{tempo}(s)',r'\textit{velocidade}(m/s)','g-',0)
	
	grafics(grpVlt0.x,grpVlt0.v,'image1_3',r'Espa\c{c}o de fases do Oscilador',r'\raggedright{\textit{posi\c{c}\~{a}o} (m)}',r'\raggedleft{\textit{velocidade}(m/s)}','b-',1)
	
	grafics(grpVlt1.t,grpVlt1.x,'image2_1',r'Oscilador real-posi\c{c}\~{a}o',r'\textit{tempo}(s)',r'\textit{posi\c{c}\~{a}o} (m)','k-',0)
	
	grafics(grpVlt1.t,grpVlt1.v,'image2_2',r'Oscilador real-velocidade',r'\textit{tempo}(s)',r'\textit{velocidade}(m/s)','g-',0)
	
	grafics(grpVlt1.x,grpVlt1.v,'image2_3',r'Espa\c{c}o de fases do Oscilador',r'\raggedright{\textit{posi\c{c}\~{a}o} (m)}',r'\raggedleft{\textit{velocidade}(m/s)}','b-',1)
	
	
main()

print 'concluido'
