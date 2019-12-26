# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 14:10:52 2019

@author: Valentin Fenoux | Mathis Boutrouelle
"""
# Imports
import numpy as np
import matplotlib.pyplot as plt

# Constantes de test
Tfin = 10
Tau = 1

###--------------------Pas fixe--------------------###

def solver_euler_explicite(f,x0,dt) :
    vect_x = [x0]   # Vecteur de la solution
    x = x0
    vect_t = [0]    # Vecteur des temps
    n = Tfin//dt    # n : nombre de points sur l'intervalle de temps pour un dt donné
    for i in range(1,n) :
        x = x + i*dt*f(x)   # Application du schéma d'Euler
        vect_x.append(x)
        vect_t.append(i*dt)
    return(vect_t, vect_x)


###--------------------Test avec une équation connue--------------------###

t = np.linspace()
    