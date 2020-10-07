def Sm_Trecursion(n):
    if n == 1:
        return n
    else:
        return n+Sm_Trecursion(n-1)
a = int(input("Numero: "))
for i in range (1, a+1):
    print(Sm_Trecursion(i))

def Ft_Trecursion(n):
    if n == 1:
        return n
    else:
        return n*Ft_Trecursion(n-1)
a = int(input("Numero: "))
for i in range (1, a+1):
    print (Ft_Trecursion(i))    

def Ec_Trecursion(x,y):
    if y == 0:
        return x
    else:
        return Ec_Trecursion(y, x%y)
a = int(input("Numero: "))
b = int(input("Numero 2: "))
print (Ec_Trecursion(a,b))
