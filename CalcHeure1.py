# v1 , ne calcule pas au dessus de 48h, 120m et 120s
# et ne demande pas les jours


print("Veuillez entrer la première durée H,M et S")
h1 = int(input("H = "))
m1 = int(input("M = "))
s1 = int(input("S = "))

print("Veuillez entrer la deuxième durée H,M et S")
h2 = int(input("H = "))
m2 = int(input("M = "))
s2 = int(input("S = "))

H = (h1+h2)
M = (m1+m2)
S = (s1+s2)
J = (0)

if S >= 60:
    S = (S-60)
    M = (M+1)

elif M >= 60:
    M = (M-60)
    H = (H+1)

elif H >= 24:
    H = (H-24)
    J = (J+1)

print(J,'j,', H,'h,',M,'m,',S,'s')
