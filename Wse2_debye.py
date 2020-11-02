import numpy as np
import scipy.integrate as integrate
import math
import matplotlib.pyplot as plt
# Constant=9*N*KB
constant = 9*6*1.38*math.pow(10,-23)
filer = open('VolumeTemp-WSe2.dat','r')
filew = open('Wse2_Fit_VT.dat','w')
lines = filer.readlines()
filer.close()
#Td is the DebyeTemp
Td=160
# X and Y are the experimental data from the input file
# X is the temperature
x = []
y = []
for line in lines[1:50]:
    p = line.split()
    x = p[0]
    y = p[1]
    # U= constant*T*(T/Td)^3*intergration of t^3/(e^t-1) from 0 to Td/T
    fa = lambda t: (t ** 3 / ((np.exp(t)) - 1))
    integration_factor = (integrate.quad(fa, 0, (Td / float(x))))
    U = constant*float(x) * math.pow((float(x) / Td), 3) * (integration_factor[0])
    # V_T = (gamma'/K)*U, where gamma' = 0.792 and K=72 Gpa, gamma'/K= 0.01x10^-9/Pascal
    V_T = (0.01111*math.pow(10,-9)*U)*math.pow(10,30)+120.79
    print(x,V_T)
    plt.scatter(float(x),V_T,c="blue")
    plt.plot(float(x),float(y),c="red")
    filew.write(str(float(x)) + "\t" + str(y) + "\t" + str(V_T) + "\n")
plt.show()
filew.close()





