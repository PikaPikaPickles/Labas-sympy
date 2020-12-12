from sympy import *
MyMat = zeros(9, 9)
y, u, p = symbols("y u p")
MyMat[0, 3] = -(1/p)
MyMat[1, 4] = -(1/p)
MyMat[2, 5] = -(1/p)
MyMat[3, 0] = -(y+2*u)
MyMat[4, 1] = -u
MyMat[5, 2] = -u
MyMat[6, 0] = -y
MyMat[8, 0] = -y
print(MyMat.eigenvals())