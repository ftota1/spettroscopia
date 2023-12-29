
import numpy as np
from scipy.special import voigt_profile
def gaussiana(x,a,s,mu):
    return a*np.exp(-(x-mu)**2/(2*s**2))/(s*np.sqrt(2*np.pi))
def lorenziana(x,a,g,mu):
    return a*(g/(2*np.pi))/((g/2)**2+(x-mu)**2)
def pseudo_Voigt1(x,s,mu,g,p):
    return p*np.exp(-(x-mu)**2/(2*s**2))/(s*np.sqrt(2*np.pi))+(1-p)*(g/(2*np.pi))/((g/2)**2+(x-mu)**2)
def voigt(x,a,s,mu,g):
    return a*voigt_profile(x-mu,s,g)
def max_boltz(x,vmax,C,mu):
     return C*((1/(np.pi*vmax**2))**(3/2))*(4*np.pi)*((x-mu)**2)*np.exp(-(((x-mu)/vmax)**2)) #vamx^2=2kT/m
if __name__=='__main__':
	print('Testing my module')
	assert 0==0#fal_body(0) == (0,0)