from scipy import *
#import matplotlib
#matplotlib.use('Agg')
from pylab import *
path1="../files/Dos_files/a-a-a-_ht_b100.gc1"
path2="../files/Dos_files/a-a-a-_ht_b10.gc1"
path3="../files/Dos_files/a-a-a-_lt_b100.gc1"
path4="../files/Dos_files/a-a-a-_lt_b10.gc1"
path5="../files/Dos_files/a0a0a0_ht_b100.gc1"
path6="../files/Dos_files/a0a0a0_ht_b10.gc1"
path7="../files/Dos_files/a0a0a0_lt_b100.gc1"
path8="../files/Dos_files/a0a0a0_lt_b10.gc1"
path1a="../files/Dos_files/a-a-a-_ht_b100.cdos"
path2a="../files/Dos_files/a-a-a-_ht_b10.cdos"
path3a="../files/Dos_files/a-a-a-_lt_b100.cdos"
path4a="../files/Dos_files/a-a-a-_lt_b10.cdos"
path5a="../files/Dos_files/a0a0a0_ht_b100.cdos"
path6a="../files/Dos_files/a0a0a0_ht_b10.cdos"
path7a="../files/Dos_files/a0a0a0_lt_b100.cdos"
path8a="../files/Dos_files/a0a0a0_lt_b10.cdos"
dat1=loadtxt(path1).transpose()
dat2=loadtxt(path2).transpose()
dat3=loadtxt(path3).transpose()
dat4=loadtxt(path4).transpose()
dat5=loadtxt(path5).transpose()
dat6=loadtxt(path6).transpose()
dat7=loadtxt(path7).transpose()
dat8=loadtxt(path8).transpose()
dat1a=loadtxt(path1a).transpose()
dat2a=loadtxt(path2a).transpose()
dat3a=loadtxt(path3a).transpose()
dat4a=loadtxt(path4a).transpose()
dat5a=loadtxt(path5a).transpose()
dat6a=loadtxt(path6a).transpose()
dat7a=loadtxt(path7a).transpose()
dat8a=loadtxt(path8a).transpose()
################################
om=dat1[0]
t2g_1=(dat1[2]+dat1[4]+dat1[2])*(-1/pi)
eg_1=(dat1[6]+dat1[6])*(-1/pi)
xlim([-4,4])
ylim([0,8])
grid()
plot(om,t2g_1, 'r-', label="$t_{2g}$")
plot(om,eg_1, 'b-', label="$e_{g}$")
plot(om,dat1a[1]/2.0,'g--',label="Total")

ax=gca()
for label in ax.get_xticklabels()+ax.get_yticklabels():
	label.set_fontsize(16)
legend(loc=0)
xlabel('$\omega$(eV)-->',fontsize=25)
savefig("../output/dos_a-a-a-_ht_b100.png")
show()
################################
t2g_2=(dat2[2]+dat2[4]+dat2[2])*(-1/pi)
eg_2=(dat2[6]+dat2[6])*(-1/pi)
xlim([-4,4])
ylim([0,8])
grid()
plot(om,t2g_2, 'r-', label="$t_{2g}$")
plot(om,eg_2, 'b-', label="$e_{g}$")
plot(om,dat2a[1]/2.0,'g--',label="Total")
legend(loc=0)
xlabel('$\omega$(eV)-->',fontsize=25)
savefig("../output/dos_a-a-a-_ht_b10.png")
show()
################################
t2g_3=(dat3[2]+dat3[4]+dat3[2])*(-1/pi)
eg_3=(dat3[6]+dat3[6])*(-1/pi)
xlim([-4,4])
ylim([0,8])
grid()
plot(om,t2g_3, 'r-', label="$t_{2g}$")
plot(om,eg_3, 'b-', label="$e_{g}$")
plot(om,dat3a[1]/2.0,'g--',label="Total")
ax=gca()
for label in ax.get_xticklabels()+ax.get_yticklabels():
	label.set_fontsize(16)
legend(loc=0)
xlabel('$\omega$(eV)-->',fontsize=25)
savefig("../output/dos_a-a-a-_lt_b100.png")
show()
################################
t2g_4=(dat4[2]+dat4[4]+dat4[2])*(-1/pi)
eg_4=(dat4[6]+dat4[6])*(-1/pi)
xlim([-4,4])
ylim([0,8])
grid()
plot(om,t2g_4, 'r-', label="$t_{2g}$")
plot(om,eg_4, 'b-', label="$e_{g}$")
plot(om,dat4a[1]/2.0,'g--',label="Total")
ax=gca()
for label in ax.get_xticklabels()+ax.get_yticklabels():
	label.set_fontsize(16)
legend(loc=0)
xlabel('$\omega$(eV)-->',fontsize=25)
savefig("../output/dos_a-a-a-_lt_b10.png")
show()
################################
t2g_5=(dat5[4]+dat5[4]+dat5[4])*(-1/pi)
eg_5=(dat5[2]+dat5[2])*(-1/pi)
xlim([-4,4])
ylim([0,8])
grid()
plot(om,t2g_5, 'r-', label="$t_{2g}$")
plot(om,eg_5, 'b-', label="$e_{g}$")
plot(om,dat5a[1],'g--',label="Total")
xlabel('$\omega$(eV)-->',fontsize=25)
ax=gca()
for label in ax.get_xticklabels()+ax.get_yticklabels():
	label.set_fontsize(16)
legend(loc=0)
savefig("../output/dos_a0a0a0_ht_b100.png")
show()
################################
t2g_6=(dat6[4]+dat6[4]+dat6[4])*(-1/pi)
eg_6=(dat6[2]+dat6[2])*(-1/pi)
xlim([-4,4])
ylim([0,8])
grid()
plot(om,t2g_6, 'r-', label="$t_{2g}$")
plot(om,eg_6, 'b-', label="$e_{g}$")
plot(om,dat6a[1],'g--',label="Total")
ax=gca()
for label in ax.get_xticklabels()+ax.get_yticklabels():
	label.set_fontsize(16)
legend(loc=0)
xlabel('$\omega$(eV)-->',fontsize=25)
savefig("../output/dos_a0a0a0_ht_b10.png")
show()
################################
t2g_7=(dat7[4]+dat7[4]+dat7[4])*(-1/pi)
eg_7=(dat7[2]+dat7[2])*(-1/pi)
xlim([-4,4])
ylim([0,8])
grid()
plot(om,t2g_7, 'r-', label="$t_{2g}$")
plot(om,eg_7, 'b-', label="$e_{g}$")
plot(om,dat7a[1],'g--',label="Total")
ax=gca()
for label in ax.get_xticklabels()+ax.get_yticklabels():
	label.set_fontsize(16)
legend(loc=0)
xlabel('$\omega$(eV)-->',fontsize=25)
savefig("../output/dos_a0a0a0_lt_b100.png")
show()
################################
t2g_8=(dat8[4]+dat8[4]+dat8[4])*(-1/pi)
eg_8=(dat8[2]+dat8[2])*(-1/pi)
xlim([-4,4])
ylim([0,8])
grid()
plot(om,t2g_8, 'r-', label="$t_{2g}$")
plot(om,eg_8, 'b-', label="$e_{g}$")
plot(om,dat8a[1],'g--',label="Total")
ax=gca()
for label in ax.get_xticklabels()+ax.get_yticklabels():
	label.set_fontsize(16)
legend(loc=0)
xlabel('$\omega$(eV)-->',fontsize=25)
savefig("../output/dos_a0a0a0_lt_b10.png")
show()
