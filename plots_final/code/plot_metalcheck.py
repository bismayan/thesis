#! /usr/bin/env python

from scipy import *
from pylab import *
import glob
prefix="a-a-a-_ht"
max_dos=0
shift0=0
col_list=['r-','b-','y-','g-','m-','c-','k-','r--','b--','y--','g--','c--','k--','m--']
files=glob.glob("../files/Dos_files/"+prefix+"*.cdos")
max_range=[-6,-3]
for i,fil in enumerate(files):
	flag=zeros(2,dtype=int)
	beta=float(fil.split('b')[-1].split('.')[0])
	temp=around(11600/beta,2)
	dat=loadtxt(fil).transpose()
	om=dat[0]
	tot_dos=dat[1]
	imp_dos=dat[2]
	for mark in range(2):
		flag[mark]=int((max_range[mark]-om[0])*len(om)/(om[-1]-om[0]))
	max_dos=argmax(tot_dos[flag[0]:flag[1]])
	if i==0:
		dos_flag=max_dos
	shift=-1.0*(max_dos-dos_flag)-shift0

	om_val=om[len(om)/2.0-shift]
	plot(om-om_val,tot_dos,col_list[i],label="T="+str(temp)+"K")
	xlim([-2,2])
	ylim([0,25])
	print beta,shift,om_val
grid()
legend()
show()

