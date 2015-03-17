#!/usr/bin/env python
#http://www.pha.jhu.edu/~broholm/l5/node3.html
from pylab import *
global g
g=9.8
def y(x,theta=45,v0=10):
    '''theta in degrees'''
    thetarad=theta*np.pi/180.
    return np.tan(theta)*x-g/(2.*(v0*np.cos(theta))**2)*x**2
if __name__ == '__main__':
    x=np.linspace(0,250)
    xx=np.arange(0,250,50)
    plt.plot(x,y(x,v0=60))
    plt.plot(xx,y(xx,v0=60),'ro')
    plt.grid()
    plt.show()
    

