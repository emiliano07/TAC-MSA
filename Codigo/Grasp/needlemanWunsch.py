import numpy as np
import copy as c
#-------------------------------------------------------------------------------------------------

def alineamiento(u,v):
	camino = dict()
	S = [u,v]
	matrix = [-999]
	for secuencia in range(len(S)-1,-1,-1):
		matrix = [c.deepcopy(matrix)]
		aux = c.deepcopy(matrix)
		for nucleotido in range(0,len(S[secuencia])):
			matrix.extend(c.deepcopy(aux))
	M = np.array(matrix)

	origen = [0,0]
	M[tuple(origen)] = 0
	for i in range(1,len(u)+1):
		M[(i,0)] = M[(i-1,0)] + costoGap()
		camino[(i,0)] = ((i-1,0),[u[i-1],"_"])
	for j in range(1,len(v)+1):
		M[(0,j)] = M[(0,j-1)] + costoGap()
		camino[(0,j)] = ((0,j-1),["_",v[j-1]])
	
	for i in range(1,len(u)+1):
		for j in range(1,len(v)+1):
			score = M[(i-1,j)][0] + costoGap()
			camino[(i,j)] = ((i-1,j),[u[i-1],"_"])
			scoreAux = M[(i,j-1)][0] + costoGap()
			if(scoreAux > score):
				score = scoreAux
				camino[(i,j)] = ((i,j-1),["_",v[j-1]])
			scoreDiag = M[(i-1,j-1)][0] + costoNucleotido(u[i-1],v[j-1])
			if(scoreDiag > score):
				score = scoreDiag
				camino[(i,j)] = ((i-1,j-1),[u[i-1],v[j-1]])
			M[(i,j)] = score
			
	ultimoIndice = (len(u),len(v))
	alineacion = generarCamino(camino, ultimoIndice, tuple(origen))
	resultado = dict()
	resultado["ALINEAMIENTO"] = alineacion
	resultado["SCORE"] = M[ultimoIndice][0]
	resultado["SECUENCIAS-ORIGINALES"] = S
	resultado["MATRIZ-N"] = M
	return resultado


def generarCamino(diccionario, clave, fin):
	alineacion = []
	for ind in range(0,len(fin)):
		alineacion.append([])
	ultimo = diccionario[clave]
	while(not ultimo[0] == fin):
		for ind in range(0,len(fin)):
			alineacion[ind].insert(0,ultimo[1][ind])
		ultimo = diccionario[ultimo[0]]
	for ind in range(0,len(fin)):
		alineacion[ind].insert(0,ultimo[1][ind])
	return alineacion


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