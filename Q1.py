import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

z=np.array([0.01,0.012,0.016,0.02167,0.0343,0.0593])
dl=np.array([38.8,60.6,73.8,87.0,140.4,268.7])
zH=z.copy()
dp=dl.copy()
c=3*10**5

H1=1
H0=0
vp=0
tol=1e-10           ##Taking tolerance as 1e-10
i=0


while(abs(H0-H1)>=tol):
    dp= dl*(1+zH)**2

    
    H1=H0

    H0,vp,_,_,_=linregress(dp,c*z)


    #updates zH

    zH=H0*dp/c
    i=i+1

print("After ",i," iterations, we got H0= ",H0,"km/s/Mpc within a tolerance of ",tol,"km/s/Mpc and corresponding vp= ",vp,"km/s")


plt.figure(figsize=(8, 6))

dl2=np.linspace(0,300,10000)
plt.scatter(dl,z,color='black',marker='o',label='Observed Data(uses $d_l$)')

H02d = "{:.2f}".format(H0)
vpc2d = "{:.2e}".format(vp/c)

plt.plot(dl2,(dl2*H0+vp)/c,label=f'Best fit curve(uses $d_p$)\nSlope=$H_0$={H02d}')

plt.scatter(0,vp/c,color='r',marker='x',s=80,label=f'Intercept=$z_{{pec}}$={vpc2d}')
plt.xlabel('Distance(Mpc)')
plt.ylabel('Redshift(z)')
plt.title('Hubble Law and Peculiar Velocities')
plt.legend()
plt.grid(True)
plt.xlim(-5,300)
plt.ylim(-0.001,0.1)
plt.show()

