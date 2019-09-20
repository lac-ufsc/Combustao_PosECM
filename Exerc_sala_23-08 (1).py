# -*- coding: utf-8 -*-
"""
Lista 3 - Combustão

Equilíbrio químico da combustão a pressão constante, em AR padrão, com reagentes a 298K

CO

@author: Félix Dal Pont Michels Júnior e Vanessa Batista
"""
#Bibliotecas
import cantera as ct
import numpy as np
import matplotlib.pyplot as plt

gas = ct.Solution('gri30.xml'); # Importação do GRI-Mech 3.0
a = 0.5; # Estequiometria O2

phi = np.linspace(0.5, 2.0, 5); # Vetor da razão estequiométrica variando de 0.5 a 2.0 com 5 divisões
Ti = np.linspace(298, 1000, 5); # Vetor da temperatura variando de 298K a 1000K com 5 divisões
Pr= np.linspace(ct.one_atm, 5*ct.one_atm, 5); # Vetor da pressão variando de 1 atm a 5 atm com 5 divisões

# Criação das matrizes para amarzenar os dados

P_phi=  np.zeros((len(phi), len(phi)));
T_complete_phi = np.zeros((len(phi), len(phi)));
T_complete_Pr = np.zeros((len(phi), len(phi)));
P_Pr =  np.zeros((len(phi), len(phi)));
X_phi = np.zeros((len(phi), len(phi)));
X_phi1 = np.zeros((len(phi), len(phi)));
X_phi2 = np.zeros((len(phi), len(phi)));
X_Pr = np.zeros((len(phi), len(phi)));
X_Pr1 = np.zeros((len(phi), len(phi)));
X_Pr2 = np.zeros((len(phi), len(phi)));

for i in range(len(Ti)):
    for j in range(len(phi)):
        gas.TP = Ti[i], ct.one_atm; # Temperatura e pressão dos reagentes
        gas.set_equivalence_ratio(phi[j], 'CO', {'O2':a, 'N2':a*3.76}); # Reagentes e razão estequimétrica
        gas.equilibrate('HP'); # Equilibra a reação
        T_complete_phi[i,j] = gas.T; # Temperatura adiabática segundo a razão estequimétrica
        X_phi[i,j] = gas.X[gas.species_index("CO")]; # Fração molar da espécie CO
        X_phi1[i,j] = gas.X[gas.species_index("CO2")]; # Fração molar da espécie CO2
        X_phi2[i,j] = gas.X[gas.species_index("N2")]; # Fração molar da espécie N2
    plt.figure(1);
    plt.plot(phi, T_complete_phi[i], lw=2, label= r"$T_i[K]=$" + str(Ti[i]));
    plt.figure(3)
    plt.plot(phi, X_phi[i], lw=2, label= r"$T_i[K]=$" + str(Ti[i]))
    plt.figure(4)
    plt.plot(phi, X_phi1[i], lw=2, label= r"$T_i[K]=$" + str(Ti[i]))
    plt.figure(5)
    plt.plot(phi, X_phi2[i], lw=2, label= r"$T_i[K]=$" + str(Ti[i]))
        
for i in range(len(Pr)):
    for k in range(len(phi)):
        gas.TP = 298, Pr[i]; # Temperatura e pressão dos reagentes
        gas.set_equivalence_ratio(phi[k], 'CO', {'O2':a, 'N2':a*3.76}); # Reagentes e razão estequimétrica
        gas.equilibrate('HP'); # Equilibra a reação
        T_complete_Pr[i,k] = gas.T; # Temperatura adiabática segundo a razão estequimétrica
        X_Pr[i,k] = gas.X[gas.species_index("CO")]; # Fração molar da espécie CO
        X_Pr1[i,k] = gas.X[gas.species_index("CO2")]; # Fração molar da espécie CO2
        X_Pr2[i,k] = gas.X[gas.species_index("N2")]; # Fração molar da espécie N2
    plt.figure(2)
    plt.plot(phi, T_complete_Pr[i], lw=2, label= r"$P_r[K]=$" + str(Pr[i]))
    plt.figure(6)
    plt.plot(phi, X_Pr[i], lw=2, label= r"$P_r[K]=$" + str(Pr[i]))
    plt.figure(7)
    plt.plot(phi, X_Pr1[i], lw=2, label= r"$P_r[K]=$" + str(Pr[i]))
    plt.figure(8)
    plt.plot(phi, X_Pr2[i], lw=2, label= r"$P_r[K]=$" + str(Pr[i]))
    
                
# Gráficos


plt.figure(1);
plt.grid(True);
plt.xlabel('Equivalence ratio, $\phi$');
plt.ylabel('Temperature [K]');
plt.title("Tad por phi em diferente temperaturas iniciais");
plt.legend();

plt.figure(2);
plt.grid(True);
plt.xlabel('Equivalence ratio, $\phi$');
plt.ylabel('Temperature [K]');
plt.title("Tad por phi, em diferentes pressoes da reação");
plt.legend();

plt.figure(3);
plt.grid(True);
plt.xlabel('Equivalence ratio, $\phi$');
plt.ylabel('Fração molar');
plt.title("Fração molar de CO por phi, em diferentes temperaturas");
plt.legend();

figura1=plt.figure(4);
plt.grid(True);
plt.xlabel('Equivalence ratio, $\phi$');
plt.ylabel('Fração molar');
plt.title("Fração molar de CO2 por phi, em diferentes temperaturas");
plt.legend();

plt.figure(5);
plt.grid(True);
plt.xlabel('Equivalence ratio, $\phi$');
plt.ylabel('Fração molar');
plt.title("Fração molar de N2 por phi, em diferentes temperaturas");
plt.legend();

plt.figure(6);
plt.grid(True);
plt.xlabel('Equivalence ratio, $\phi$');
plt.ylabel('Fração molar');
plt.title("Fração molar de CO por phi, em diferentes pressoes");
plt.legend();

plt.figure(7);
plt.grid(True);
plt.xlabel('Equivalence ratio, $\phi$');
plt.ylabel('Fração molar');
plt.title("Fração molar de CO2 por phi, em diferentes pressoes");
plt.legend();

plt.figure(8);
plt.grid(True);
plt.xlabel('Equivalence ratio, $\phi$');
plt.ylabel('Fração molar');
plt.title("Fração molar de N2 por phi, em diferentes pressoes");
plt.legend();