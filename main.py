import math

#a= int (input ("entrez le nombre : a="))
#if a>0 :
    #s= math.sqrt(a)
    #print(s)
#else :
    #print(erreur)



#a= int(input("entrer le nombre: a="))
#b= int(input("entrer le nombre: b="))
#if a!=b:
 #   a,b=b,a
 #   print("a=",a)
 #   print("b=",b)
#else:
   # print("a==b")
   #print("le nombre min est : ",min(a,b))
#else:
    #print("a==b")

import math



##a= int(input("entrer le nombre: a="))
#b= int(input("entrer le nombre: b="))
#c= int(input("entrer le nombre: c="))
#if a!=b and b!=c and a!=c :
   # minimum = min(a,b,c)
    #print("le nombre min est :", minimum)
#elif a==b and b!=c and a!=c or b==c and a!=b and a!=c or a==c and a!=b and b!=c :
    #minimum = min(a, b, c)
    #print("le nombre min est :", minimum)
#else:
    #print("equal")##

#import random , math
#x=int(input("donner x:"))
#y=int(input("donner y:"))
#op=input("donner un operateur (+ou-):")
#if op=='+':
   # r=x+y
    #print(f"{x} {op} {y} = {r}")
#else : op == '-':
    #r=x-y
#else:
    #r = None
#if r is not None :
    #print(f"{x} {op} {y} = {r}")

#x=int(input("donner x:"))
#y=int(input("donner y:"))
#p=x*y
#if x>=0 and y>=0 or x<=0 and y<=0:
   # print("p est positif")
#else:
#    print("p est negatif")

#a=float(input("donner a:"))
#b=float(input("donner b:"))
#*x+b==0if a!=0:
 #  x=-b/a
 #   print("x =",x)
#else:
 #   print("erreur")


#import math

#a = float(input("Donner a : "))
#b = float(input("Donner b : "))
#c = float(input("Donner c : "))

#if a != 0:
#    delta = b**2 - 4*a*c
#    print("Delta =", delta)

#    if delta > 0:
#        x1 = (-b - math.sqrt(delta)) / (2*a)
#        x2 = (-b + math.sqrt(delta)) / (2*a)
#        print("Deux solutions réelles : x1 =", x1, "et x2 =", x2)
#    elif delta == 0:
#        x = -b / (2*a)
#        print("Une solution réelle double : x =", x)
#    else:
#        print("Pas de solution réelle (delta < 0)")
#else:
    # Cas particulier : ce n'est plus une équation du 2e degré
#    if b != 0:
#       x = -c / b
#        print("Équation du 1er degré : x =", x)
#    else:
#        if c == 0:
#            print("Infinité de solutions (0 = 0)")
#        else:
#            print("Aucune solution (c ≠ 0)")


#n = int(input("Entrer le nombre n : "))
#fact = 1

#if n < 0:
#    print("La factorielle n'est pas définie pour les nombres négatifs.")
#else:
#    for i in range(1, n + 1):
#        fact *= i
#    print(f"La factorielle de {n} est : {fact}")


import math

# Lire les entiers p et n
p = int(input("Entrer la valeur de p : "))
n = int(input("Entrer la valeur de n : "))

# Vérifier que p <= n et que les valeurs sont valides
if p < 0 or n < 0:
    print("Erreur : p et n doivent être positifs.")
elif p > n:
    print("Erreur : p ne peut pas être supérieur à n.")
else:
    # Calcul de la combinaison : C(n, p) = n! / (p! * (n - p)!)
    combinaison = math.factorial(n) // (math.factorial(p) * math.factorial(n - p))
    print(f"Le nombre de combinaisons de {p} parmi {n} est : C({n}, {p}) = {combinaison}")


#n = int(input("Entrer la valeur de n : "))

#if n>0:
#    i=math.factorial(n)
 #   print("n! =",i)
#else:
#    print("erreur")


#n = int(input("Entrer un entier n : "))

#if n > 0:
#    s = 0
#    for k in range(1, n + 1):
#        s += 1 / k
    print(f"La somme harmonique H({n}) = {s}")
else:
    print("Erreur : n doit être un entier positif (> 0).")

