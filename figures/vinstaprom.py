#!/usr/bin/env python
from pylab import *
from matplotlib import rc
rc('text', usetex=True)

x=np.zeros((3,2))
x[0]=np.array([0,0])
x[1]=np.array([1.,70.])
x[2]=np.array([2.,100.])
plt.plot(x[:,0],x[:,1],'k-',lw=2)
plt.plot(x[:,0],x[:,1],'ro')
plt.xlabel(r'$t$ [h]',size=20)
plt.ylabel(r'$d$ [Km]',size=20)
       
plt.ylim(0,120)
plt.xlim(0,2.2)
plt.grid()
plt.savefig('vinstaprom1.pdf')

plt.vlines(1,ylim()[0],70,color='b', linestyles='dashed')
plt.ylim(0,120)
plt.xlim(0.,2.2)
plt.text(1.05,35,r'$v_1=\bar{v}_1=\frac{70\ \hbox{Km}}{1\ \hbox{h}}=70\ \hbox{Km/h}$',fontsize=20)
plt.text(0.8,72,'(1,70)',size=20)
plt.savefig('vinstaprom2.pdf')


plt.vlines(2,70,100,color='g', linestyles='dashed')
plt.hlines(70,1,2,color='g', linestyles='dashed')
plt.text(1.9,102,'(2,100)',size=20)
plt.ylim(0,120)
plt.xlim(0.,2.2)
plt.savefig('vinstaprom3.pdf')

plt.show()
#
