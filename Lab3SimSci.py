from scipy.integrate import odeint
import numpy as np
from matplotlib import pyplot as plt
import sympy as sp


def dydt(y, t):
    return -2*y


x, y, C = sp.symbols('x y C')
sol = sp.solve(sp.Eq(sp.integrate(1 / y, y), -2*x), y)[0]
e = sp.Eq(sol.evalf(subs={x: 0}) + C, np.sqrt(2))  #c симпаем следует быть аккуратным
C = sp.solve(e, C)[0]
sol += C
fig, ax = plt.subplots(1, 2)
X = np.linspace(start=-10, stop=0, num=int(20 / 0.1))
Y = []
for i in range(len(X)):
    Y.append(sol.evalf(subs={x: X[i]}))
ax[0].plot(X, Y)
ax[0].set_title('SymPy answer')



plt.plot(np.linspace(-10, 0, 200), np.array(odeint(dydt, np.e ** (-2*(-10)), np.linspace(-10, 0, 200))).flatten() + odeint(dydt, np.e ** (-2*(-10)),np.linspace(-10, 0, 200))[len(odeint(dydt, np.e ** (-2*(-10)),np.linspace(-10, 0, 200))) - 1] - np.sqrt(2))
ax[1].set_title('SciPy answer')

for graf in ax:
    graf.set_xlabel('x')
    graf.set_ylabel('y')

plt.show()