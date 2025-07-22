from config import rho, Tmax, Tmin
from utilitaire import profit 

def mettreAjourTetSolution(obj, T, S, PbestOfAll):
    T = [ T[i] * rho for i in range(len(T))]
    
    # On determine kmax
    liste_profit = [] 
    for S_k in S:
        liste_profit.append(profit(S_k, obj))
    kmax = liste_profit.index(max(liste_profit))
    
    Pmax = liste_profit[kmax]

    # On update de la pheromone
    for i in range(len(S[kmax])):
        if S[kmax][i] == 1:
            T[i] += 1/(1 + PbestOfAll - Pmax)

    for k in range(len(T)):
        if T[k] < Tmin:
            T[k] = Tmin
        elif T[k] > Tmax:
            T[k] = Tmax
    return T

def miseAJourCandidats(obj, candidats,b):
    return [i for i in candidats if obj[i][0] <= b]
     # Remove the first occurence of the element in the remove method 



