import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

H0=[70,70,70,70,70*121.8]

data=np.array([[1e-5,0.3,0.7,0],[1e-5,0.3,0.7,0.9],[1e-5,0.3,0.7,-0.6],[1e-5,0.8,0.2,0],[0.001222,0.99878,4.72*10**-5,0]]) #wr,wm,wde,wde*(1+z)^?,title
Tdata=np.transpose(data)
tit=["FLCDM Model","FDECM Model with $\omega_{DE}= -0.7$","FDECDM Model with $\omega_{DE}= -1.2$","FLCDM Model with $\Omega_{m}= 0.8$","FLCDM Model with $T_0=100K$"]
##Now, Tdata[0]=wr,.. Tdata[3]=powers

wr=Tdata[0].copy()
wm=Tdata[1].copy()
wd=Tdata[2].copy()
power=Tdata[3].copy()
# tit=Tdata[4].copy()

cnt=0
color_codes = ['b', 'g', 'r', 'c', 'm']

def integrand(z,H0,wr,wm,wd,power):
    return 1/(H0*(1+z)*np.sqrt(wr*(1+z)**4+wm*(1+z)**3+wd*(1+z)**power))
    
# vInt=vectorize(integrand,excluded=['wr','wm','wd','power'])     ##Vectoriezed integrand

def plotting(z,mark,ls,tit2):
    global cnt
    for j in range(len(wr)):
        if cnt==0:
            print(f"For {tit[j]}:")
        res=[]
        for i in range(len(z)):
            lowLimit=0
            upLimit=z[i]
            results,_=quad(integrand,lowLimit,upLimit,args=(H0[j],wr[j],wm[j],wd[j],power[j]))
        
            res.append(results*10**3)       ##To get it in terms of gigayears
            if cnt==0:
                print(f"\tFor z= {z[i]}\tIntegration value is {res[-1]}")
        plt.plot(z,res,color=color_codes[j],marker=mark,linestyle=ls,label=f'{tit2}{tit[j]}')
        # print(res)
    plt.title('Lookback Time vs Redshift')
    cnt=cnt+1

z=np.array([0,2,6,1100])

plt.figure(figsize=(12,6.5))
plotting(z,'o','','Required Data points for ')
z=np.linspace(0,1100,1100)
plotting(z,None,None,'')
plt.xscale("log")
plt.yscale("log")
plt.legend(fontsize='small')
plt.xlabel("log z")
plt.ylabel("log $T_{LB}$ (in terms of Gyears)")
plt.show()

z=np.array([0,2,6,1100])

plt.figure(figsize=(12,6.5))
plotting(z,'o','','Required Data points for ')
z=np.linspace(0,1100,1100)
plotting(z,None,None,'')
plt.legend(fontsize='small')
plt.xlabel("z")
plt.ylabel("$T_{LB}$ (in terms of Gyears)")
plt.show()
