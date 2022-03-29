# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
import math

a = 1
a1 = a* [1/2,np.sqrt(3)/2]
a2 = a* [-1/2,np.sqrt(3)/2]
L = [[a1],[np.negative(a1)],[a2],[np.negative(a2)],
     [np.subtract(a1,a2)],[np.subtract(a2,a1)]]
print(L)

"""
kx = np.linspace(-math.pi, math.pi, 50)
ky = np.linspace(-math.pi, math.pi, 50)
E = 1/2 * k**2

plt.plot(k, E)
plt.show()
"""