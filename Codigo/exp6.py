import Grasp.grasp as gr
import Programacion_Dinamica.programacionDinamica as pd
from timeit import default_timer
import numpy as np
import copy as c

#-------------------------------------------------------------------------------------------------

A = "A"
C = "C"
G = "G"
T = "T"
_ = "_"

S0 = [[A,T,A,T,C,A,G,G],[G,T,A,T,C,A,C,G],[G,T,A,T,C,A,G,G],[A,T,A,T,C,A,C,G]]
S1 = [ [C,A,A,G,C,G,A,G,T,A,T,G,G,A,C,C,C],[G,A,A,C,G,G,A,G,T,A,T,G,G,A,C,T,C],[G,A,A,C,C,G,A,G,T,A,T,G,G,A,C,T,C] ]

#-------------------------------------------------------------------------------------------------

def calcularScore(secuencias):
  score = 0
  for u in range(0,len(secuencias)):
    for v in range(u+1,len(secuencias)):
      score += scorePar(secuencias[u],secuencias[v])
  return score

def scorePar(u,v):
  score = 0
  for i in range(0,len(u)):
    score += costoComparacion(u[i],v[i])
  return score

def costoComparacion(u,v):
  match = 3
  missmatch = -1
  gap = 1
  if (u == v):
    if(u == "_"):
      return 0
    return match
  else:
    if(u == "_" or v == "_"):
      return gap
    return missmatch

def executeGrasp(secAux,nExe):
  ejecuciones = nExe
  for x in range(ejecuciones):
      ti = default_timer() 
      grAux = gr.grasp(30,secAux)
      tf = default_timer()
      tiempo = tf - ti
      secFinal = grAux["PROFILE"]["SECUENCIAS"]
      tiempo = round(tiempo,2)
      scoreGR = calcularScore(secFinal)
  return (grAux,scoreGR)

def executePD(secAux,nExe):
  ejecuciones = nExe
  for x in range(ejecuciones):
    ti = default_timer() 
    pdAux = pd.alineamiento(secAux)
    tf = default_timer()
    tiempo = tf - ti
    tiempo = round(tiempo,2)
    scorePD = calcularScore(pdAux)
  return (pdAux,scorePD)

#-------------------------------------------------------------------------------------------------

print("------------------------------------------------------")
print("------------------------------------------------------")
print("Experimento N° 6")
print("------------------------------------------------------")
print("------------------------------------------------------")
print("Secuencias Iniciales:")
print("------------------------------------------------------")
secuencias = [S0,S1]
escenario = 1
for sec in range(0,len(secuencias)):
    print("Escenario N° " + str(escenario))
    for i in range(0,len(secuencias[sec])):
        print(' '.join(map(str, secuencias[sec][i])))
    escenario += 1
    print("---------------------")
resultadosPD = []
resultadosGRASP = []
for sec in range(0,len(secuencias)):
    resultadosPD.append(executePD(secuencias[sec],1))
    resultadosGRASP.append(executeGrasp(secuencias[sec],1))
print("------------------------------------------------------")
print("Alineamiento Final:")
print("------------------------------------------------------")
escenario = 1
for sec in range(0,len(secuencias)):
    print("Escenario N° " + str(escenario))
    print("---------------------")
    print("Programacion Dinamica")
    print("---------------------")
    for i in range(0,len(resultadosPD[sec][0])):
        print(' '.join(map(str, resultadosPD[sec][0][i])))
    print("---------------------")
    print("Score Final PD = " + str(resultadosPD[sec][1]))
    print("---------------------")
    print("---------------------")
    print("Grasp")
    print("---------------------")
    for i in range(0,len(resultadosGRASP[sec][0]["PROFILE"]["SECUENCIAS"])):
        print(' '.join(map(str, resultadosGRASP[sec][0]["PROFILE"]["SECUENCIAS"][i])))
    print("---------------------")
    print("Score Final Grasp = " + str(resultadosGRASP[sec][1]))
    escenario += 1
    print("---------------------")
    print("---------------------")