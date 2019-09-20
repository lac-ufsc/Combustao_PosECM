#import packages
import cantera as ct
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

#import gas object
gas = ct.Solution("gri30.cti")

#define some auxiliary variable
Patm = ct.one_atm #[Pa]

#define gas condition
#equivalence ratio
phi = np.linspace(0.6,1.4,15)
#initial temperature
Tin = np.linspace(298,1000,15) #[K]
#initial pressure
Pin = np.linspace(Patm,100*Patm,15)

#define results array
Xout = []
Tad = []

#equivalence ratio loop
for i in phi:
    #define some auxiliary array
    aux11 = []
    aux22 = []
    
    #initial temperature loop
    for j in Tin:
        
        #define some auxiliary array
        aux1 = []
        aux2 = []

        #initial pressure loop
        for k in Pin:
            #define the gas condition
            gas.TP = j, k
            #set the equivalence ratio
            gas.set_equivalence_ratio(i,"C2H6","O2:1.0,N2:3.76")

            #equilibrate the gas
            gas.equilibrate("HP")
            
            #save the results
            aux1.append(gas.T)
            aux2.append(gas.X)
            
        #realocate the results
        aux11.append(aux1)
        aux22.append(aux2)
    
    #realocate the results
    Tad.append(aux11)
    Xout.append(aux22)         
            
#%% post processing
            
#redefine to numpy array
Tad = np.array(Tad)
Xout = np.array(Xout)

#define some params
Tmesh, phimesh = np.meshgrid(Tin,phi)


#plot the results
plot = 3
#if plot 1 - pressure influence plot
#if plot 2 - adiabatic temperature plot for phi x Tin
#if plot 3 - #NO formation plot
#if plot 4 - #H2O formation plot
#if plot 5 - #CO2 formation plot
#if plot 6 - #CO formation plot
#if plot 7 - #H2 formation plot
#if plot 8 - #NO2 formation plot
#if plot 9 - #O2 formation plot

if plot != 0:
    
    #pressure influence plot
    if plot==1:
        
        fig = plt.figure()
        fig.set_size_inches(14, 7)
        plt.rcParams.update({'font.size': 14}) 
        
        ax = fig.add_subplot(121)
        ax.plot(Pin/Patm,Tad[0,0,:],'--k',label="$\Phi$=0.6")
        ax.plot(Pin/Patm,Tad[int(len(phi)/2),0,:],'-k',label="$\Phi$=1")
        ax.plot(Pin/Patm,Tad[-1,0,:],':k',label="$\Phi$=1.4")
        ax.legend(loc='best')
        ax.set_xlabel("Pressure [atm]")
        ax.set_ylabel("Adiabatic Temperature [K]")
        ax.set_title("T$_{in}$ = 298 [K]")

        ax2 = fig.add_subplot(122)
        ax2.plot(Pin/Patm,Tad[int(len(phi)/2),0,:],'--k',label="T$_{in}$= 298 [K]")
        ax2.plot(Pin/Patm,Tad[int(len(phi)/2),int(len(Tin)/2),:],'-k',label="T$_{in}$= 649 [K]")
        ax2.plot(Pin/Patm,Tad[int(len(phi)/2),-1,:],':k',label="T$_{in}$= 1000 [K]")
        ax2.legend(loc='right')
        ax2.set_xlabel("Pressure [atm]")
        ax2.set_ylabel("Adiabatic Temperature [K]")
        ax2.set_title("$\Phi$ = 1")


    #adiabatic temperature plot for phi x Tin
    if plot==2:
        
        fig = plt.figure()
        
        plt.rcParams.update({'font.size': 14}) 
        fig.set_size_inches(11, 7)
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(phimesh,Tmesh,Tad[:,:,0], cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)


        ax.set_xlabel("$\Phi$ [-]")
        ax.set_ylabel("T$_{in}$ [K]")
        ax.set_zlabel("T$_{ad}$ [K]")
        ax.set_title("P = 1 atm")
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()

    #NO formation plot
    if plot==3:
        
        fig = plt.figure()
        
        plt.rcParams.update({'font.size': 14}) 
        fig.set_size_inches(11, 7)
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(phimesh,Tmesh,Xout[:,:,0,gas.species_index("NO")]*1e6, 
                       cmap=cm.coolwarm, linewidth=0, antialiased=False)

        ax.set_xlabel("$\Phi$ [-]")
        ax.set_ylabel("T$_{in}$ [K]")
        ax.set_zlabel("ppm$_{NO}$")
        ax.set_title("P = 1 atm")
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()
        
    #H2O formation plot
    if plot==4:
        
        fig = plt.figure()
        
        plt.rcParams.update({'font.size': 14}) 
        fig.set_size_inches(11, 7)
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(phimesh,Tmesh,Xout[:,:,0,gas.species_index("H2O")], 
                       cmap=cm.coolwarm, linewidth=0, antialiased=False)

        ax.set_xlabel("$\Phi$ [-]")
        ax.set_ylabel("T$_{in}$ [K]")
        ax.set_zlabel("X$_{H2O}$")
        ax.set_title("P = 1 atm")
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()
        
    #CO2 formation plot
    if plot==5:
        
        fig = plt.figure()
        
        plt.rcParams.update({'font.size': 14}) 
        fig.set_size_inches(11, 7)
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(phimesh,Tmesh,Xout[:,:,0,gas.species_index("CO2")], 
                       cmap=cm.coolwarm, linewidth=0, antialiased=False)

        ax.set_xlabel("$\Phi$ [-]")
        ax.set_ylabel("T$_{in}$ [K]")
        ax.set_zlabel("X$_{CO2}$")
        ax.set_title("P = 1 atm")
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()
    
    #CO formation plot
    if plot==6:
        
        fig = plt.figure()
        
        plt.rcParams.update({'font.size': 14}) 
        fig.set_size_inches(11, 7)
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(phimesh,Tmesh,Xout[:,:,0,gas.species_index("CO")], 
                       cmap=cm.coolwarm, linewidth=0, antialiased=False)

        ax.set_xlabel("$\Phi$ [-]")
        ax.set_ylabel("T$_{in}$ [K]")
        ax.set_zlabel("X$_{CO}$")
        ax.set_title("P = 1 atm")
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()
       
    #H2 formation plot
    if plot==7:
        
        fig = plt.figure()
        
        plt.rcParams.update({'font.size': 14}) 
        fig.set_size_inches(11, 7)
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(phimesh,Tmesh,Xout[:,:,0,gas.species_index("H2")], 
                       cmap=cm.coolwarm, linewidth=0, antialiased=False)

        ax.set_xlabel("$\Phi$ [-]")
        ax.set_ylabel("T$_{in}$ [K]")
        ax.set_zlabel("X$_{H2}$")
        ax.set_title("P = 1 atm")
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()

    #NO2 formation plot
    if plot==8:
        
        fig = plt.figure()
        
        plt.rcParams.update({'font.size': 14}) 
        fig.set_size_inches(11, 7)
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(phimesh,Tmesh,Xout[:,:,0,gas.species_index("NO2")]*1e6, 
                       cmap=cm.coolwarm, linewidth=0, antialiased=False)

        ax.set_xlabel("$\Phi$ [-]")
        ax.set_ylabel("T$_{in}$ [K]")
        ax.set_zlabel("ppm$_{NO2}$")
        ax.set_title("P = 1 atm")
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()
    
    #O2 formation plot    
    if plot==9:
        
        fig = plt.figure()
        
        plt.rcParams.update({'font.size': 14}) 
        fig.set_size_inches(11, 7)
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(phimesh,Tmesh,Xout[:,:,0,gas.species_index("O2")], 
                       cmap=cm.coolwarm, linewidth=0, antialiased=False)

        ax.set_xlabel("$\Phi$ [-]")
        ax.set_ylabel("T$_{in}$ [K]")
        ax.set_zlabel("X$_{O2}$")
        ax.set_title("P = 1 atm")
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()