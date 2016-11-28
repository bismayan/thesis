from scipy import *
from pylab import *
path1='../files/Sz_files/Sz=0.dat'
path2='../files/Sz_files/Sz=0.5.dat'
path3='../files/Sz_files/Sz=1.0.dat'
path4='../files/Sz_files/Sz=1.5.dat'
path5='../files/Sz_files/Sz=2.0.dat'

dat1=loadtxt(path1).transpose()
dat2=loadtxt(path2).transpose()
dat3=loadtxt(path3).transpose()
dat4=loadtxt(path4).transpose()
dat5=loadtxt(path5).transpose()
T=11600.0/dat1[0][1:]
x=zeros(len(T),dtype=float)
######### high temp ##########
for i in range(1,5):
	d0=dat1[i][1:]
	d1=d0+dat2[i][1:]
	d2=d1+dat3[i][1:]
	d3=d2+dat4[i][1:]
	d4=d3+dat5[i][1:]
	ax=gca()
	print T.size,d0.size
	ax.fill_between(T,0,d0,color='r',alpha=0.25)
	#text(0.8,(d0[0]/2.0),"|Sz=0.0|", transform=ax.transAxes, fontsize=10)
	ax.fill_between(T,d0,d1,color='b',alpha=0.25)
	ax.fill_between(T,d1,d2,color='g',alpha=0.25)
	ax.fill_between(T,d2,d3,color='y',alpha=0.25)
	ax.fill_between(T,d3,d4,color='m',alpha=0.25)
	xlim([T[-1],T[0]])
	ylim([0,1])
	xlabel("T(K)-->",fontsize=32)
	ylabel("Probability-->",fontsize=32)	
	tick_params(axis='both', which='major', labelsize=20)
	fig=gcf()
	fig.set_size_inches(20,10)
	savefig("../output/Sz_area"+str(i)+".png",dpi=100)
	show()

