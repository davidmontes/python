# -*- coding: utf-8 -*-
import math


# ejercio 1 
def median(valorX, valorY, valorZ):
        media = (float(valorX) + float(valorY) +float(valorZ))/3
        print "La media es:", media
#------------------------------------------------------------------
        
# ejercicio 2
def vol_Esf(radio):
        vol = (1.33 * 3.1416) * (float(radio)**3)
        print "El volumen es:", vol

#-------------------------------------------------------------------
        
# ejercicio 3
def impar_N(impar):
        while impar <= 32: 
                 print "Num_Impar:", str(impar) 
                 impar += 2
#-------------------------------------------------------------------

# ejercicio 4
def mayor_N(x, y, z):
        if x >= y and x >= z:
                print "NMayor", x
        elif y >= x and y >= z:
                print "NMayor", y
        elif z >= x and z >= y:
                print "NMayor", z
#---------------------------------------------------------------------
                
# ejercicio 5
def rotar(lista):
        cont=1
       while cont<len(lista):
                lista.append(lista[0])
                lista.remove(lista[0])
                cont +=1
                print lista
rotar(input('vector'))

#-----------------------------------------------------------------


# ejercicio 6

def intervaloSuma(x):      
        vacio=[(conta**3) for conta in range(1,x+1)]        
        print vacio
        return sum(vacio)
#-----------------------------------------------------------------


# ejercicio 7

def intervaloMayor(x):
        #for conta in range(1,x+1):
            #   if (conta**2)>100:
            #       return [(conta**2) for conta in range(1,x+1)]
        vacio=[(conta**2) for conta in range(1,x+1)]        
        num=1
        while num<len(vacio):
                if vacio[num]>100:
                        print vacio[num]
                num+=1
#-----------------------------------------------------------------

# ejercicio 8

def intervaloN (x):
        cont=1
        while cont<=x:
                if cont>=20 and cont<=60:
                        print cont
                cont+=1
#-----------------------------------------------------------------

# ejercicio 9

def hipoT (x, y):
        return math.sqrt(x**2 + y**2)

#----------------------------------------------------------------


# ejercicio 10







