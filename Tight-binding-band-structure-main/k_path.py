# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 01:38:32 2022

@author: User
"""
import math
import numpy as np

def k_path(UnitCellType,a):
    NoPt = 12    # num of point between k-points
    if UnitCellType == 'SC':
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
        k_MX = np.add(
            k_M,
            np.multiply(np.subtract(k_X,k_M),np.arange(NoPt).reshape(NoPt,1))/NoPt
            )
        k = np.concatenate((k_XG,k_GM,k_MX),axis=0)
    elif UnitCellType =='BCC':
        k_G = [0,0,0]
        k_P = [math.pi/a,math.pi/a,math.pi/a]
        k_N = [0,math.pi/a,math.pi/a]
        k_PG = np.add(
            k_P,
            np.multiply(np.subtract(k_G,k_P),np.arange(NoPt).reshape(NoPt,1))/NoPt
            )
        k_GN = np.add(
            k_G,
            np.multiply(np.subtract(k_N,k_G),np.arange(NoPt).reshape(NoPt,1))/NoPt
            )
        k_NP = np.add(
            k_N,
            np.multiply(np.subtract(k_P,k_N),np.arange(NoPt).reshape(NoPt,1))/NoPt
            )
        k = np.concatenate((k_PG,k_GN,k_NP),axis=0)
    elif UnitCellType == 'FCC':
        k_G = [0,0,0]
        k_X = [0,2*math.pi/a,0]
        k_L = [math.pi/a,math.pi/a,math.pi/a]
        k_LG = np.add(
            k_L,
            np.multiply(np.subtract(k_G,k_L),np.arange(NoPt).reshape(NoPt,1))/NoPt
            )
        k_GX = np.add(
            k_G,
            np.multiply(np.subtract(k_X,k_G),np.arange(NoPt).reshape(NoPt,1))/NoPt
            )
        k_XL = np.add(
            k_X,
            np.multiply(np.subtract(k_L,k_X),np.arange(NoPt).reshape(NoPt,1))/NoPt
            )
        k = np.concatenate((k_LG,k_GX,k_XL),axis=0)

    return k