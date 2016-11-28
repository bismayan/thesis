#! /usr/bin/env python
#tries to produce different histograms for LaCoO3
#right now assumes size 1
# modified from hist_create to create inverted histograms with more complicated color coding for paper
#slightly cheats in order to sum over S_z direction by taking only +ve Sz and multiplying probablility by 2
#produces final plots with inverted histograms
# derived from hist_create 
from scipy import *
from pylab import *

Path11="/work/bismayan/test/vasp_calculations/LaCoO3_final_2/a0a0a0_from_hightemp/b100_J0.7/diag_run/154851bismayan/a0a0a0/imp.0/"
Path12="/work/bismayan/test/vasp_calculations/LaCoO3_final_2/high_temp_struct/b100_J0.7/128784bismayan/LaCoO3_1248K/imp.0/"
Path21="/work/bismayan/test/vasp_calculations/LaCoO3_final_2/a0a0a0_from_lowtemp/b100_J0.7/diag_run/154845bismayan/a0a0a0/imp.0/"
Path22="/work/bismayan/test/vasp_calculations/LaCoO3_final_2/low_temp_struct/b100_J0.7/128640bismayan/LaCoO3_4K/imp.0/"
Path31="/work/bismayan/test/vasp_calculations/LaCoO3_final_2/a0a0a0_from_hightemp/b10_J0.7/diag_run/154852bismayan/a0a0a0/imp.0/"
Path32="/work/bismayan/test/vasp_calculations/LaCoO3_final_2/high_temp_struct/b10_J0.7/128639bismayan/LaCoO3_1248K/imp.0/"
Path41="/work/bismayan/test/vasp_calculations/LaCoO3_final_2/a0a0a0_from_lowtemp/b10_J0.7/diag_run/154812bismayan/a0a0a0/imp.0/"
Path42="/work/bismayan/test/vasp_calculations/LaCoO3_final_2/low_temp_struct/b10_J0.7/128785bismayan/LaCoO3_4K/imp.0/"
cl=['r','g','b','y','m','c','w','k']
sp_cl=['r','y','g','c','b','m']
Cols=['N','Sz','Prob']
sort_col=[0,1]  # always have 1st one to be 0
N_min=6
N_max=8
ylim_max=-1
Order=[Cols[sort_col[0]],Cols[sort_col[1]]]
wid=1.0
crit_Prob=0.001
if __name__=="__main__":	
	file11=open(Path11+"actqmc.cix","r")
	dat11=loadtxt(Path11+"Probability.dat").transpose()
	Probs11=dat11[2]
	file12=open(Path12+"actqmc.cix","r")
	dat12=loadtxt(Path12+"Probability.dat").transpose()
	Probs12=dat12[2]
	file21=open(Path21+"actqmc.cix","r")
	dat21=loadtxt(Path21+"Probability.dat").transpose()
	Probs21=dat21[2]
	file22=open(Path22+"actqmc.cix","r")
	dat22=loadtxt(Path22+"Probability.dat").transpose()
	Probs22=dat22[2]
	file31=open(Path31+"actqmc.cix","r")
	dat31=loadtxt(Path31+"Probability.dat").transpose()
	Probs31=dat31[2]
	file32=open(Path32+"actqmc.cix","r")
	dat32=loadtxt(Path32+"Probability.dat").transpose()
	Probs32=dat32[2]
	file41=open(Path41+"actqmc.cix","r")
	dat41=loadtxt(Path41+"Probability.dat").transpose()
	Probs41=dat41[2]
	file42=open(Path42+"actqmc.cix","r")
	dat42=loadtxt(Path42+"Probability.dat").transpose()
	Probs42=dat42[2]
	length=int(dat11[0][-1])
	line11=file11.readline()
	hist_data=zeros((length),dtype=[('N',float),('Sz',float),('Prob1',float),('Prob2',float),('Prob3',float),('Prob4',float),('Prob5',float),('Prob6',float),('Prob7',float),('Prob8',float)])
	while (line11.split()[-1]!='size'):
		line11=file11.readline()
	dat_count=0
	for i in range(length):
		line11=file11.readline()
		split_line11=line11.split()
		if (float(split_line11[1]) in range(N_min,N_max+1)):
			if( Probs11[i]>=crit_Prob or Probs12[i]>= crit_Prob or Probs21[i]>=crit_Prob or Probs22[i]>= crit_Prob or Probs31[i]>=crit_Prob or Probs32[i]>= crit_Prob or Probs41[i]>=crit_Prob or Probs42[i]>= crit_Prob):
				if(float(split_line11[3])>=0):
					hist_data[dat_count][0]=float(split_line11[1])
					hist_data[dat_count][1]=float(split_line11[3])
					if(float(split_line11[3])>0):
						hist_data[dat_count][2]=2*Probs11[i]
						hist_data[dat_count][3]=2*Probs12[i]
						hist_data[dat_count][4]=2*Probs21[i]
						hist_data[dat_count][5]=2*Probs22[i]
						hist_data[dat_count][6]=2*Probs31[i]
						hist_data[dat_count][7]=2*Probs32[i]
						hist_data[dat_count][8]=2*Probs41[i]
						hist_data[dat_count][9]=2*Probs42[i]
					else:
						hist_data[dat_count][2]=Probs11[i]
						hist_data[dat_count][3]=Probs12[i]
						hist_data[dat_count][4]=Probs21[i]
						hist_data[dat_count][5]=Probs22[i]
						hist_data[dat_count][6]=Probs31[i]
						hist_data[dat_count][7]=Probs32[i]
						hist_data[dat_count][8]=Probs41[i]
						hist_data[dat_count][9]=Probs42[i]
					dat_count=dat_count+1
	hist_data1=hist_data[0:dat_count]
	a=sort(hist_data1,order=Order)
	col_count=0
	c_old=0
	tickname=[]
	pos_old=0
	tickpos=[]
	spin_tickpos=[0]
	spin_tickcolor=[]
	for i in range(dat_count):
		
		c=(a[i][0]-a[0][0])
		if(i>0 and a[i][1]!=a[i-1][1]):
			spin_tickpos.append(i)
			spin_color=abs(round(a[i-1][1]/0.5))
			spin_tickcolor.append(spin_color)
		#	spin_tickpos.append(dat_count+wid+i)
		#	spin_tickcolor.append(spin_color)
		if i==0:
			c_old=c
		if(c-c_old)>0.001:
			tickname.append(str(a[i-1][0]))
			tickpos.append((i+pos_old)/2.0)
			tickname.append(str(a[i-1][0]))
			tickpos.append((2*(dat_count+wid)+i+pos_old)/2.0)
			pos_old=i
			c_old=c
			col_count=col_count+1
			if col_count>7:
				col_count=0			
		bar(i,-1*a[i][2],wid,color=cl[col_count],bottom=1.2,zorder=2)
		bar(i,a[i][3],wid,color=cl[col_count],bottom=1.2,zorder=2)
		bar(dat_count+i,-1*a[i][6],wid,color=cl[col_count],bottom=1.2,zorder=2)
		bar(dat_count+i,a[i][7],wid,color=cl[col_count],bottom=1.2,zorder=2)
		bar(i,-1*a[i][4],wid,color=cl[col_count],bottom=0.4,zorder=2)
		bar(i,a[i][5],wid,color=cl[col_count],bottom=0.4,zorder=2)
		bar(dat_count+i,-1*a[i][8],wid,color=cl[col_count],bottom=0.4,zorder=2)
		bar(dat_count+i,a[i][9],wid,color=cl[col_count],bottom=0.4,zorder=2)
	spin_color=abs(round(a[dat_count-1][1]/0.5))
	if (spin_color != spin_tickcolor[-1]):
		spin_tickpos.append(dat_count)
		spin_tickcolor.append(spin_color)
		#spin_tickpos.append(2*dat_count)
		#spin_tickcolor.append(spin_color)
	
	tickpos.append((dat_count+1+pos_old)/2.0)
	tickname.append(str(a[dat_count-1][0]))
	tickpos.append((3*dat_count+1+pos_old)/2.0)
	tickname.append(str(a[dat_count-1][0]))
	xticks(array(tickpos),tickname,fontsize=32)
	xlabel(Order[0]+"-->",fontsize=32)
	ylabel("Probability-->",fontsize=32)
	grid()
	xlim([0,2*(dat_count)])
	ytickpos=[]
	ytickname=[]
	for i in linspace(0.0,1.6,17):
		ytickpos.append(i)
	#	ytickname.append(str(abs(round(i-0.4,2))))
	#	ytickpos.append(i)
	#	ytickname.append(str(abs(round(i-0.4,2))))
	ytickname=['','0.3','0.2','0.1','0.0','0.1','0.2','0.3','','0.3','0.2','0.1','0.0','0.1','0.2','0.3','']
	yticks(array(ytickpos),ytickname,fontsize=24)
	ax=gca()
	spin_tickcolor=map(int,spin_tickcolor)
	print dat_count
	print spin_tickpos
	for i in range(len(spin_tickcolor)):
		#text((spin_tickpos[i]+spin_tickpos[i+1]-4)/(4.0*spin_tickpos[-1]),0.95,"|Sz|="+str(spin_tickcolor[i]/2.0),transform=ax.transAxes,fontsize=26)
		axvspan(spin_tickpos[i],spin_tickpos[i+1],color=sp_cl[spin_tickcolor[i]],alpha=0.09,zorder=1)
		#text((spin_tickpos[i]+spin_tickpos[i+1]+2.0*(spin_tickpos[-1])-4)/(4.0*spin_tickpos[-1]),0.95,"|Sz|="+str(spin_tickcolor[i]/2.0),transform=ax.transAxes,fontsize=24)
		axvspan(spin_tickpos[i]+spin_tickpos[-1],spin_tickpos[i+1]+spin_tickpos[-1],color=sp_cl[spin_tickcolor[i]],alpha=0.09,zorder=1)
	text(0.01,0.1,"Low  T struct \nunrotated", transform=ax.transAxes, fontsize=32,bbox=dict(facecolor='wheat', edgecolor='black',boxstyle='round,pad=0.7'))
	text(0.01,0.35,"Low  T struct", transform=ax.transAxes, fontsize=32,bbox=dict(facecolor='wheat', edgecolor='black',boxstyle='round,pad=0.7'))
	text(0.01,0.6,"High T struct \nunrotated", transform=ax.transAxes, fontsize=32,bbox=dict(facecolor='wheat', edgecolor='black',boxstyle='round,pad=0.7'))
	text(0.01,0.85,"High T struct", transform=ax.transAxes, fontsize=32,bbox=dict(facecolor='wheat', edgecolor='black',boxstyle='round,pad=0.7'))
	for i in range(len(spin_tickcolor)-1):
		if(spin_tickcolor[i]%2+spin_tickcolor[i+1]%2)==1.0:
			axvline(spin_tickpos[i+1],linewidth=1,color='k',linestyle='--')
			axvline(spin_tickpos[i+1]+spin_tickpos[-1],linewidth=1,color='k',linestyle='--')
	axhline(0.8,lw=4.5,color='k')
	axhline(0.4,lw=3.0,color='k')
	axhline(1.2,lw=3.0,color='k')
	axvline(dat_count,lw=4.5,color='k')
	text(0.23,0.05,"T=116K", transform=ax.transAxes, fontsize=32,bbox=dict(facecolor='wheat', edgecolor='black',boxstyle='round,pad=0.7'))
	text(0.73,0.05,"T=1160K", transform=ax.transAxes, fontsize=32,bbox=dict(facecolor='wheat', edgecolor='black',boxstyle='round,pad=0.7'))
	fig=gcf()
	fig.set_size_inches(40,20)
	savefig("../output/hist_final.png",dpi=300)
	show()

	
	
	
	
	
