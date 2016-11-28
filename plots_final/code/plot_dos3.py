#import scipy as sp
import pylab as plt
import matplotlib.lines as mlines

## Creating lists of cdos and gc1 files 
paths_gc1=["../files/Dos_files/a-a-a-_ht_b100.gc1","../files/Dos_files/a-a-a-_ht_b10.gc1","../files/Dos_files/a-a-a-_lt_b100.gc1","../files/Dos_files/a-a-a-_lt_b10.gc1","../files/Dos_files/a0a0a0_ht_b100.gc1_broad","../files/Dos_files/a0a0a0_ht_b10.gc1_broad","../files/Dos_files/a0a0a0_lt_b100.gc1_broad","../files/Dos_files/a0a0a0_lt_b10.gc1_broad"]

paths_cdos=["../files/Dos_files/a-a-a-_ht_b100.cdos","../files/Dos_files/a-a-a-_ht_b10.cdos","../files/Dos_files/a-a-a-_lt_b100.cdos","../files/Dos_files/a-a-a-_lt_b10.cdos","../files/Dos_files/a0a0a0_ht_b100.cdos_broad","../files/Dos_files/a0a0a0_ht_b10.cdos_broad","../files/Dos_files/a0a0a0_lt_b100.cdos_broad","../files/Dos_files/a0a0a0_lt_b10.cdos_broad"]

labels=["High Temp w/ Rotations", "Low Temp w/ Rotations", "High Temp w/o Rotations", "Low Temp w/o Rotations"]

Temps=["T=116K", "T=1160K"]

lines = [mlines.Line2D([],[],color='green',linewidth=2.0),mlines.Line2D([],[],color='red',linewidth=2.0),mlines.Line2D([],[],color='blue',linewidth=2.0)] 
leg_label=["Total","$t_{2g}$","$e_{g}$"]
nrows=2
ncols=4
xlim=[-3.95,3.95]
ylim=[0,5.99]

plt.rcParams['xtick.labelsize']=20
plt.rcParams['ytick.labelsize']=20
plt.rcParams['axes.labelsize']=18
plt.rcParams['axes.grid']=False
plt.rcParams["figure.subplot.wspace"]=0.08
plt.rcParams["figure.subplot.hspace"]=0.08
plt.rcParams["savefig.bbox"]="tight"


if __name__=="__main__":
	count=0
	fig=plt.figure(figsize=(18,9.2))
	for i in range(ncols):
		for j in range(nrows):
			ax=plt.subplot(nrows,ncols,(ncols*j)+i+1)
			dat_cdos=plt.loadtxt(paths_cdos[count]).transpose()
			dat_gc1=plt.loadtxt(paths_gc1[count]).transpose()
			plt.plot(dat_cdos[0],dat_cdos[1]/(1+(count<4)),"g-",linewidth=1.3)
			if i<2:
				plt.plot(dat_gc1[0],(dat_gc1[2]*2+dat_gc1[4])*(-1/plt.pi),"r-",linewidth=1.3)
				plt.plot(dat_gc1[0],(dat_gc1[6]*2)*(-1/plt.pi),"b-",linewidth=1.3)
			else:
				
				plt.plot(dat_gc1[0],(dat_gc1[4]*3)*(-1/plt.pi),"r-",linewidth=1.3)
				plt.plot(dat_gc1[0],(dat_gc1[2]*2)*(-1/plt.pi),"b-",linewidth=1.3)
			plt.xlim(xlim)
			plt.ylim(ylim)
			if i is not 0:	
				ax.get_yaxis().set_ticklabels([])
			if j==0:
				ax.get_xaxis().set_ticklabels([])
				plt.title(labels[i],fontsize=20)
			ax.axvline(color='k',linestyle="--",linewidth=1.0)
			ax.text(-1.5,4.5,Temps[j],fontsize=20)
			count=count+1
	fig.text(0.5,0.04,'$\omega$(eV)',fontsize=20)
	fig.text(0.08,0.55,'DOS(1/eV)',fontsize=20,rotation=90)
	plt.figlegend(lines,leg_label,loc=(0.065,0.005),ncol=3,fontsize=20,fancybox=True)
	plt.savefig("../output/New_dos.png")	
	#plt.show()
