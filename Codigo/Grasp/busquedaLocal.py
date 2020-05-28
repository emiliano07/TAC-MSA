import numpy as np
import copy as c
#-------------------------------------------------------------------------------------------------

def busquedaLocal(g):
    gAux = c.deepcopy(g)
    mejore = True
    it = 0
    while(mejore):
        bl = busquedaLocalAux(gAux)
        mejore = bl[1]
        gAux = c.deepcopy(bl[0])
        it += 1
    return gAux


def calcularScore(secuencias):
  score = 0
  for u in range(0,len(secuencias)):
    for v in range(u+1,len(secuencias)):
      score += scorePar(secuencias[u],secuencias[v])
  return score


def scorePar(u,v):
  score = 0
  for i in range(0,len(u)):
    score += costoNucleotido(u[i],v[i])
  return score


def busquedaLocalAux(g): 
    alineaciones = c.deepcopy(g["PROFILE"]["SECUENCIAS"])
    rev = (c.deepcopy(g),False)
    for sec in range(0,len(alineaciones)):
        for nuc in range(0,len(alineaciones[sec])):
            rev = revision(g, alineaciones, sec, nuc)
            if(rev[1]):
                score = calcularScore(rev[0]["PROFILE"]["SECUENCIAS"])
                rev[0]["SCORE"] = score
                return rev
    score = calcularScore(rev[0]["PROFILE"]["SECUENCIAS"])
    rev[0]["SCORE"] = score
    rev = (rev[0],False)
    return rev

		
def revision(greedy,alineaciones,sec,nuc):
    g = c.deepcopy(greedy)
    if(not (alineaciones[sec][nuc] == "_")):
        if(nuc == 0):
            if(alineaciones[sec][nuc+1] == "_"): # miro derecha si hay un gap
                # si lo hay los cambio y calculo el nuevo alineamiento y score(para esa columna)
                nuevoAlineamiento = calcularNuevoAlineamiento(alineaciones, +1, sec, nuc)
                viejoScore = calcularScore(g["PROFILE"]["SECUENCIAS"])
                nuevoScore = calcularScore(nuevoAlineamiento)
                if(nuevoScore > viejoScore):
                    # si es mayor me lo quedo y le hago la busqueda local
                    g["PROFILE"]["SECUENCIAS"] = nuevoAlineamiento
                    g["SCORE"] = nuevoScore
                    return (g,True)
        else:
            if(nuc == (len(alineaciones[sec])-1)): # miro si es el ultimo elemento
                if(alineaciones[sec][nuc-1] == "_"): # miro a la izquierda si hay un gap
                    # si lo hay los cambio y calculo el nuevo alineamiento y score(para esa columna)
                    nuevoAlineamiento = calcularNuevoAlineamiento(alineaciones, -1, sec, nuc)
                    viejoScore = calcularScore(g["PROFILE"]["SECUENCIAS"])#permutacion[1]
                    nuevoScore = calcularScore(nuevoAlineamiento)#permutacion[2]
                    if(nuevoScore > viejoScore):
                        # si es mayor me lo quedo y le hago la busqueda local
                        g["PROFILE"]["SECUENCIAS"] = nuevoAlineamiento
                        g["SCORE"] = nuevoScore
                        return (g,True)
            else: # es un elemento del medio
                if(alineaciones[sec][nuc+1] == "_"): # miro derecha si hay un gap
                    # si lo hay los cambio y calculo el nuevo alineamiento y score(para esa columna)
                    nuevoAlineamiento = calcularNuevoAlineamiento(alineaciones, +1, sec, nuc)
                    viejoScore = calcularScore(g["PROFILE"]["SECUENCIAS"])#permutacion[1]
                    nuevoScore = calcularScore(nuevoAlineamiento)#permutacion[2]
                    if(nuevoScore > viejoScore):
                        # si es mayor me lo quedo y le hago la busqueda local
                        g["PROFILE"]["SECUENCIAS"] = nuevoAlineamiento
                        g["SCORE"] = nuevoScore
                        return (g,True)
                if(alineaciones[sec][nuc-1] == "_"):# miro a la izquierda si hay un gap
                    # si lo hay los cambio y calculo el nuevo alineamiento y score(para esa columna)
                    nuevoAlineamiento = calcularNuevoAlineamiento(alineaciones, -1, sec, nuc)
                    viejoScore = calcularScore(g["PROFILE"]["SECUENCIAS"])#permutacion[1]
                    nuevoScore = calcularScore(nuevoAlineamiento)#permutacion[2]
                    if(nuevoScore > viejoScore):
                        # si es mayor me lo quedo y le hago la busqueda local
                        g["PROFILE"]["SECUENCIAS"] = nuevoAlineamiento
                        g["SCORE"] = nuevoScore
                        return (g,True)
    return (g,False)


def calcularNuevoAlineamiento(secuencias, direccion, indice, nucleotido):
    na = c.deepcopy(secuencias)
    na[indice][nucleotido+direccion] = na[indice][nucleotido]
    na[indice][nucleotido] = "_"
    return na


def costoNucleotido(u,v):
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