# -*- coding: utf-8 -*-
"""
This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
import math
# dimensions: (k_xyz,k_path,a_i)

V_ssd = -0.2 # t_ss(a)
a = 1

NoPt = 3    # num of point between k-points
## k-path definition
# X-Γ-M for sc
k_X = [0,math.pi/a,0]
k_G = [0,0,0]
k_M = [math.pi/a,math.pi/a,0]

# dimensions: (k_path,k_xyz,a_i)
k_XG = np.add(
    k_X,
    np.multiply(np.subtract(k_G,k_X),np.arange(NoPt).reshape(NoPt,1))/NoPt
    )

# simple cubic
a1 = a* [[[1,0,0]]]
a2 = a* [[[-1,0,0]]]
a3 = a* [[[0,1,0]]]
a4 = a* [[[0,-1,0]]]
a5 = a* [[[0,0,1]]]
a6 = a* [[[0,0,-1]]]

L = np.concatenate((a1,a2,a3,a4,a5,a6),axis=1)
print(L)

"""
kx = np.linspace(-math.pi, math.pi, 50)
ky = np.linspace(-math.pi, math.pi, 50)
E = 1/2 * k**2

plt.plot(k, E)
plt.show()
"""