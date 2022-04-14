# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 23:02:03 2022

@author: User
"""
import numpy as np

def nearest_neighbor(UnitCellType,a):
    # simple cubic　(a_i,k_xyz)
    if UnitCellType == 'SC':
        a1 = a* np.array([[1,0,0]])
        a2 = a* np.array([[-1,0,0]])
        a3 = a* np.array([[0,1,0]])
        a4 = a* np.array([[0,-1,0]])
        a5 = a* np.array([[0,0,1]])
        a6 = a* np.array([[0,0,-1]])
        
        L = np.concatenate((a1,a2,a3,a4,a5,a6),axis=0)
        
    elif UnitCellType == 'BCC':
        a1 = a/2* np.array([[1,1,1]])
        a2 = a/2* np.array([[1,1,-1]])
        a3 = a/2* np.array([[1,-1,1]])
        a4 = a/2* np.array([[-1,1,1]])
        l1 = np.concatenate((a1,a2,a3,a4),axis=0)
        l2 = -1 * l1
        L = np.concatenate((l1,l2),axis=0)
    elif UnitCellType == 'FCC':
        a1 = a/2* np.array([[0,1,1]])
        a2 = a/2* np.array([[1,0,1]])
        a3 = a/2* np.array([[1,1,0]])
        a4 = a/2* np.array([[0,-1,1]])
        a5 = a/2* np.array([[-1,0,1]])
        a6 = a/2* np.array([[-1,1,0]])
        l1 = np.concatenate((a1,a2,a3,a4,a5,a6),axis=0)
        l2 = -1 * l1
        L = np.concatenate((l1,l2),axis=0)
        
    return(L)

if __name__ == "__main__":
    L = nearest_neighbor('BCC',1)

