# -*- coding: utf-8 -*-
"""

Problema Aula - H2
    
@author: Lucas E. Belino
"""
import cantera as ct
import numpy as np
import matplotlib.pyplot as plt


# Get all of the Species objects defined in the GRI 3.0 mechanism
species = {S.name: S for S in ct.Species.listFromFile('gri30.cti')}

# Create an IdealGas object with species representing complete combustion
complete_species = [species[S] for S in ('H2', 'O2','N2','H2O','H','O','N')]
gas1 = ct.Solution(thermo='IdealGas', species=complete_species)

phi = np.linspace(0.7, 1.3, 1000)
Temp = np.linspace(298, 800, 10)
Press = np.linspace(101325, 1013250, 20)


#Criando variáveis dependentes dos vetores para armazenamento de dados
c = np.zeros(phi.shape)
d = np.zeros(phi.shape)
a = np.zeros(phi.shape)

b = np.zeros(Temp.shape)
e = np.zeros(Temp.shape)
f = np.zeros(Temp.shape)

g = np.zeros(Press.shape)
h = np.zeros(Press.shape)
m = np.zeros(Press.shape)


for i in range(len(phi)):#variando Phi[0.7-1.3] com Pressão[atm] e Temperatura fixa[298] - armazenando fração molar dos componentes da mistura
        gas1.TP = 298, ct.one_atm
        gas1.set_equivalence_ratio(phi[i], 'H2', 'O2:0.5, N2:1.88')
        gas1.equilibrate('TP')
        c[i] = gas1['N2'].X
        d[i] = gas1['H2O'].X
        a[i] = gas1['H2'].X

for j in range(len(Temp)):#variando Temperatura[298-800] com Pressão[atm] e Phi fixo[1.0] - armazenando fração molar dos componentes da mistura
        gas1.TP = Temp[j], ct.one_atm
        gas1.set_equivalence_ratio(1.0, 'H2', 'O2:0.5, N2:1.88')
        gas1.equilibrate('HP')
        e[j] = gas1['N2'].X
        f[j] = gas1['H2O'].X
        b[j] = gas1['H2'].X

for k in range(len(Press)):#variando Pressão[atm-10xatm] com Phi fixo[1.0] - armazenando fração molar dos componentes da mistura
        gas1.TP = 298, Press[k]
        gas1.set_equivalence_ratio(1.0, 'H2', 'O2:0.5, N2:1.88')
        gas1.equilibrate('UV')
        h[k] = gas1['N2'].X
        m[k] = gas1['H2O'].X
        g[k] = gas1['H2'].X

#plotando grafico Phi x Fração Molar
plt.title(' Phi x Fração Molar % - T: 298K & P: 1.0atm')
plt.plot(phi, c,  ':',  label="N2",lw = 3)
plt.plot(phi, d,  ':',  label="H2O",lw = 3)
plt.plot(phi, a,  ':',  label="H2",lw = 3)
plt.grid(True)
plt.xlabel('Phi [H]')
plt.ylabel('Fração Molar [%]');
plt.legend(loc='upper left')
plt.show()

#plotando grafico Temperatura x Fração Molar
plt.title(' Temperatura de Entrada x Fração Molar % - phi: 1.0 & P: 1.0atm')
plt.plot(Temp, e,  ':',  label="N2",lw = 3)
plt.plot(Temp, f,  ':',  label="H2O",lw = 3)
plt.plot(Temp, b,  ':',  label="H2",lw = 3)
plt.grid(True)
plt.xlabel('Temp [K]')
plt.ylabel('Fração Molar [%]');
plt.legend(loc='upper left')
plt.show()


#plotando grafico Pressão x Fração Molar
plt.title(' Pressão Entrada x Fração Molar % - phi: 1.0 & T: 298K')
plt.plot(Press, h,  ':',  label="N2",lw = 3)
plt.plot(Press, m,  ':',  label="H2O",lw = 3)
plt.plot(Press, g,  ':',  label="H2",lw = 3)
plt.grid(True)
plt.xlabel('Pressão [kPa]')
plt.ylabel('Fração Molar [%]');
plt.legend(loc='upper left')
plt.show()

