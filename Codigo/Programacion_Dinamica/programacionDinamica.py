import numpy as np
import copy as c
#-------------------------------------------------------------------------------------------------

def alineamiento(S):
  camino = dict()

  # ////////////////////////////////////////////////////////////////////
  # INICIALIZO LA MATRIZ EN BLANCO
  # ////////////////////////////////////////////////////////////////////
  matrix = [-999]
  for secuencia in range(len(S)-1,-1,-1):
    matrix = [c.deepcopy(matrix)]
    aux = c.deepcopy(matrix)
    for nucleotido in range(0,len(S[secuencia])):
      matrix.extend(c.deepcopy(aux))
  M = np.array(matrix)
  
  # ////////////////////////////////////////////////////////////////////
  # CASOS BASE:
  # ////////////////////////////////////////////////////////////////////
  origen = [0]*len(S)
  M[tuple(origen)] = 0
  indicesCasoBase = []
  indicesCasoBase.append(tuple(origen))
  for secuencia in range(0,len(S)):
    indice = [0]*len(S)
    for i in range(1,len(S[secuencia])+1):
      indice[secuencia] = i
      indiceMenor = c.deepcopy(indice)
      indiceMenor[secuencia] = i-1
      res = [a_i - b_i for a_i, b_i in zip(indice, indiceMenor)]
      nucleotidos = listaDeNucleotidos(S, indice, res)
      camino[tuple(indice)] = ((indiceMenor),nucleotidos)
      M[tuple(indice)] = M [tuple(indiceMenor)] + calcularGap(S[secuencia][i-1],len(S)-1)
      indicesCasoBase.append(tuple(indice))

  # ////////////////////////////////////////////////////////////////////
  # COMPLETO LA MATRIZ:
  # ////////////////////////////////////////////////////////////////////
  restas = generarRestas(S)
  indice = siguienteIndice(S, origen, indicesCasoBase)
  while(not termine(indice)):
    score = 0
    for resta in range(0,len(restas)):
      res = [a_i - b_i for a_i, b_i in zip(indice, restas[resta])]
      resultadoResta = chequearResta(res)
      if (not indice == resultadoResta):
        scoreAnterior = M[tuple(resultadoResta)][0]
        nucleotidos = listaDeNucleotidos(S,indice,restas[resta])
        scoreCelda = calcularPares(nucleotidos)
        scoreResta = scoreCelda + scoreAnterior
        if(scoreResta > score):
          camino[tuple(indice)] = ((resultadoResta),nucleotidos)
          score = scoreResta
    M[tuple(indice)] = score
    ultimoIndice = tuple(indice)
    indice = siguienteIndice(S, indice, indicesCasoBase)
 
  # ////////////////////////////////////////////////////////////////////
  # RETORNO EL RESULTADO:
  # ////////////////////////////////////////////////////////////////////
  alineacion = generarCamino(camino,ultimoIndice, tuple(origen))
  return alineacion


def generarCamino(diccionario, clave, fin):
  alineacion = []
  for ind in range(0,len(fin)):
    alineacion.append([])
  ultimo = diccionario[clave]
  while(not tuple(ultimo[0]) == fin):
    for ind in range(0,len(fin)):
      alineacion[ind].insert(0,ultimo[1][ind])
    ultimo = diccionario[tuple(ultimo[0])]
  for ind in range(0,len(fin)):
      alineacion[ind].insert(0,ultimo[1][ind])
  return alineacion


def listaDeNucleotidos(S, indice, resta):
  lista = []
  for ind in range(0, len(resta)):
    if (resta[ind] == 0):
      lista.append("_")
    else:
      if(indice[ind] == 0):
        lista.append("_")
      else:
        lista.append(S[ind][(indice[ind])-1])
  return lista


def calcularPares(nucleotidos):
  score = 0
  gaps = 0
  nuc = []
  for indice in range(0,len(nucleotidos)):
    if (nucleotidos[indice] == "_"):
      gaps += 1
    else:
      nuc.append(nucleotidos[indice])
  for indicePrincipal in range(0,len(nuc)):
    aux = calcularGap(nuc[indicePrincipal], gaps)
    score = score + aux
    for indiceQueComparo in range(indicePrincipal+1,len(nuc)):
      aux = calcularNucleotido(nuc[indicePrincipal], nuc[indiceQueComparo])
      score = score + aux
  return score


def calcularGap(nuleotido, cantidadDeSecuenciasAComparar):
  valorGap = 1
  return valorGap * cantidadDeSecuenciasAComparar


def calcularNucleotido(nuc1, nuc2):
  match = 3
  missmatch = -1
  if (nuc1 == nuc2):
    if(nuc1 == "_"):
      return 0
    return match
  else:
    return missmatch


def siguienteIndice(S, indice, indicesCasoBase):
  elemento = len(S)-1
  sig = siguiente(S, indice, elemento)
  if(not ((tuple(sig)) in indicesCasoBase)):
    return sig
  else:
    return siguienteIndice(S, sig, indicesCasoBase)


def siguiente(S, indice, elemento):
  indaux = c.deepcopy(indice)
  aux = indaux[elemento]
  aux += 1
  if(aux > len(S[elemento])):
    if(elemento == 0):
      indaux[elemento] = -1
      return indaux
    else:
      indaux[elemento] = 0
      eleaux = elemento - 1
      return siguiente(S, indaux, eleaux)
  else:
    indaux[elemento] = aux
    return indaux


def termine(indice):
  elem = indice[0]
  if(elem == -1):
    return True
  return False


def generarRestas(S):
  restas = []
  largo = len(S)
  decimal = 2 ** len(S)
  for ind in range(1,decimal):
    binar = binarizar(ind,largo)
    restas.append(binar)
  return restas


def binarizar(numero,largo):
  decimal = numero
  binario = []
  while (decimal >= 1):
      binario.insert(0, decimal % 2)
      decimal = decimal // 2
  while (largo > len(binario)):
    binario.insert(0,0)
  return binario


def chequearResta(resta):
  res = c.deepcopy(resta)
  for i in range(0,len(resta)):
    if(resta[i] < 0):
      res[i] = 0
  return res