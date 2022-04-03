# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math
from k_path import *

e_s = 1
V_ssd = -0.2 # t_ss(a)
a = 1

k = k_path(a)   #(k_path,k_xyz)

# simple cubic　(a_i,k_xyz)
a1 = a* np.array([[1,0,0]])
a2 = a* np.array([[-1,0,0]])
a3 = a* np.array([[0,1,0]])
a4 = a* np.array([[0,-1,0]])
a5 = a* np.array([[0,0,1]])
a6 = a* np.array([[0,0,-1]])

L = np.concatenate((a1,a2,a3,a4,a5,a6),axis=0)

# (a_i,k_path)
#E_XG = e_s + V_ssd * np.sum(np.exp(np.inner(L,k_XG)),axis=0)
#E_GM = e_s + V_ssd * np.sum(np.exp(np.inner(L,k_GM)),axis=0)
E = e_s + V_ssd * np.sum(np.exp(np.inner(L,k)),axis=0)

#E = np.concatenate((E_XG,E_GM),axis=0)
plt.plot(np.arange(np.size(k,0)).reshape(np.size(k,0),1),E)
