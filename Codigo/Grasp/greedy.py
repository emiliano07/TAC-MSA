import numpy as np
import operator
from random import randint
import copy as c
import Grasp.needlemanWunsch as nw
#-------------------------------------------------------------------------------------------------

def greedy(secuencias):
    S = secuencias
    pares = calcularPares(S)
    resultados = dict()
    resultados["SCORE"] = 0
    resultados["PROFILE"] = 0
    resultados["SECUENCIAS-ORIGINALES"] = S
    if(len(S) == 2):
        resultados["SCORE"] = pares[(0,1)]["SCORE"]
        resultados["MATRIZ"] = pares[(0,1)]["MATRIZ-N"]
        largo = len(pares[(0,1)]["ALINEAMIENTO"][0])
        profile = generarProfileInicial(largo)
        profile = agregarSecuencia(profile, pares[(0,1)]["ALINEAMIENTO"][0])
        profile = agregarSecuencia(profile, pares[(0,1)]["ALINEAMIENTO"][1])
        resultados["PROFILE"] = profile
    else:
        top3 = top(S,pares,3)
        eleccion = elegirAlAzar(len(top3)-1)
        par = pares[top3[eleccion]]
        score = par["SCORE"]
        largo = len(par["ALINEAMIENTO"][0])
        profile = generarProfileInicial(largo)
        profile = agregarSecuencia(profile, par["ALINEAMIENTO"][0])
        profile = agregarSecuencia(profile, par["ALINEAMIENTO"][1])
        sec = c.deepcopy(S)
        sec.pop(top3[eleccion][1])
        sec.pop(top3[eleccion][0])
        for cantidadDeIt in range(0,len(S)-2):
            p = obtenerSecuencia(profile, sec)
            sec.pop(p[1])
            profile = p[0]["PROFILE"]
            score = p[0]["SCORE"]
            matriz = p[0]["MATRIZ"]
        resultados["PROFILE"] = profile
        resultados["SCORE"] = score
        resultados["MATRIZ"] = matriz
    return resultados


def topProfile(secuencias,diccionario,numero):
    if(len(secuencias) < numero):
        numero = len(secuencias)
    miDic = dict()
    for u in range(0,len(secuencias)):
        miDic[u] = diccionario[u]["SCORE"]
    resultados = sorted(miDic.items(), key=operator.itemgetter(1))
    resultados.reverse()
    ret = []
    for i in range(0,numero):
        ret.append(resultados[i][0])
    return ret


def obtenerSecuencia(profile, secuencias):
	res = dict()
	for s in range(0,len(secuencias)):
		p = c.deepcopy(profile)
		res[s] = alinearProfileSecuencia(p,secuencias[s])
	top3 = topProfile(secuencias,res,3)
	eleccion = elegirAlAzar(len(top3)-1)
	return (res[eleccion],eleccion)


def alinearProfileSecuencia(profile, sec):
	camino = dict()
	S = [profile["SECUENCIAS"][0],sec]
	matrix = [float(-999)]
	for secuencia in range(len(S)-1,-1,-1):
		matrix = [c.deepcopy(matrix)]
		aux = c.deepcopy(matrix)
		for nucleotido in range(0,len(S[secuencia])):
			matrix.extend(c.deepcopy(aux))
	M = np.array(matrix)

	origen = [0,0]
	M[tuple(origen)] = 0
	for i in range(1,len(S[0])+1):
		M[(i,0)] = M[(i-1,0)] + costoP(profile,i-1,"_")
		camino[(i,0)] = ((i-1,0),[i-1,"_"])
	for j in range(1,len(S[1])+1):
		M[(0,j)] = M[(0,j-1)] + costoGap()
		camino[(0,j)] = ((0,j-1),[-9,S[1][j-1]])
	for i in range(1,len(S[0])+1):
		for j in range(1,len(S[1])+1):
			score = M[(i-1,j)][0] + costoP(profile,i-2,"_")
			camino[(i,j)] = ((i-1,j),[i-1,"_"])
			scoreAux = M[(i,j-1)][0] + costoGap()
			if(scoreAux > score):
				score = scoreAux
				camino[(i,j)] = ((i,j-1),[-9,S[1][j-1]])
			scoreDiag = M[(i-1,j-1)][0] + costoP(profile,i-2,S[1][j-2])
			if(scoreDiag > score):
				score = scoreDiag
				camino[(i,j)] = ((i-1,j-1),[i-1,S[1][j-1]])
			M[(i,j)] = score
			
	ultimoIndice = (len(S[0]),len(S[1]))
	alineacion = generarCaminoP(camino, ultimoIndice, tuple(origen), profile, secuencia)
	resultado = dict()
	resultado["ALINEAMIENTO"] = alineacion
	resultado["MATRIZ"] = M
	p = corregirProfile(alineacion)
	resultado["PROFILE"] = p
	resultado["SCORE"] = calcularScore(alineacion)
	return resultado


def generarCaminoP(diccionario, clave, fin, profile, secuencia):
    alineacion = []
    cantidadDeSec = profile["TOTAL"]+1
    for ind in range(0,cantidadDeSec):
        alineacion.append([])
    ultimo = diccionario[clave]	
    while(not ultimo[0] == fin):
        for ind in range(0,cantidadDeSec-1):
            if(ultimo[1][0] == -9):
                alineacion[ind].insert(0,"_")
            else:
                alineacion[ind].insert(0,profile["SECUENCIAS"][ind][ultimo[1][0]])
        alineacion[cantidadDeSec-1].insert(0,ultimo[1][1])
        ultimo = diccionario[ultimo[0]]
    for ind in range(0,cantidadDeSec-1):
        if(ultimo[1][0] == -9):
            alineacion[ind].insert(0,"_")
        else:
            alineacion[ind].insert(0,profile["SECUENCIAS"][ind][ultimo[1][0]])
    alineacion[cantidadDeSec-1].insert(0,ultimo[1][1])
    return alineacion


def costoP(profile, indice ,nucleotido):
	num = len(profile["SECUENCIAS"])
	costo_ = costoNucleotido("_",nucleotido) * (profile["MATRIZ"][indice][0] / num)
	costoA = costoNucleotido("A",nucleotido) * (profile["MATRIZ"][indice][1] / num)
	costoT = costoNucleotido("T",nucleotido) * (profile["MATRIZ"][indice][2] / num)
	costoG = costoNucleotido("G",nucleotido) * (profile["MATRIZ"][indice][3] / num)
	costoC = costoNucleotido("C",nucleotido) * (profile["MATRIZ"][indice][4] / num)
	costo = costo_ + costoA + costoT + costoG + costoC
	return costo
	

def corregirProfile(secuencias):
	profile = generarProfileInicial(len(secuencias[0]))
	for ind in range(0,len(secuencias)):
		profile = agregarSecuencia(profile, secuencias[ind])
	return profile


def generarProfileInicial(largo):
    profile = dict()
    profile["SECUENCIAS"] = []
    profile["TOTAL"] = 0
    M = [[0,0,0,0,0]]*largo # _ / A / C / G / T  =>  M[indice de nucleotido de la secuencia][caracter correspondiente]
    matrix = np.array(M)
    profile["MATRIZ"] = matrix
    return profile


def agregarSecuencia(profile, secuencia):
	p = profile
	m = p["MATRIZ"]
	s = p["SECUENCIAS"]
	for n in range(0,len(secuencia)):
		m = nuevoNucleotido(m,n,secuencia[n])
	p["MATRIZ"] = m
	p["TOTAL"] = p["TOTAL"] + 1
	s.append(secuencia)
	p["SECUENCIAS"] = s
	return p

	
def nuevoNucleotido(matriz,ind,nucleotido):
    m = matriz
    m[ind]
    if(nucleotido == "_"):
        aux = m[ind][0]
        m[ind][0] = aux + 1
    if(nucleotido == "A"):
        aux = m[ind][1]
        m[ind][1] = aux + 1
    if(nucleotido == "T"):
        aux = m[ind][2]
        m[ind][2] = aux + 1
    if(nucleotido == "G"):
        aux = m[ind][3]
        m[ind][3] = aux + 1
    if(nucleotido == "C"):
        aux = m[ind][4]
        m[ind][4] = aux + 1
    return m


def elegirAlAzar(numero):
	return randint(0,numero)


def top(secuencias,diccionario,numero):
	if(len(secuencias) < numero):
		numero = len(secuencias)
	miDic = dict()
	for u in range(0,len(secuencias)):
		for v in range(u+1,len(secuencias)):
			miDic[(u,v)] = diccionario[(u,v)]["SCORE"]
	resultados = sorted(miDic.items(), key=operator.itemgetter(1))
	resultados.reverse()
	ret = []
	for i in range(0,numero):
		ret.append(resultados[i][0]) 
	return ret


def calcularPares(S):
	resultados = dict()
	for u in range(0,len(S)):
		for v in range(u+1,len(S)):
			resultados[(u,v)] = nw.alineamiento(S[u],S[v])
	return resultados


def costoGap():
	costoGap = 1
	return costoGap


def costoNucleotido(u,v):
	match = 3
	missmatch = -1
	if (u == v):
		if(u == "_"):
			return 0
		return match
	else:
		return missmatch


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
  match = 5
  missmatch = -3
  gap = 1
  if (u == v):
    if(u == "_"):
      return 0
    return match
  else:
    if(u == "_" or v == "_"):
      return gap
    return missmatch