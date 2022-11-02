#Les boucles For
n1,n2=int(input("valeur1 ")),int(input("valeur2 "))
for v in range(n1+1,n2):
    print(v)
for v in range(n1-1,n2,-1):
    print(v) 
if n1==n2 :
    print("valeurs égales")