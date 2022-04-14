# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from k_path import *
from nearest_neighbor import *

e_s = 0
V_ssd = -0.2 # t_ss(a)
a = 1
UnitCellType = 'FCC'  # SC, BCC, FCC

k = k_path(UnitCellType,a)   #(k_path,k_xyz)

L = nearest_neighbor(UnitCellType,a)     #(a_i,k_xyz)

# (a_i,k_path)
tss = V_ssd
E = e_s + tss * np.sum(np.exp(np.inner(L,k)*1j).real,axis=0)

#E = np.concatenate((E_XG,E_GM),axis=0)
plt.plot(np.arange(np.size(k,0)).reshape(np.size(k,0),1),E)
