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
S0 = [[A,T,C,C],[G,T,G,G],[G,T,C,G],[G,T,C,G]]
# 4 SECUENCIAS DE 5 NUCLEOTIDOS
S1 = [[A,T,C,C,T],[G,T,G,G,C],[G,T,C,G,C],[G,T,C,G,C]]
# 4 SECUENCIAS DE 6 NUCLEOTIDOS
S2 = [[A,T,C,C,T,C],[G,T,G,G,C,G],[G,T,C,G,C,G],[G,T,C,G,C,G]]
# 4 SECUENCIAS DE 7 NUCLEOTIDOS
S3 = [[A,T,C,C,T,C,C],[G,T,G,G,C,G,G],[G,T,C,G,C,G,G],[G,T,C,G,C,G,G]]
# 4 SECUENCIAS DE 8 NUCLEOTIDOS
S4 = [[A,T,C,C,T,C,C,A],[G,T,G,G,C,G,G,A],[G,T,C,G,C,G,G,A],[G,T,C,G,C,G,G,A]]
# 4 SECUENCIAS DE 9 NUCLEOTIDOS
S5 = [[A,T,C,C,T,C,C,A,C],[G,T,G,G,C,G,G,A,G],[G,T,C,G,C,G,G,A,G],[G,T,C,G,C,G,G,A,G]]
# 4 SECUENCIAS DE 10 NUCLEOTIDOS
S6 = [[A,T,C,C,T,C,C,A,C,G],[G,T,G,G,C,G,G,A,G,A],[G,T,C,G,C,G,G,A,G,A],[G,T,C,G,C,G,G,A,G,A]]
# 4 SECUENCIAS DE 11 NUCLEOTIDOS
S7 = [[A,T,C,C,T,C,C,A,C,G,G],[G,T,G,G,C,G,G,A,G,A,A],[G,T,C,G,C,G,G,A,G,A,A],[G,T,C,G,C,G,G,A,G,A,A]]
# 4 SECUENCIAS DE 12 NUCLEOTIDOS
S8 = [[A,T,C,C,T,C,C,A,C,G,G,T],[G,T,G,G,C,G,G,A,G,A,A,G],[G,T,C,G,C,G,G,A,G,A,A,G],[G,T,C,G,C,G,G,A,G,A,A,G]]
# 4 SECUENCIAS DE 13 NUCLEOTIDOS
S9 = [[A,T,C,C,T,C,C,A,C,G,G,T,C],[G,T,G,G,C,G,G,A,G,A,A,G,A],[G,T,C,G,C,G,G,A,G,A,A,G,A],[G,T,C,G,C,G,G,A,G,A,A,G,A]]
# 4 SECUENCIAS DE 14 NUCLEOTIDOS
S10 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A],[G,T,G,G,C,G,G,A,G,A,A,G,A,C],[G,T,C,G,C,G,G,A,G,A,A,G,A,C],[G,T,C,G,C,G,G,A,G,A,A,G,A,C]]
# 4 SECUENCIAS DE 15 NUCLEOTIDOS
S11 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C]]
# 4 SECUENCIAS DE 16 NUCLEOTIDOS
S12 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T]]
# 4 SECUENCIAS DE 17 NUCLEOTIDOS
S13 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T]]
# 4 SECUENCIAS DE 18 NUCLEOTIDOS
S14 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A]]
# 4 SECUENCIAS DE 19 NUCLEOTIDOS
S15 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G]]
# 4 SECUENCIAS DE 20 NUCLEOTIDOS
S16 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G]]
# 4 SECUENCIAS DE 21 NUCLEOTIDOS
S17 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G]]
# 4 SECUENCIAS DE 22 NUCLEOTIDOS
S18 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G]]
# 4 SECUENCIAS DE 23 NUCLEOTIDOS
S19 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C]]
# 4 SECUENCIAS DE 24 NUCLEOTIDOS
S20 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C]]
# 4 SECUENCIAS DE 25 NUCLEOTIDOS
S21 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A]]
# 4 SECUENCIAS DE 26 NUCLEOTIDOS
S22 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T,G],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G]]
# 4 SECUENCIAS DE 27 NUCLEOTIDOS
S23 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T,G,G],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G,T],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C]]
# 4 SECUENCIAS DE 28 NUCLEOTIDOS
S24 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T,G,G,C],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G,T,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G]]
# 4 SECUENCIAS DE 29 NUCLEOTIDOS
S25 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T,G,G,C,A],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G,T,G,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G]]
# 4 SECUENCIAS DE 30 NUCLEOTIDOS
S26 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T,G,G,C,A,C],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G,T,G,G,A],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C]]
# 4 SECUENCIAS DE 31 NUCLEOTIDOS
S27 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T,G,G,C,A,C,A],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G,T,G,G,A,A],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A]]
# 4 SECUENCIAS DE 32 NUCLEOTIDOS
S28 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T,G,G,C,A,C,A,T],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G,T,G,G,A,A,T],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T]]
# 4 SECUENCIAS DE 33 NUCLEOTIDOS
S29 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T,G,G,C,A,C,A,T,C],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G,T,G,G,A,A,T,C],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T,C],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T,C]]
# 4 SECUENCIAS DE 34 NUCLEOTIDOS
S30 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T,G,G,C,A,C,A,T,C,G],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G,T,G,G,A,A,T,C,C],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T,C,C],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T,C,C]]
# 4 SECUENCIAS DE 35 NUCLEOTIDOS
S31 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T,G,G,C,A,C,A,T,C,G,G],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G,T,G,G,A,A,T,C,C,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T,C,C,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T,C,C,G]]
# 4 SECUENCIAS DE 36 NUCLEOTIDOS
S32 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T,G,G,C,A,C,A,T,C,G,G,C],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G,T,G,G,A,A,T,C,C,G,T],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T,C,C,G,T],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T,C,C,G,T]]
# 4 SECUENCIAS DE 37 NUCLEOTIDOS
S33 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T,G,G,C,A,C,A,T,C,G,G,C,G],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G,T,G,G,A,A,T,C,C,G,T,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T,C,C,G,T,G],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T,C,C,G,T,C]]
# 4 SECUENCIAS DE 38 NUCLEOTIDOS
S34 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T,G,G,C,A,C,A,T,C,G,G,C,G,T],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G,T,G,G,A,A,T,C,C,G,T,G,T],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T,C,C,G,T,G,T],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T,C,C,G,T,C,T]]
# 4 SECUENCIAS DE 39 NUCLEOTIDOS
S35 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T,G,G,C,A,C,A,T,C,G,G,C,G,T,A],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G,T,G,G,A,A,T,C,C,G,T,G,T,A],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T,C,C,G,T,G,T,A],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T,C,C,G,T,C,T,A]]
# 4 SECUENCIAS DE 40 NUCLEOTIDOS
S36 = [[A,T,C,C,T,C,C,A,C,G,G,T,C,A,C,C,C,T,G,G,A,A,A,A,T,G,G,C,A,C,A,T,C,G,G,C,G,T,A,T],[G,T,G,G,C,G,G,A,G,A,A,G,A,C,C,C,T,A,G,G,G,G,C,C,A,G,T,G,G,A,A,T,C,C,G,T,G,T,A,T],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T,C,C,G,T,G,T,A,T],[G,T,C,G,C,G,G,A,G,A,A,G,A,C,C,T,T,A,G,G,G,G,C,C,A,G,C,G,G,C,A,T,C,C,G,T,C,T,A,T]]

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
print("Experimento N° 2 Y 3")
print("------------------------------------------------------")
print("------------------------------------------------------")
print("Secuencias Iniciales:")
print("------------------------------------------------------")
secuencias = [S0,S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S16,S17,S18,S19,S20,S21,S22,S23,S24,S25,S26,S27,S28,S29,S30,S31,S32,S33,S34,S35,S36]
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
for sec in range(0,len(secuencias)):
    print("Escenario N° " + str(escenario))
    resAux = executePD(secuencias[sec],2)
    resultadosPD.append(resAux)
    print("Score PD = " + str(resAux[1]))
    print("---------------------")
    resAux = executeGrasp(secuencias[sec],2)
    resultadosGRASP.append(resAux)
    print("Score GRASP = " + str(resAux[1]))
    escenario += 1
    print("---------------------")
    print("---------------------")
print("------------------------------------------------------")
print("Alineamiento Final:")
print("------------------------------------------------------")
escenario = 1
for sec in range(0,len(secuencias)):
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