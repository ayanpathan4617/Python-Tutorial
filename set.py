#Set Operations
# 1) Union

A = {1,2,3}
B = {3,4,6,2,8,7}
C = A.union(B)
print(C)

# 2) Update

D = {1,2,3}
D.update([4,5])
print(D)

# 3) Intersection

E = {1,2,3,4,5}
F = {2,3,8,9,7}
G = E.intersection(F)
print(G)

# 4) Symmetric

H = {1,2,3,4}
I = {1,2}
J = H.symmetric_difference(I)
print(J)

# 5) Difference
K = {1,2,3}
L = {2,3,4}
M = K.difference(L)
print(M)


##  METHODS

# 1) issubset()

N = {1,2,3,4}
O = {1,2,3,4,5}
P = N.issubset(O)
print(P)

# 2) issuperset()
Q = {1,2,3,4}
R = {1,2,3}
S = O.issuperset(R)
print(S)

# 3) isdisjoint()
T = {1,2,3,4}
U = {5,6,7,8,9}
V = T.isdisjoint(U)
print(V)

# 4) Add

ayan = {1,2,3,4,5,6}
ay = ayan.add(15)
print(ayan)

# 5) UPDATE

XYZ = {1,23,4,5,6,7}
P = XYZ.update([22,11,33,44,55,66])
print(XYZ)

# 6) COPY
# 7) CLEAR
# 8) POP