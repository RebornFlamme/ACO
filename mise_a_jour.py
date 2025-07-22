from main import T, SbestOfAll, PbestOfAll, Tmin, Tmax, rho



def mettreAjourTetSolution(obj, T, S):
    T = [ T[i] * rho for i in range(len(T))]
    
    # On determine kmax
    liste_profit = [] 
    for S_k in S:
        liste_profit.append(profit(S_k))
    kmax = liste_profit.index(max(liste_profit))
    
    Pmax = liste_profit[kmax]

    # On update de la pheromone
    for i in range(len(S[kmax])):
        if S[kmax][i] == 1:
            T[i] += 1/(1 + PbestOfAll - Pmax)

    for tau in T:
        if tau < Tmin:
            tau = Tmin
        elif tau > Tmax:
            tau = Tmax
    return T

def miseAJourCandidats(obj, candidats,b):
    for k in range(len(candidats)):
        if obj[k][0] > b:
            candidats[k] = 0


