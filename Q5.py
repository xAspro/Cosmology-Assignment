import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

H0=[70,70,70,70,70*121.8]

data=np.array([[1e-5,0.3,0.7,0],[1e-5,0.3,0.7,0.9],[1e-5,0.3,0.7,-0.6],[1e-5,0.8,0.2,0],[0.001222,0.99878,4.72*10**-5,0]]) #wr,wm,wde,wde*(1+z)^?,title
Tdata=np.transpose(data)
TITLE=["FLCDM Model","FDECM Model with $\omega_{DE}= -0.7$","FDECDM Model with $\omega_{DE}= -1.2$","FLCDM Model with $\Omega_{m}= 0.8$","FLCDM Model with $T_0=100K$"]
##Now, Tdata[0]=wr,.. Tdata[3]=powers

wr=Tdata[0].copy()
wm=Tdata[1].copy()
wd=Tdata[2].copy()
power=Tdata[3].copy()
# tit=Tdata[4].copy()

color_codes = ['b', 'g', 'r', 'c']


def integrand(z,H0,wr,wm,wd,power):
    return 1/(H0*np.sqrt(wr*(1+z)**4+wm*(1+z)**3+wd*(1+z)**power))

def dist(res,k,alpha):
    # print("res= ",res)
    # print("alpha= ",alpha)
    if k==0:
        # print('in k=0')
        # print('res*alpha= ',res*alpha)
        return res*alpha
    if k==1:
        # print('in k=1')
        # print('res= ',res)
        return res
    # print('in k=2,3')
    # print('res/alpha= ',res/alpha)
    return res/alpha

# vInt=vectorize(integrand,excluded=['wr','wm','wd','power'])     ##Vectoriezed integrand

tit=["Luminosity Distance","Comoving Distance","Angular Diameter Distance","Proper Distance"]
def plotting(z,mark,ls,alpha=1):
    for j in range(len(wr)):
        print(f"For {TITLE[j]}:")
        for k in range(len(tit)):
            print(f"\tFor {tit[k]}")
            res=[]
            for i in range(len(z)):
                lowLimit=0
                upLimit=z[i]
                results,_=quad(integrand,lowLimit,upLimit,args=(H0[j],wr[j],wm[j],wd[j],power[j]))
                alpha=(1+z[i])
                
                res.append(dist(results,k,alpha))       ##To get it in terms of gigayears
                print(f"\t\tFor z= {z[i]}\tIntegration value={res[-1]}")
            plt.plot(z,res,color=color_codes[k],marker=mark,linestyle=ls,label=f'{tit[k]}')
            # print(res)
        plt.title(f'{TITLE[j]}')
        plt.legend(fontsize='small')
        plt.xscale("log")
        plt.yscale("log")
        plt.xlabel("log z")
        plt.ylabel("log distance (in terms of $1/H_0$)")
        plt.show()
        

z=np.array([0,2,6,1100])

# plt.figure(figsize=(12,6.5))
plotting(z,'o',None)
# z=np.linspace(0,1100,110)
# plotting(z,None,None)
