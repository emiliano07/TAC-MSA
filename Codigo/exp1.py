import copy as c
import Grasp.greedy as gdy
import Grasp.busquedaLocal as blo

#-------------------------------------------------------------------------------------------------

A = "A"
C = "C"
G = "G"
T = "T"
_ = "_"

S0 = [ [C,T,A,G,C,G,A,C,T,C,C,A] , [G,A,A,C,G,G,A,G,T,C,T,C] , [G,A,A,C,C,G,A,G,C,C,T,C] ]

S1 = [ [C,C,G,C,A,C,C,A,T,A] , [G,G,A,A,T,C,C,A,C,C] , [G,G,C,A,C,C,A,A,T,C] , [G,G,A,G,C,A,T,C,C,A] ]

S2 = [ [G,C,A,C,C,T,A,T,T,A,C,C,T,G,C,A,C,C,T,A,T,T,A,C,C,T] , [G,T,G,G,C,C,T,A,T,T,A,G,A,C,C,C,T,A,G,G,G,G,T,C,A,A] , [G,T,G,G,C,C,T,A,T,T,A,G,A,C,C,C,G,C,A,C,C,T,A,T,T,A] ]

S3 = [ [A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T,G,G,C,A,C] , [G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G,T,G,G,A] , [G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C] , [G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C] ]

S4 = [ [A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,G,G,T,C,A,C,C,A,A,A,T,G,G,C,A,C] , [G,T,G,G,T,C,A,C,C,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G,T,G,G,A] , [G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,G,G,T,C,A,C,C,C,A,G,C,G,G,C] , [G,T,C,G,C,G,G,A,G,A,A,G,A,C,G,G,T,C,A,C,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C] ]

#-------------------------------------------------------------------------------------------------

def graspParaAnalisis(limiteIteracion, secuencias):
    iteracion = 0
    mejorValor = -999
    res = gdy.greedy(secuencias)
    while(iteracion < limiteIteracion):
        iteracion += 1
        print("Iteracion N° " + str(iteracion))       
        g = gdy.greedy(secuencias)
        bl = blo.busquedaLocal(g)
        if(mejorValor < bl["SCORE"]):
            mejorValor = c.deepcopy(bl["SCORE"])
            res = bl
        print("Nuevo Score:  " + str(bl["SCORE"]))
        print("Mejor Score:  " + str(c.deepcopy(mejorValor)))
        print("---------------------")
    return res

def compararScore(secuencia, iteraciones):
    print("------------------------------------------------------") 
    print("Secuencias Iniciales:")
    for i in range(0,len(secuencia)):
        print(' '.join(map(str, secuencia[i])))
    print("---------------------")
    graspAux = graspParaAnalisis(iteraciones,secuencia)
    alineamientoAux = graspAux["PROFILE"]["SECUENCIAS"]
    print("Alineamiento Final:")
    for i in range(0,len(alineamientoAux)):
        print(' '.join(map(str, alineamientoAux[i])))
    print("Score Final = " + str(graspAux["SCORE"]))
    return graspAux

#-------------------------------------------------------------------------------------------------

print("------------------------------------------------------")
print("------------------------------------------------------")
print("Experimento N° 1")
print("------------------------------------------------------")
print("------------------------------------------------------")
print("Secuencias Iniciales:")
print("------------------------------------------------------")
secuencias = [S0,S1,S2,S3,S4]
escenario = 1
for sec in range(0,len(secuencias)):
    print("Escenario N° " + str(escenario))
    for i in range(0,len(secuencias[sec])):
        print(' '.join(map(str, secuencias[sec][i])))
    escenario += 1
    print("------------------------------------------------------")
print("------------------------------------------------------")
print("Iteraciones:")
print("------------------------------------------------------")
resultados = []
escenario = 1
for sec in range(0,len(secuencias)):
    print("Escenario N° " + str(escenario))
    resultados.append(compararScore(secuencias[sec],30))
    escenario += 1
    print("------------------------------------------------------")
print("------------------------------------------------------")
print("Alineamiento Final:")
print("------------------------------------------------------")
escenario = 1
for sec in range(0,len(secuencias)):
    print("Escenario N° " + str(escenario))
    for i in range(0,len(resultados[sec]["PROFILE"]["SECUENCIAS"])):
        print(' '.join(map(str, resultados[sec]["PROFILE"]["SECUENCIAS"][i])))
    print("Score Final = " + str(resultados[sec]["SCORE"]))
    escenario += 1
    print("------------------------------------------------------")

