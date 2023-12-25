import numpy as np
import matplotlib.pyplot as plt

z=[0,6,20,1090,1e4]
h=6.626*10**-34
c=3*10**8
k=1.38*10**-23
T=2.7255

def B(v,T,z):
    return (2*h*(v/(1+z))**3)/c**2*1/(np.exp((h*v)/(k*T))-1)
    
p=(np.linspace(7,15,50))
v=np.power(10,p)
for i in range(len(z)):
    print("z[i]= ",z[i])
    plt.plot(v,B(v,T,z[i]),label=f"for z={z[i]}")

plt.title("BB radiation Spectrum of the Universe")
plt.legend()
plt.xlabel("frequency(Hz)")
plt.ylabel("Radiation spectral density")
plt.xscale("log")
plt.yscale("log")
plt.show()
