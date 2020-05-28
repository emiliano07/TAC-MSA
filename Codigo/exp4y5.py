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

# 4 SECUENCIAS DE 4 NUCLEOTIDOS
S0 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G]]
# 5 SECUENCIAS DE 4 NUCLEOTIDOS
S1 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G]]
# 6 SECUENCIAS DE 4 NUCLEOTIDOS
S2 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[G,T,C,G]]
# 7 SECUENCIAS DE 4 NUCLEOTIDOS
S3 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[G,T,C,G],[A,T,G,G]]
# 8 SECUENCIAS DE 4 NUCLEOTIDOS
S4 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G]]
# 9 SECUENCIAS DE 4 NUCLEOTIDOS
S5 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G],[A,T,G,G]]

#SOLO PARA GRASP
# 10 SECUENCIAS DE 4 NUCLEOTIDOS
S6 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G],[A,T,G,G],[G,T,C,G]]
# 11 SECUENCIAS DE 4 NUCLEOTIDOS
S7 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G],[A,T,G,G],[G,T,C,G],[A,T,G,G]]
# 12 SECUENCIAS DE 4 NUCLEOTIDOS
S8 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G],[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G]]
# 13 SECUENCIAS DE 4 NUCLEOTIDOS
S9 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G],[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G]]
# 14 SECUENCIAS DE 4 NUCLEOTIDOS
S10 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G],[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G]]
# 15 SECUENCIAS DE 4 NUCLEOTIDOS
S11 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G],[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G]]
# 16 SECUENCIAS DE 4 NUCLEOTIDOS
S12 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G],[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G]]
# 17 SECUENCIAS DE 4 NUCLEOTIDOS
S13 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G],[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G],[A,T,G,G]]
# 18 SECUENCIAS DE 4 NUCLEOTIDOS
S14 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G],[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G],[A,T,G,G],[G,T,C,G]]
# 19 SECUENCIAS DE 4 NUCLEOTIDOS
S15 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G],[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G],[A,T,G,G],[G,T,C,G],[A,T,G,G]]
# 20 SECUENCIAS DE 4 NUCLEOTIDOS
S16 = [[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G],[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[A,T,C,G],[G,T,G,G],[A,T,G,G],[G,T,C,G],[A,T,G,G],[A,T,C,G]]

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
  print("Grasp")
  promTiempo = 0
  for x in range(ejecuciones):
      ti = default_timer() 
      grAux = gr.grasp(30,secAux)
      tf = default_timer()
      tiempo = tf - ti
      promTiempo += tiempo
      secFinal = grAux["PROFILE"]["SECUENCIAS"]
      tiempo = round(tiempo,2)
      print("Tiempo " + str(x+1) + " = " + str(tiempo) + " segundos")
      scoreGR = calcularScore(secFinal)
  promTiempo = promTiempo / ejecuciones
  promTiempo = round(promTiempo,2)
  print("Tiempo promedio = " + str(promTiempo) + " segundos")
  return (grAux,scoreGR)

def executePD(secAux,nExe):
  ejecuciones = nExe
  print("---------------------")
  print("Programacion Dianmica")
  promTiempo = 0
  for x in range(ejecuciones):
    ti = default_timer() 
    pdAux = pd.alineamiento(secAux)
    tf = default_timer()
    tiempo = tf - ti
    promTiempo += tiempo
    tiempo = round(tiempo,2)
    print("Tiempo " + str(x+1) + " = " + str(tiempo) + " segundos")
    scorePD = calcularScore(pdAux)
  promTiempo = promTiempo / ejecuciones
  promTiempo = round(promTiempo,2)
  print("Tiempo promedio = " + str(promTiempo) + " segundos")
  return (pdAux,scorePD)

#-------------------------------------------------------------------------------------------------

print("------------------------------------------------------")
print("------------------------------------------------------")
print("Experimento N° 4 Y 5")
print("------------------------------------------------------")
print("------------------------------------------------------")
print("Secuencias Iniciales:")
print("------------------------------------------------------")
secuencias = [S0,S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S16]
secuencias2 = [S0,S1,S2,S3,S4,S5]
secuenciasGRASP = [S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S16]
escenario = 1
for sec in range(0,len(secuencias)):
    print("Escenario N° " + str(escenario))
    for i in range(0,len(secuencias[sec])):
        print(' '.join(map(str, secuencias[sec][i])))
    escenario += 1
    print("---------------------")
print("------------------------------------------------------")
print("Ejecuciones:")
print("------------------------------------------------------")
resultadosPD = []
resultadosGRASP = []
escenario = 1
for sec in range(0,len(secuencias2)):
    print("Escenario N° " + str(escenario))
    resAux = executePD(secuencias2[sec],2)
    resultadosPD.append(resAux)
    print("Score PD = " + str(resAux[1]))
    print("---------------------")
    resAux = executeGrasp(secuencias2[sec],2)
    resultadosGRASP.append(resAux)
    print("Score GRASP = " + str(resAux[1]))
    escenario += 1
    print("---------------------")
    print("---------------------")
for sec in range(0,len(secuenciasGRASP)):
    print("Escenario N° " + str(escenario))
    print("---------------------")
    resAux = executeGrasp(secuenciasGRASP[sec],2)
    resultadosGRASP.append(resAux)
    print("Score GRASP = " + str(resAux[1]))
    escenario += 1
    print("---------------------")
    print("---------------------")
print("------------------------------------------------------")
print("Alineamiento Final:")
print("------------------------------------------------------")
escenario = 1
for sec in range(0,len(secuencias2)):
    print("Escenario N° " + str(escenario))
    print("---------------------")
    print("Programacion Dinamica")
    for i in range(0,len(resultadosPD[sec][0])):
        print(' '.join(map(str, resultadosPD[sec][0][i])))
    print("Score Final PD = " + str(resultadosPD[sec][1]))
    print("---------------------")
    print("Grasp")
    for i in range(0,len(resultadosGRASP[sec][0]["PROFILE"]["SECUENCIAS"])):
        print(' '.join(map(str, resultadosGRASP[sec][0]["PROFILE"]["SECUENCIAS"][i])))
    print("Score Final Grasp = " + str(resultadosGRASP[sec][1]))
    escenario += 1
    print("---------------------")
    print("---------------------")
for sec in range(len(secuencias2),(len(secuencias2) + len(secuenciasGRASP))):
    print("Escenario N° " + str(escenario))
    print("---------------------")
    print("Grasp")
    for i in range(0,len(resultadosGRASP[sec][0]["PROFILE"]["SECUENCIAS"])):
        print(' '.join(map(str, resultadosGRASP[sec][0]["PROFILE"]["SECUENCIAS"][i])))
    print("Score Final Grasp = " + str(resultadosGRASP[sec][1]))
    escenario += 1
    print("---------------------")
    print("---------------------")