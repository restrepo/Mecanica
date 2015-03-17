from pylab import *
import sys
def ellipse(x,a,e):
    if e>1:
        sys.exit("e=%g, not an ellipse" %e)
        
    b=np.sqrt(a**2*(1.-e**2))
    return np.sqrt(b**2*(1.-(x-a*e)**2/a**2))


class orbit:
    '''
    orbit properties
    '''
    def __init__(self):
        self.a=0
        self.e=0
    def __call__(self):
        print("call")

    def getorbit(self,a=0,e=0):
        self.a=a
        self.e=e
        
if __name__ == '__main__':
    """
    a in units of 10^6 Km
    """
    #From http://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
    npoints=200
    earth=orbit()
    earth.getorbit(a=149.60,e=0.0167)
    x=np.linspace(-(earth.a-earth.a*earth.e),earth.a+earth.a*earth.e,npoints)
    plt.plot(x,ellipse(x,earth.a,earth.e),'k-',label='Tierra')
    plt.plot(x,-ellipse(x,earth.a,earth.e),'k-')
    meteor=orbit()
    #http://en.wikipedia.org/wiki/2013_Russian_meteor_event
    #meteor original
    #meteor.getorbit(a=394.94,e=0.51)
    meteor.getorbit(a=394.94,e=0.71)
    x=np.linspace(-(meteor.a-meteor.a*meteor.e),meteor.a+meteor.a*meteor.e,npoints)
    plt.plot(x,ellipse(x,meteor.a,meteor.e),'b--',label='Meteoro')
    plt.plot(x,-ellipse(x,meteor.a,meteor.e),'b--')
    aT=earth.a;eT=earth.e
    aM=meteor.a;eM=meteor.e
    xsol=(aT*(1-eT**2)-aM*(1-eM**2))/(eM-eT)
    plt.plot(xsol,ellipse(xsol,aT,eT),'ro')
    plt.plot(xsol,-ellipse(xsol,aT,eT),'ro')
    plt.xlabel(r'$x\quad (\times 10^6$ Km)',size=20)
    plt.ylabel(r'$y\quad (\times 10^6$ Km)',size=20)
    plt.plot(0,0,'y*',ms=20.)
    plt.show()
    plt.savefig('orbitcollision.pdf')
    legend(loc='best')
    print "The solution is: (x_1,y_1)=(%g,%g)" %(xsol,ellipse(xsol,aT,eT))
    print "Text: yM=yT: %g=%g" %( ellipse(xsol,aM,eM),ellipse(xsol,aT,eT) )
