import random,functools
def primo(a,n):
    primos=[]
    cont=0
    posicao = 0
    for i in range(n):
        cont = 0
        for j in range(1,a[i]+1):
            if a[i]%j == 0:
                cont+=1
        if cont == 2 and a[i] not in primos:
            posicao = i
            primos.append(tuple((a[i],posicao)))
    return primos

n = int(input("Informe o tamanho: "))
a = [random.randint(1,1000) for i in range (n)]
b = [1,2,3,4,5,6,7,8,9,10]
print(a)
print("(número,posição)",primo(a,n))

#como reescrever esse teste usando list comprehension
