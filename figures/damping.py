#!/usr/bin/env/python
from pylab import *
gamma=0.5
omega=5
t=np.linspace(0,10,1000)
plt.plot(t,np.exp(-gamma/2.*t),'k--')
plt.plot(t,-np.exp(-gamma/2.*t),'k--')
plt.plot(t,np.exp(-gamma/2.*t)*cos(omega*t),'k-')
plt.ylabel(r'$x(t)$',size=20)
plt.xlabel(r'$t$',size=20)
plt.savefig('damping.pdf')
plt.show()
