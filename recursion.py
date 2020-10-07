def Sm_Recursion(n):
    if n == 1:
        return n
    else:
        return n+(n-1)
m = int(input("Digite un numero: "))
for i in range(1,m+1):
    print(Sm_Recursion(i))


def Ft_Recursion(n):
    if n == 1:
        return n
    else:
        return n*(n-1)
m = int(input("Digite un numero: "))
for i in range(1,m+1):
    print (Ft_Recursion(i))

def Ec_Recursion(x,y):
    if y == 0:
        return 0
    else:
        return (y, x%y)
m = int(input("Digite un numero: "))
n = int(input("Digite un numero: "))
print (Ec_Recursion(m,n))
