#! /usr/bin/env python

from scipy import *
from pylab import *
import glob

prefix=["a-a-a-_ht","a-a-a-_lt",'a0a0a0_ht','a0a0a0_lt']
prefix2=["$HTa^-$","$LTa^-$",'$HTa^0$','$LTa^0$']
col_list=['ro-','bo-','yo-','go-']
npoints=5	# number of points on each side of omega=0 to avge over
shift0=[0,0,-0,0]
max_range=[-10,10]
for j,pref in enumerate(prefix):
	files=glob.glob("../files/Dos_files/"+pref+"*.cdos")
	out=zeros(len(files), dtype=[('temp',float),('tdos',float),('idos',float)])
	for i,fil in enumerate(files):
		flag=zeros(2,dtype=int)
		beta=float(fil.split('b')[-1].split('.')[0])
		temp=11600/beta
		dat=loadtxt(fil).transpose()
		om=dat[0]
		tot_dos=dat[1]
		imp_dos=dat[2]
		for mark in range(2):
			flag[mark]=int((max_range[mark]-om[0])*len(om)/(om[-1]-om[0]))
		max_dos=argmax(tot_dos[flag[0]:flag[1]])
		if i==0:
			dos_flag=max_dos
		shift=-1.0*(max_dos-dos_flag)-shift0[j]

		tot_val=sum(tot_dos[len(om)/2.0-npoints-shift:len(om)/2.0+npoints-shift])/(2*npoints)
		om_val=sum(om[len(om)/2.0-npoints-shift:len(om)/2.0+npoints-shift])/(2*npoints)
		imp_val=sum(imp_dos[len(om)/2.0-npoints-shift:len(om)/2.0+npoints-shift])/(2*npoints)
		out[i]['temp']=temp
		out[i]['tdos']=tot_val
		out[i]['idos']=imp_val
	out=sort(out,order='temp')
	xlabel("T (K) -->",fontsize=20)
	ylabel("DOS at $\omega$=0-->",fontsize=20)
	if j<2:
		plot(out['temp'],out['tdos']/2.0,col_list[j],label=prefix2[j])
	else:	
		plot(out['temp'],out['tdos'],col_list[j],label=prefix2[j])

legend(loc=2)
grid()
#savefig("../output/metalcheck.png")
show()

