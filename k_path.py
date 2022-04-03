# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 01:38:32 2022

@author: User
"""
import math
import numpy as np

def k_path(a):
    NoPt = 8    # num of point between k-points
    ## k-path definition
    # X-Γ-M for sc
    k_X = [0,math.pi/a,0]
    k_G = [0,0,0]
    k_M = [math.pi/a,math.pi/a,0]
    
    # dimensions: (k_path,k_xyz)
    k_XG = np.add(
        k_X,
        np.multiply(np.subtract(k_G,k_X),np.linspace(0,1,num=NoPt).reshape(NoPt,1))
        )
    k_GM = np.add(
        k_G,
        np.multiply(np.subtract(k_M,k_G),np.arange(NoPt).reshape(NoPt,1))/NoPt
        )
    k = np.concatenate((k_XG,k_GM),axis=0)
    
    return k