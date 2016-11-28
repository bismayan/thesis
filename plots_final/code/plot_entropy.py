from scipy import *
from pylab import *

dat1=loadtxt("../files/Entropy_files/Entropy_lt.dat").transpose()
dat2=loadtxt("../files/Entropy_files/Entropy_ht.dat").transpose()
T=dat1[0]*11600
plot(T,dat1[1],'ro-',label="Low Temp Struct")
plot(T,dat2[1],'bo-',label="High Temp Struct")
legend(loc=0)
xlabel("T-->")
ylabel("S-->")
grid()
show()
savefig("../output/Entropy.eps")

