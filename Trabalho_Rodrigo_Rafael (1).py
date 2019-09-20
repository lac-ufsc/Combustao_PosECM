"""
@author: Rodrigo silveira de Santiago e Rafael Trevisan 
Combustível: CH4 
"""
import cantera as ct 
import numpy as np
import matplotlib.pyplot as plt
## entrada (Define elementos, espécies e estado inicial)
cti_def = """ideal_gas(name='gri30' , elements= ' C H O N',

          species='gri30: CH4 O2 N2 CO2 H2O CO H2 NO NO2 OH H  ', 

          options=['skip_undeclared_elements'], 

          initial_state=state(temperature=298,pressure=101325))"""

T = [298, 600, 900] ## temperaturas analisadas
P = [ct.one_atm, 5*ct.one_atm,10*ct.one_atm] ## pressões analisadas 
Phi = [0.75,0.9,1.00,1.05,1.1,1.25] ## razões de equivalências analisadas
## teste para 298K e 1 atm
gas = ct.Solution(source=cti_def)
gas.TP = T[0], P[0] 
gas.set_equivalence_ratio(Phi[1],'CH4:1', 'O2:2, N2:7.52')
gas()
gas.equilibrate('HP')
gas()


## armazenamento de variáveis
Tad = np.zeros((len(T),len(P),len(Phi))) # temperatura de chama
xCO2 = np.zeros((len(T),len(P),len(Phi))) #Fração molar
xCO = np.zeros((len(T),len(P),len(Phi)))
xH2O = np.zeros((len(T),len(P),len(Phi)))
xH2 = np.zeros((len(T),len(P),len(Phi)))
xN2 = np.zeros((len(T),len(P),len(Phi)))
#Hr = np.zeros((len(T),len(P),len(Phi)))
#Hp = np.zeros((len(T),len(P),len(Phi)))
#deltaH = np.zeros((len(T),len(P),len(Phi)))

## resultados 
for i in range(len(T)): ## varre a matriz de resultados para T
    for ii in range(len(P)): ## varre a matriz de resultados para P
            for iii in range(len(Phi)): ## varre a matriz de resultados para Phi
                gas.TP = T[i], P[ii] ## define pressão 
                gas.set_equivalence_ratio(Phi[iii],'CH4:1', 'O2:2, N2:7.52')
#                Hr[i][ii][iii]=gas.enthalpy_mole*1e-3
                gas.equilibrate('HP')
#                Hp[i][ii][iii]=gas.enthalpy_mole*1e-3
                Tad[i][ii][iii]=gas.T
                xCO2[i][ii][iii]=gas['CO2'].X[0]
                xCO[i][ii][iii]=gas['CO'].X[0]
                xH2O[i][ii][iii]=gas['H2O'].X[0]
                xH2[i][ii][iii]=gas['H2'].X[0]
                xN2[i][ii][iii]=gas['N2'].X[0]
#                deltaH[i][ii][iii]=Hp[i][ii][iii]-Hr[i][ii][iii]
## plots                
Fig1 = plt.Figure()        
plt.plot(Phi ,Tad[0][0],'b^--',label = 'T = 298 K, 1 atm ')
plt.plot(Phi ,Tad[0][1],'r<--',label = 'T = 298 K, 5 atm ')
plt.plot(Phi ,Tad[0][2],'ko--',label = 'T = 298 K, 10 atm ')
plt.plot(Phi ,Tad[1][0],'m^--',label = 'T = 600 K, 1 atm ')
plt.plot(Phi ,Tad[1][1],'y<--',label = 'T = 600 K, 5 atm ')
plt.plot(Phi ,Tad[1][2],'co--',label = 'T = 600 K, 10 atm ')
plt.plot(Phi ,Tad[2][0],'g^--',label = 'T = 900 K, 1 atm ')
plt.plot(Phi ,Tad[2][1],'m<--',label = 'T = 900 K, 5 atm ')
plt.plot(Phi ,Tad[2][2],'c>--',label = 'T = 900 K, 10 atm ')
plt.grid(True)
plt.xlabel('phi')
plt.ylabel('Tad [K]');
plt.axis([0.5,2,1800,2700])
plt.legend(loc='center right')
plt.axis
plt.savefig('Tad.png')
plt.show()

Fig2 = plt.Figure()        
plt.plot(Phi ,xCO2[0][0],'b^--',label = 'T = 298 K, 1 atm ')
plt.plot(Phi ,xCO2[0][1],'r<--',label = 'T = 298 K, 5 atm ')
plt.plot(Phi ,xCO2[0][2],'ko--',label = 'T = 298 K, 10 atm ')
plt.plot(Phi ,xCO2[1][0],'m^--',label = 'T = 600 K, 1 atm ')
plt.plot(Phi ,xCO2[1][1],'y<--',label = 'T = 600 K, 5 atm ')
plt.plot(Phi ,xCO2[1][2],'co--',label = 'T = 600 K, 10 atm ')
plt.plot(Phi ,xCO2[2][0],'g^--',label = 'T = 900 K, 1 atm ')
plt.plot(Phi ,xCO2[2][1],'m<--',label = 'T = 900 K, 5 atm ')
plt.plot(Phi ,xCO2[2][2],'c>--',label = 'T = 900 K, 10 atm ')
plt.grid(True)
plt.xlabel('phi')
plt.ylabel('xCO2');
plt.axis([0.7,1.7,0.05,0.091])
plt.legend(loc='center right')
plt.axis
plt.savefig('xCO2.png')
plt.show()

Fig3 = plt.Figure()        
plt.plot(Phi ,xCO[0][0],'b^--',label = 'T = 298 K, 1 atm ')
plt.plot(Phi ,xCO[0][1],'r<--',label = 'T = 298 K, 5 atm ')
plt.plot(Phi ,xCO[0][2],'ko--',label = 'T = 298 K, 10 atm ')
plt.plot(Phi ,xCO[1][0],'m^--',label = 'T = 600 K, 1 atm ')
plt.plot(Phi ,xCO[1][1],'y<--',label = 'T = 600 K, 5 atm ')
plt.plot(Phi ,xCO[1][2],'co--',label = 'T = 600 K, 10 atm ')
plt.plot(Phi ,xCO[2][0],'g^--',label = 'T = 900 K, 1 atm ')
plt.plot(Phi ,xCO[2][1],'m<--',label = 'T = 900 K, 5 atm ')
plt.plot(Phi ,xCO[2][2],'c>--',label = 'T = 900 K, 10 atm ')
plt.grid(True)
plt.xlabel('phi')
plt.ylabel('xCO');
plt.axis([0.7,1.7,0.0,0.06])
plt.legend(loc='center right')
plt.axis
plt.savefig('xCO.png')
plt.show()

Fig4 = plt.Figure()        
plt.plot(Phi ,xH2O[0][0],'b^--',label = 'T = 298 K, 1 atm ')
plt.plot(Phi ,xH2O[0][1],'r<--',label = 'T = 298 K, 5 atm ')
plt.plot(Phi ,xH2O[0][2],'ko--',label = 'T = 298 K, 10 atm ')
plt.plot(Phi ,xH2O[1][0],'m^--',label = 'T = 600 K, 1 atm ')
plt.plot(Phi ,xH2O[1][1],'y<--',label = 'T = 600 K, 5 atm ')
plt.plot(Phi ,xH2O[1][2],'co--',label = 'T = 600 K, 10 atm ')
plt.plot(Phi ,xH2O[2][0],'g^--',label = 'T = 900 K, 1 atm ')
plt.plot(Phi ,xH2O[2][1],'m<--',label = 'T = 900 K, 5 atm ')
plt.plot(Phi ,xH2O[2][2],'c>--',label = 'T = 900 K, 10 atm ')
plt.grid(True)
plt.xlabel('phi')
plt.ylabel('xH2O');
plt.axis([0.7,1.7,0.135,0.195])
plt.legend(loc='center right')
plt.axis
plt.savefig('xH2O.png')
plt.show()

Fig5 = plt.Figure()        
plt.plot(Phi ,xH2[0][0],'b^--',label = 'T = 298 K, 1 atm ')
plt.plot(Phi ,xH2[0][1],'r<--',label = 'T = 298 K, 5 atm ')
plt.plot(Phi ,xH2[0][2],'ko--',label = 'T = 298 K, 10 atm ')
plt.plot(Phi ,xH2[1][0],'m^--',label = 'T = 600 K, 1 atm ')
plt.plot(Phi ,xH2[1][1],'y<--',label = 'T = 600 K, 5 atm ')
plt.plot(Phi ,xH2[1][2],'co--',label = 'T = 600 K, 10 atm ')
plt.plot(Phi ,xH2[2][0],'g^--',label = 'T = 900 K, 1 atm ')
plt.plot(Phi ,xH2[2][1],'m<--',label = 'T = 900 K, 5 atm ')
plt.plot(Phi ,xH2[2][2],'c>--',label = 'T = 900 K, 10 atm ')
plt.grid(True)
plt.xlabel('phi')
plt.ylabel('xH2');
plt.axis([0.7,1.7,0.0,0.04])
plt.legend(loc='center right')
plt.axis
plt.savefig('xH2.png')
plt.show()

Fig6 = plt.Figure()        
plt.plot(Phi ,xN2[0][0],'b^--',label = 'T = 298 K, 1 atm ')
plt.plot(Phi ,xN2[0][1],'r<--',label = 'T = 298 K, 5 atm ')
plt.plot(Phi ,xN2[0][2],'ko--',label = 'T = 298 K, 10 atm ')
plt.plot(Phi ,xN2[1][0],'m^--',label = 'T = 600 K, 1 atm ')
plt.plot(Phi ,xN2[1][1],'y<--',label = 'T = 600 K, 5 atm ')
plt.plot(Phi ,xN2[1][2],'co--',label = 'T = 600 K, 10 atm ')
plt.plot(Phi ,xN2[2][0],'g^--',label = 'T = 900 K, 1 atm ')
plt.plot(Phi ,xN2[2][1],'m<--',label = 'T = 900 K, 5 atm ')
plt.plot(Phi ,xN2[2][2],'c>--',label = 'T = 900 K, 10 atm ')
plt.grid(True)
plt.xlabel('phi')
plt.ylabel('xN2');
plt.axis([0.7,1.7,0.66,0.735])
plt.legend(loc='center right')
plt.axis
plt.savefig('xN2.png')
plt.show()

#Fig7 = plt.Figure()        
#plt.plot(Phi ,deltaH[0][0],'b^--',label = 'T = 298 K, 1 atm ')
#plt.plot(Phi ,deltaH[0][1],'r<--',label = 'T = 298 K, 5 atm ')
#plt.plot(Phi ,deltaH[0][2],'ko--',label = 'T = 298 K, 10 atm ')
#plt.plot(Phi ,deltaH[1][0],'m^--',label = 'T = 600 K, 1 atm ')
#plt.plot(Phi ,deltaH[1][1],'y<--',label = 'T = 600 K, 5 atm ')
#plt.plot(Phi ,deltaH[1][2],'co--',label = 'T = 600 K, 10 atm ')
#plt.plot(Phi ,deltaH[2][0],'g^--',label = 'T = 900 K, 1 atm ')
#plt.plot(Phi ,deltaH[2][1],'m<--',label = 'T = 900 K, 5 atm ')
#plt.plot(Phi ,deltaH[2][2],'c>--',label = 'T = 900 K, 10 atm ')
#plt.grid(True)
#plt.xlabel('phi')
#plt.ylabel('deltaH [kJ/kmol]');
#plt.axis([0.7,1.7,-600,450])
#plt.legend(loc='center right')
#plt.axis
#plt.savefig('xN2.png')
#plt.show()
#
