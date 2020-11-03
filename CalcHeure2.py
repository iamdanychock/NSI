# v2

#################################################################
print("Veuillez entrer la première durée J,H,M et S")
j1 = int(input("J = "))
h1 = int(input("H = "))
if h1 >= 24:
    print("Veuillez entrer une valeur inférieure à 24")

m1 = int(input("M = "))
if m1 >= 60:
    print("Veuillez entrer une valeur inférieure à 60")

s1 = int(input("S = "))
if s1 >= 60:
    print("Veuillez entrer une valeur inférieure à 24")
#################################################################
print("Veuillez entrer la deuxième durée H,M et S")
j2 = int(input("J = "))
h2 = int(input("H = "))
if h2 >= 24:
    print("Veuillez entrer une valeur inférieure à 24")

m2 = int(input("M = "))
if m2 >= 60:
    print("Veuillez entrer une valeur inférieure à 60")

s2 = int(input("S = "))
if s2 >= 60:
    print("Veuillez entrer une valeur inférieure à 24")
#################################################################
H = (h1+h2)
M = (m1+m2)
S = (s1+s2)
J = (j1+j2+0)


if S >= 60:
    S = (S-60)
    M = (M+1)

elif M >= 60:
    M = (M-60)
    H = (H+1)

elif H >= 24:
    H = (H-24)
    J = (J+1)
#################################################################
elif S >= 60:
    S = (S-60)
    M = (M+1)

elif M >= 60:
    M = (M-60)
    H = (H+1)

elif H >= 24:
    H = (H-24)
    J = (J+1)


print(J,'j,', H,'h,',M,'m,',S,'s')








         
