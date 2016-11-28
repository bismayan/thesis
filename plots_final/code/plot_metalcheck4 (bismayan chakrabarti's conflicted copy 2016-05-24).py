#! /usr/bin/env python

from scipy import *
from pylab import *
import glob

#prefix=["a-a-a-_ht","a-a-a-_lt",'a0a0a0_ht','a0a0a0_lt']
prefix=['a0a0a0_ht']
col_list=['ro-','bo-','yo-','go-']
npoints=4	# number of points on each side of omega=0 to avge over
shift0=[0,-3,0,10]
max_range=[-6,-3]
min_dos=0.1	# min dos to calculate bandgap
print "min_dos=",min_dos
min_dos_range=[-1.0,1.0]	# range in which to look for bandgap
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
		mark_dos=zeros(2,dtype=int)
		mark_gap=zeros(2,dtype=int)
		mark_dos[0]=(min_dos_range[0]-om[0])/(om[1]-om[0])
		mark_dos[1]=(min_dos_range[1]-om[0])/(om[1]-om[0])
		gap_count=0
		print "beta=",beta
	#	print "minimum Dos=",amin(imp_dos[(mark_dos[0]-shift):(mark_dos[1]-shift)])
		flag=0
		for k in range(mark_dos[0],mark_dos[1]):
			if((tot_dos[k-shift]-min_dos)*(tot_dos[k-shift+1]-min_dos)<0):
				mark_gap[flag%2]=k	
				flag=flag+1
				if(flag%2==0):
					print "gap found of size ",(mark_gap[1]-mark_gap[0])*(om[1]-om[0])		
					gap_count+=1
		print "Number of gaps found=",gap_count
		print "#################"
	out=sort(out,order='temp')
	xlabel("T (in K) -->")
	ylabel("Dos-->")
	if j<2:
		plot(out['temp'],out['tdos']/2.0,col_list[j],label=pref)
	else:	
		plot(out['temp'],out['tdos'],col_list[j],label=pref)

legend(loc=2)
grid()
#savefig("../output/metalcheck.eps")
#show()

