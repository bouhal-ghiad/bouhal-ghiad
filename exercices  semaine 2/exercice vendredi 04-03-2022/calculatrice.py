# Exercice 1 - Vendredi le 04-03-2022 
# Partie 1 créer une fonction pour calculer les modulos
def mod(n1):
    (x,y)=n1
    return(x%y)
x=9 , 4
print(mod(x))

# Exercice 2 -Partie 1
def Fract(a,b,c,d):
    fract_add=a/b+c/d
    fract_sous=a/b-c/d
    fract_mult=(a/b)*(c/b)
    fract_div=(a/b)/(c/d)
    return (fract_add, fract_sous, fract_mult, fract_div)

a=20
b=2
c=6
d=3

print(Fract(20,2,6,3))

# Exercice 2 -Partie 2
def Fract2(x,y):
    a,b=x
    c,d=y
    fract_add_2=a/b+c/d
    fract_sous_2=a/b-c/d
    fract_mult_2=(a/b)*(c/b)
    fract_div_2=(a/b)/(c/d)
    return (fract_add_2, fract_sous_2, fract_mult_2, fract_div_2)

x=20,2
y=6,3

print(Fract2(x,y)) 