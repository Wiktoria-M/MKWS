import math
import sdtoolbox as sd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import cantera


p_0_min =100000 ; 
p_0_max =1000000 ;
T_0_min =300 ;
T_0_max =1000 ;
PHI_0_min = 0.5;
PHI_0_max = 1.5;
p_imax =5 ;
T_jmax = 7;
PHI_kmax = 5;

mech = 'gri30.cti';

p0 = np.zeros(p_imax);
p0bar = np.zeros(p_imax);
T0 = np.zeros(T_jmax);
PHI = np.zeros(PHI_kmax);
U_CJ = np.zeros((p_imax, T_jmax, PHI_kmax));

for i in range(0,p_imax):
    p0[i] = p_0_min + i*(p_0_max - p_0_min)/(p_imax - 1);
    p0bar[i] = p0[i]/100000;
    for j in range(0,T_jmax):
        T0[j] = T_0_min + j*(T_0_max - T_0_min)/(T_jmax - 1);
        for k in range(0,PHI_kmax):
            PHI[k] = PHI_0_min + k*(PHI_0_max - PHI_0_min)/(PHI_kmax - 1);
            x = 'H2:%.2f O2:1 N2:3.76' % PHI[k];
            U_CJ[i , j , k] = sd.postshock.CJspeed(p0[i] , T0[j], x , mech);
            print("gowno")
        k = 0;
    j = 0;

font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 18}

plt.rc('font', **font)

plt.figure(figsize=(20,10))
for l in range(int(p_imax)):
    plt.plot(PHI, U_CJ[l,0,:], label = 'p0 = %.1f bar' % p0bar[l])
    plt.plot()
plt.xlabel('Equivalence ratio $\phi$ [-]')
plt.ylabel('CJ detonation speed [m/s]')
plt.title("")
plt.legend()
plt.show()
#plt.savefig('CJU_phi_p1var.png')

plt.figure(figsize=(20,10))
for l in range(int(T_jmax)):
    plt.plot(PHI, U_CJ[0,l,:], label = 'T0 = %.0f K' % T0[l])
    plt.plot()
plt.xlabel('Equivalence ratio $\phi$ [-]')
plt.ylabel('CJ detonation speed [m/s]')
plt.title("")
plt.legend()
plt.show()
#plt.savefig('CJU_phi_T1var.png')

plt.figure(figsize=(20,10))
for l in range(int(T_jmax)):
    plt.plot(p0bar, U_CJ[:,l,3], label = 'T0 = %.0f K' % T0[l])
plt.xlabel('Preassure [bar]')
plt.ylabel('CJ detonation speed [m/s]')
plt.title("")
plt.legend()
plt.show()
#plt.savefig('CJU_p1_T1var.png')
             
plt.figure(figsize=(20,10))
for l in range(int(PHI_kmax)):
    plt.plot(p0bar, U_CJ[:,0,l], label = '$\phi$ = %.1f' % PHI[l])
plt.xlabel('Preassure [bar]')
plt.ylabel('CJ detonation speed [m/s]')
plt.title("")
plt.legend()
plt.show()
#plt.savefig('CJU_p1_phivar.png')

plt.figure(figsize=(20,10))
for l in range(int(p_imax)):
    plt.plot(T0, U_CJ[l,:,3], label = 'p0 = %.1f bar' % p0bar[l])
plt.xlabel('Temperature [K]')
plt.ylabel('CJ detonation speed [m/s]')
plt.title("")
plt.legend()
plt.show()
#plt.savefig('CJU_T1_p1var.png')

plt.figure(figsize=(20,10))
for l in range(int(PHI_kmax)):
    plt.plot(T0, U_CJ[0,:,l], label = '$\phi$ = %.1f' % PHI[l])
plt.xlabel('Temperature [K]')
plt.ylabel('CJ detonation speed [m/s]')
plt.title("")
plt.legend()
plt.show()
#plt.savefig('CJU_T1_phivar.png')




















            
