#!/usr/bin/env python
# coding: utf-8

# # Implementación de la Firma Digital
# 
# Se va implementar un sistema de firma digital y verificación de la firma con RSA. Para ello se deben de realizar tres tareas: **generación de claves**, **generación de firma** y **verificación de firma**.

# ## 1. Generación de claves

# Para la **generación de la clave**, nos basamos en la función que implementa un $RSA$.
# 
# 1. Para elegir la pareja de claves, lo primero que necesitamos es elegir dos primos grandes $p$ y $q$, y calcular su producto $n = p \cdot q$.
# 2. Ahora se elige un entero $e$ tal que $mcd(e,\phi(n)) = 1$. Recordemos que $\phi(n) = (p-1)\cdot(q-1)$. Ambos valores, $(n, e)$ constituyen la clave pública del criptosistema. El número $n$ se conoce como módulo del Criptosistema.
# 3. La clave privada es un entero $d$ tal que $d \cdot e = 1 \pmod {\phi(n)}$.
# 
# #### Generación de claves RSA
# 
# Dichas claves, serán guardadas en un fichero.
#     
# - **Entrada**: 
#     - o _p,q_ como dos primos grandes 
#     - o que se generen ambos primos dentro de la función de manera aleatoria
#     
# - **Salida**:
#     - _e,n_: clave pública
#     - _d_: clave privada

# In[1]:


import fun_auxiliares as aux

# Función que calcula el siguiente primo
# --------------------------------------------------------------------------------------------
def NextPrime(p):
    
    if p%2==0:
        p=p+1
    
    while (not aux.alg_miller_rabin(p)):
        p+=2
    
    return p


# In[2]:


import random
import fun_auxiliares as aux

# Método para generar una clave
# --------------------------------------------------------------------------------------------
def generacion_claves():

    # Por seguridad es conveniente elegir dos números de manera aleatoria
    p = random.randint(1, 1000000000000000)
    q = random.randint(1, 1000000000000000)
    
    # Si p no es primo, forzamos a que sea
    p = NextPrime(p)
    
    # Si q no es primo, forzamos a que sea
    q = NextPrime(q)
    
    # Realizamos su producto
    n = p*q
    
    # Calculamos phi
    phi = (p-1)*(q-1)
    
    e = 2
    # Elegimos un número 'e' que sea primo relativo con phi_n, sino aumentamos uno 'e'
    while(aux.alg_euclides_v2(phi,e)[0] != 1):
        e = e +1
    
    # Para hallar la clave privada resolvemos la congruencia e·d = 1 (mod phi_n)
    # es decir, calculamos el inverso de 'e' en Z(phi_n)
    d = aux.alg_inverso(e,phi)
    
    # Abrimos los ficheros donde se guardarán las claves (debe tener permiso de escritura)
    try:
        f_pub = open("clave_publica", "w")
        f_priv = open("clave_privada", "w")
    except:
        print("Error abriendo los ficheros de las claves.")
        
    # Escribimos en un fichero la clave publica y privada, separando e y d de n con un espacio
    # Clave Pública
    f_pub.write(str(e)+" ")
    f_pub.write(str(n))
    # Clave Privada
    f_priv.write(str(d)+" ")
    f_priv.write(str(n))
    
    # Devolvemos las claves
    return e, n, d


# In[3]:


# Para comprobar: e,n (clave publica) y d (clave privada)
e, n, d = generacion_claves()
print(e, n, d)


# ## 2. Generación de firma

# Para la **generación de la firma**, se le introducirá un mensaje a cifrar (fichero) y el fichero con la clave (privada), y deberá generar una firma, que se guardará en un fichero de texto.
# 
# Puesto que lo que realmente se firma no es el mensaje, sino un resumen del mensaje, hay que generar un resumen de dicho mensaje. Para esto emplearemos la función SHA1 (se pueden añadir otras funciones resumen). 
# 
# _Para la función SHA1_, usaremos la librería de Python **hashlib**, que ya implementa esa función.
# 
# #### Generación de firma RSA  
# 
# Como podemos ver en los apuntes, para generar una firma, solo nos bastaría hacer $fir(r) = r^d \pmod n$. Por tanto, el mensaje firmado sería el par $(r, fir(r))$.
#     
# - **Entrada**:
#     - _mensaje_: nombre del fichero del mensaje a firmar en string
#     - _clave-privada_: nombre del fichero de la clave privada en string (contiene d y n)
#         
# - **Salida**:
#     - _f_: firma del resumen del mensaje

# In[4]:


import hashlib 
import fun_auxiliares as aux

# Método para generar la firma
# --------------------------------------------------------------------------------------------
def generacion_firma(mensaje, clave_privada):

    # Abrimos el fichero de mensaje
    try:
        myfile = open(mensaje, encoding='utf-8')
    except:
        print("Error abriendo el fichero del mensaje.")
    
    # Lo guardamos en una variable 
    m = myfile.read()  
    m = m.encode("utf-8")

    # Calculamos un resumen del mensaje
    r = hashlib.sha1(m).hexdigest()
    
    # Como la salida de 'r' es en hexadecimal,
    # la convertimos a entero base 10 para poder operar con el resumen
    r = int("0x"+r, 0)
    
    # Leemos la clave del fichero
    try:
        f_priv = open("clave_privada")
    except:
        print("Error abriendo el fichero de la clave privada.")
        
    clave = f_priv.read().split(" ")
    d = int(clave[0])
    n = int(clave[1])
    
    # Generamos la firma (firma del resumen)
    f = aux.alg_potencia(r,d,n)
    
    try:
        f_firma = open("firma","w")
    except:
        print("Error abriendo el fichero firma.")
        
    # Escribios la firma en el archivo    
    f_firma.write(str(f))
    
    # Devolvemos la firma
    return f


# In[5]:


# Para comprobar

# Nombre del fichero de la clave privada
clave_privada = "clave_privada"

# Nombre del fichero del mensaje
mensaje = "mensaje"

firma = generacion_firma(mensaje, clave_privada)
print(firma)


# ## 3. Verificación de la firma

# Para la **verificación de la firma**, se introduce el mensaje (fichero) que se ha firmado, un fichero con la firma (con el mismo formato que el generado en el apartado anterior) y un fichero con la clave (pública). Deberá responder si la firma es o no válida.
# 
# #### Verificación de firma RSA  
# 
# Como podemos ver en los apuntes, para comprobar si la firma es válida, habría que hacer si $r = fir(r)^e \pmod n$.
# 
# - **Entrada**:
#     - _clave-publica_: nombre del fichero de la clave pública en string (e y n)
#     - _mensaje_: nombre del fichero del mensaje a verificar en string
#     - _firma_: nombre del fichero de firma en string
#     
# - **Salida**:
#     - _True_: si la firma es correcta
#     - _False_: si la firma no es correcta

# In[6]:


import hashlib 
import fun_auxiliares as aux

# Método para verificar la firma
# --------------------------------------------------------------------------------------------
def verificacion_firma(clave_publica, mensaje, firma):
   
    # Abrimos el fichero de mensaje
    try:
        myfile = open(mensaje, encoding='utf-8')
    except:
        print("Error abriendo el fichero del mensaje.")
    
    # Lo guardamos en una variable como string
    m = myfile.read()
    m = m.encode("utf-8")
    
    # Calculamos un resumen del mensaje
    r = hashlib.sha1(m).hexdigest()
    
    # Como la salida de 'r' es en hexadecimal,
    # la convertimos a entero base 10 para poder operar con el resumen
    r = int("0x"+r,0)
    
    # Leemos la clave del fichero
    try:
        f_pub = open("clave_publica")
    except:
        print("Error abriendo el fichero de la clave pública.")
    
    clave = f_pub.read().split(" ")
    e = int(clave[0])
    n = int(clave[1])
    
    # Leemos el fichero con la firma
    try:
        f_firma = open("firma")
    except:
        print("Error abriendo el fichero de la firma.")
    
    f = int(f_firma.read())
    
    # Verificamos la firma
    v = aux.alg_potencia(f,e,n)

    # Si la verificacion coincide con la función resumen es válidad
    if(v%n == r%n): 
        return True # Firma válida
    else:
        return False # Firma no válidad


# In[7]:


# Nombre del fichero de la clave privada
clave_privada = "clave_privada"

# Nombre del fichero de la clave pública
clave_publica = "clave_publica"

# Nombre del fichero del mensaje
mensaje = "mensaje"

# Nombre del fichero de la firma
firma = "firma" 

# Hacemos la Firma RSA
generacion_claves()
generacion_firma(mensaje, clave_privada)
verificacion_firma(clave_publica, mensaje, firma)


# Para comprobar que la verificación funciona, si editamos el fichero de firma y realizamos de nuevo la verificación, obtenemos un valor False.
