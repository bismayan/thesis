from pylab import *
import glob
import matplotlib.lines as mlines

lines = [mlines.Line2D([],[],color='red',marker='o',linewidth=2.0),mlines.Line2D([],[],color='blue',marker='o',linewidth=2.0),mlines.Line2D([],[],color='black',marker='o',linewidth=2.0),mlines.Line2D([],[],color='green',marker='o',linewidth=2.0)]
leg_label=["$HTa^-$","$LTa^-$","$HTa^0$","$LTa^0$"]

rcParams['xtick.labelsize']=14                                                                                    
rcParams['lines.linewidth']=2.4                                                                                   
rcParams['ytick.labelsize']=14                                                                                    
rcParams['axes.labelsize']=18                                                                                     
rcParams['axes.grid']=True                                                                                        
#rcParams["figure.subplot.right"]=1.0                                                                              
#rcParams["figure.subplot.top"]=0.9                                                                                
rcParams["figure.subplot.bottom"]=0.15                                                                            
rcParams["figure.subplot.wspace"]=0.25                                                                   
#rcParams["savefig.bbox"]="tight"        


path1='../files/Sz_files/Sz.dat'
fig=figure(figsize=(10,6.5))
subplot(121)
dat1=loadtxt(path1).transpose()
T=11600.0/dat1[0][1:]
a1=dat1[1][1:]
a2=dat1[2][1:]
a3=dat1[3][1:]
a4=dat1[4][1:]
xlim([0,1180])
ylabel("|$S_{z}$|",fontsize=18)
plot(T,a1,'ro-',label="$HTa^-$")
plot(T,a2,'bo-',label="$LTa^-$")
plot(T,a3,'ko-',label="$HTa^0$")
plot(T,a4,'go-',label="$LTa^0$")
yticks(linspace(0.3,0.7,5))
subplot(122)
prefix=["a-a-a-_ht","a-a-a-_lt",'a0a0a0_ht','a0a0a0_lt']
prefix2=["$HTa^-$","$LTa^-$",'$HTa^0$','$LTa^0$']
col_list=['ro-','bo-','ko-','go-']
npoints=5	# number of points on each side of omega=0 to avge over
shift0=[0,-1,0,0]
max_range=[-6,-3]
xlim([0,1180])
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
	ylabel("DOS at $\omega$=0",fontsize=18)
	if j<2:
		plot(out['temp'],out['tdos']/2.0,col_list[j],label=prefix2[j])
	else:	
		plot(out['temp'],out['tdos'],col_list[j],label=prefix2[j])
fig=gcf()
fig.text(0.47,0.09,"T(K)",fontsize=18)
fig=gcf()
fig.legend(lines,leg_label,loc=(0.18, 0.01),fontsize=18,ncol=4,fancybox=True)
savefig("fig2.png")
show()
