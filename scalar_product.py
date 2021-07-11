import math,random,functools
a = [random.randrange(-100,100) for i in range(5)]
b = [random.randrange(-100,100) for i in range(5)]
c = list(map(lambda x,y:x*y,a,b))
d = [a*b for a,b in zip(a,b)]
print(a)
print(b)
print(c)
print(d)
#[a*b for a,b in zip(lista,listb)]
