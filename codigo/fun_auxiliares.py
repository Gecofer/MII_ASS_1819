# FUNCIONES AUXILIARES PARA LA P3 #

import random

# Función que calcula el mcd(a,b)
# --------------------------------------------------------------------------------------------
def mcd (a, b):
    
    if a % b == 0:
        return b
    
    return mcd(b, a%b)


# Función que implementa el Algoritmo Extendido de Euclides
# --------------------------------------------------------------------------------------------
def alg_euclides(a, b):
    
    euclides = [] # Nos creamos una lista que devolverá los valores de la ecuación
    
    # Si el valor es negativo de a
    if a < 0:
        a = -(a) # Convierto 'a' en positivo
    
    # Si el valor es negativo de a
    if b < 0:
        b = -(b) # Convierto 'b' en positivo
    
    # Si a = 0 y b = 0 hemos terminado y se devuelve "Error"
    if a == 0 and b == 0:
        print("Error, los dos números introducidos son cero.")
    
    # Si a = 0 hemos terminado y se devuelve 0
    if a == 0:
        d = 0
        u = 0
        v = 0
    
    # Si b = 0 hemos terminado y se devuelve d = a, u = 1, v = 0
    if b == 0:
        d = a
        u = 1
        v = 0

    # En caso contrario donde a y b sean positivos
    else:
        
        # Comprobamos si a < b, en caso afirmativo cambiamos el orden de los valores dejando a > b
        if a < b:
            tmp = a
            a = b
            b = tmp
    
        # Guardamos el valor de la entrada, para no perderlos
        a0 = a
        b0 = b

        # Inicializamos las variables a manejar
        u0 = 1
        u1 = 0
        v0 = 0
        v1 = 1

        # Mientras b > 0
        while b > 0:
            
            # q = a div b
            q = a // b
            
            # (a, b) = (b, a-q*b)
            r = a - q*b
            a = b
            b = r
            
            # (u0, u1) = (u1, u0-q*u1)
            u = u0 - q*u1
            u0 = u1
            u1 = u
            
            # (v0, v1) = (v1, v0-q*v1)
            v = v0 - q*v1
            v0 = v1
            v1 = v

        # Guardamos el valor que nos interesa
        d = a
        u = u0
        v = v0

    # Añadimos a la lista los valores para la ecuación
    euclides.append(a0)
    euclides.append(u)
    euclides.append(b0)
    euclides.append(v)
    euclides.append(d)

    # Devolvemos la lista
    return euclides


# Función que implementa el Algoritmo Extendido de Euclides (Versión 2)
# --------------------------------------------------------------------------------------------
def alg_euclides_v2(a,b):
    
    r = [a,b]
    s = [1,0]
    t = [0,1]
    i = 1
    q = [[]]
    
    while (r[i] != 0):
        q = q + [r[i-1] // r[i]]
        r = r + [r[i-1] % r[i]]
        s = s + [s[i-1] - q[i]*s[i]]
        t = t + [t[i-1] - q[i]*t[i]]
        i = i+1
    
    return (r[i-1], s[i-1], t[i-1])


# Función que calcula el inverso de dos números que son primos relativos
# --------------------------------------------------------------------------------------------
def alg_inverso(a, b):
    
    # Calculamos el Algoritmo Extendido de Euclides para a y b
    euclides = alg_euclides(a, b)
    
    # Si el mcd es distinto de 1, no tiene inverso
    if euclides[4] != 1:
        print("\nNo existe inverso para {0}^(-1) en Z({1})".format(a,b))
    
    # Si el mcd es igual a 1, si tiene inverso
    if euclides[4] == 1:
        
        # a(u) * b(v) = d
        # Como [a*u (mod a)] = 0. Nos quedamos con b*v siendo el v el inverso de a
        
        # Si el inverso es positivo, es decir, v, lo dejo tal cual
        if (euclides[3] > 0) :
            return euclides[3] % b
    
        # Si el inverso es negativo, le cambio el signo en módulo 'a'
        elif (euclides[3] < 0):
            
            nuevo = b + euclides[3]
            
            # Mientras el valor siga siendo negativo, le vamos sumando 'a'
            while nuevo < 0:
                nuevo = b + euclides[3]
            
            return nuevo % b


# Algoritmo que calcula el a^k mod n
# --------------------------------------------------------------------------------------------
def alg_potencia(a, k, n):
    
    # Inicializamos b a 1
    b = 1
    
    # Si k = 0, ya hemos terminado y devolvemos 1
    
    # Pero mientras k > 0
    while k > 0:
        
        # Iremos descomponiendo k0 y comprobaremos si su resto es 0 ó 1
        k0 = k % 2
        
        # Si el resto es 1
        if k0 == 1:
            
            # Cambiamos el valor de b
            b = a*b % n
        
        # Como k = k0 ... kr, nos quedamos con el k sin usar
        k = (k-k0) // 2
        
        # Cambiamos el valor de a
        a = (a**2) % n

    # Devolvemos b
    return b


# Algoritmo que calcula el a^k mod n (Versión 2)
# --------------------------------------------------------------------------------------------
def alg_potencia_v2(n):
    pot = 0
    
    while n%2 == 0:
        n = n//2
        pot += 1
    
    return pot


# Algoritmo que calcula la primalidad de un numero
# --------------------------------------------------------------------------------------------
def alg_miller_rabin(p):
    
    # Primero sacamos la primalidad para los números del 1 al 5
    
    # Si el número es 1 o 4, no es primo
    if p == 1 or p == 4:
        return False # No primo
    
    # Si el número es 2, 3, es primo
    if p == 2 or p == 3:
        return True #Primo
    
    # En caso de que el número sea mayor que 5 --> Descompongo en p-1
    p1 = p - 1
    u = 0
    
    # Descompongo p-1 en 2^(u) * s
    while p1%2 == 0:
        p1 = p1 // 2
        u = u + 1

    s = p1

    # Eligo aleatoriamente un número entre 2 y p-2
    a = random.randint(2, p-2)
    
    # Calculo a^(s) -> a = a**s
    a = alg_potencia(a,s,p)
    
    # Y compruebo si es 1 o-1,
    if a == 1 or a == p-1:
        return True # Problamente primo

    # Sino es primo, voy elevando al cuadrado
    for i in range(1, u):
        a = alg_potencia(a, 2, p) # a = (a**2) % p
        
        # Si 'a' es p-1
        if a == p-1:
            return True # Problamente primo
        
        # Si 'a' es 1
        if a == 1:
            return False # Probalmemente no primo

    return False # Probalmemente no primo


# Algoritmo que calcula la primalidad de un numero n veces
# --------------------------------------------------------------------------------------------
def alg_miller_rabin1(p, k):
    return all(alg_miller_rabin(p) for a in range(k))


# Función que calcula si un número es símbolo de Jacobi
# --------------------------------------------------------------------------------------------
def jacobi(a, p):
    
    # Si a es 0 se devuelve 0
    if a == 0:
        return 0
    
    # Si a es 1 se devuelve 1
    if a == 1:
        return 1
    
    # Variable que cuenta el numero de veces que se ha dividido el número
    e = 0
    
    # Vamos diviendiendo 'a' hasta que sea impar
    while a % 2 == 0:
        a /= 2
        e += 1
    
    # Si e % 2 = 1, devuelvo s=1
    if e % 2 == 0:
        s = 1

    else:
        
        # Si p ≡ 1 or 7 (mod 8) devuelvo s=1
        if p%8 == 1 or p%8 == 7:
            s = 1
        
        # Si p ≡ 3 or 5 (mod 8) devuelvo s=-1
        elif p%8==3 or p%8==5:
            s = -1
                
    # Si p ≡ 3 (mod 4) y a ≡ 3 (mod 4) devuelvo s=-s
    if (p%4) == 3 and (a%4) == 3:
        s = -s
    
    # Divido 'p' entre 'a'
    p = p % a
    
    # Si a es 1, devuelvo s
    if a==1:
        return s

    # Sino deevuelvo (s*jacobi1(p,a))
    else:
        return (s*jacobi(p,a))


# Función para calcular la raíz cuadrada de un número
# --------------------------------------------------------------------------------------------
def isqrt(n):
    x = n
    y = (x+1) // 2
    
    while(y < x):
        x = y
        y = (x+n // x) // 2
    
    return x


# Función que calcula el Algoritmo dePaso Enano Paso Gigante
# --------------------------------------------------------------------------------------------
def paso_enano_paso_gigante(a, b, p):
    
    # Nos creamos una lista con todos los posibles a^(cs) --> Esta lista será el paso gigante
    L = []
    
    # Nos creamos una lista con todos los posibles b*a^(r)  --> Esta lista será el paso enano
    l = []
    
    # Obtenemos s = [sqrt(p-1)], con redondeo hacia arriba
    s = isqrt(p-1)+1
    
    # Calculamos los valores que tendrá la lista para el
    # paso gigante que empieza el índice en 1 hasta s+1
    for i in range(1, s+1):
        # Los valores de la lista serán [a^(i*s) % p]
        gigante = alg_potencia(a, i*s, p)
        L.append(gigante)
    
    # Calculamos los valores que tendrá la lista para el
    # paso enano que empieza el índice en 0 hasta s-1
    for i in range(0, s):
        # Los valores de la lista serán [b*a^(i) % p]
        enano = (b*alg_potencia(a, i, p))% p;
        l.append(enano)
    
    # Nos creamos una variable, donde se guardará la posición de ambas listas
    aux_l = 0.0
    aux_L = 0.0
    
    # Recorremos la primera lista y buscamos ese elemento en la siguiente lista
    for x in L:
        
        # Si tienen ambas listas un elemento común
        if x in l:
            
            # Posición donde se encuentra el elemento repetido en la lista L
            aux_L = L.index(x)
            
            # Posición donde se encuentra el elemento repetido en la lista l
            aux_l = l.index(x)
            
            return ((aux_L+1)*s - aux_l)
            # k = c*s - r = (aux_L+1)*s - (aux_l) = (aux_L+1)*s-aux_l) % p)


# Función que calcula el siguiente primo
# --------------------------------------------------------------------------------------------
def NextPrime(p):
    
    if p%2==0:
        p=p+1
    
    while (not alg_miller_rabin(p)):
        p+=2
    
    return p
