import copy as c
import Grasp.greedy as gdy
import Grasp.busquedaLocal as blo
#-------------------------------------------------------------------------------------------------

def grasp(limiteIteracion, secuencias):
    iteracion = 0
    mejorValor = -999
    res = gdy.greedy(secuencias)
    while(iteracion < limiteIteracion):
        g = gdy.greedy(secuencias)
        bl = blo.busquedaLocal(g)
        if(mejorValor < bl["SCORE"]):
            mejorValor = c.deepcopy(bl["SCORE"])
            res = bl
        iteracion += 1
    return res