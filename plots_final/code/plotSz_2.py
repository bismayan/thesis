import pylab as plt
import matplotlib.lines as mlines

paths=['../files/Sz_files/Sz=0.dat','../files/Sz_files/Sz=0.5.dat','../files/Sz_files/Sz=1.0.dat','../files/Sz_files/Sz=1.5.dat','../files/Sz_files/Sz=2.0.dat']

Temps=["High Temp","Low Temp"]
Rots=["w/ Rotations","w/o Rotations"]

lines = [mlines.Line2D([],[],color='red',marker='o',linewidth=2.0),mlines.Line2D([],[],color='yellow',marker='o',linewidth=2.0),mlines.Line2D([],[],color='blue',marker='o',linewidth=2.0),mlines.Line2D([],[],color='black',marker='o',linewidth=2.0),mlines.Line2D([],[],color='green',marker='o',linewidth=2.0)] 
leg_label=["|Sz]=0.0","|Sz]=0.5","|Sz]=1.0","|Sz]=1.5","|Sz]=2.0",]

plt.rcParams['xtick.labelsize']=24
plt.rcParams['lines.linewidth']=2.5
plt.rcParams['ytick.labelsize']=24
plt.rcParams['axes.labelsize']=20
plt.rcParams['axes.grid']=True
plt.rcParams["figure.subplot.wspace"]=0.06
plt.rcParams["figure.subplot.left"]=0.09
plt.rcParams["figure.subplot.right"]=1.0
plt.rcParams["figure.subplot.top"]=0.9
plt.rcParams["figure.subplot.bottom"]=0.13
plt.rcParams["figure.subplot.hspace"]=0.06
plt.rcParams["savefig.bbox"]="tight"
xlim=[0,1180]
nrows=2
ncols=2

if __name__=="__main__":
	dat1=plt.loadtxt(paths[0]).transpose()
	dat2=plt.loadtxt(paths[1]).transpose()
	dat3=plt.loadtxt(paths[2]).transpose()
	dat4=plt.loadtxt(paths[3]).transpose()
	dat5=plt.loadtxt(paths[4]).transpose()
	T=11600.0/dat1[0][1:]
	fig=plt.figure(figsize=(12,16))
	count=0
	for i in range(nrows):
		for j in range(ncols):
			ax=plt.subplot(nrows,ncols,i*nrows+j+1)
			plt.plot(T,dat1[i*nrows+j+1][1:],'ro-')
			plt.plot(T,dat2[i*nrows+j+1][1:],'yo-')
			plt.plot(T,dat3[i*nrows+j+1][1:],'bo-')
			plt.plot(T,dat4[i*nrows+j+1][1:],'ko-')
			plt.plot(T,dat5[i*nrows+j+1][1:],'go-')
			plt.xlim(xlim)
			plt.ylim([0,0.495])
			if  i==0:	
				plt.title(Temps[j],fontsize=32)
				ax.get_xaxis().set_ticklabels([])
			if j is not 0:
				ax.get_yaxis().set_ticklabels([])
			ax.text(200,0.25,Rots[i],fontsize=32)
	
	fig.text(0.5,0.08,"T(K)",fontsize=28)
	fig.text(0.00,0.6,"Probability",fontsize=26,rotation=90)
	fig.legend(lines,leg_label,bbox_to_anchor=(0.02, 0.02, 1.0,0.06),fontsize=24,bbox_transform=plt.gcf().transFigure,ncol=5,fancybox=True,labelspacing=0.2,columnspacing=0.8,handletextpad=0.4)
	plt.savefig("../output/New_Sz.png")	
#	plt.show()
