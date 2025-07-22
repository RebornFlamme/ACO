
"""
Liste objet, ou obj[i] = r_i
"""


def mettreAjourTetSolution(obj, T, S):
    global SbestOfAll, PbestOfAll
    # Evaporation 
    T = [ T[i] * rho for i in range(len(T))]
    
    
    # On determine kmax
    liste_profit = [] 
    for S_k in S:
        liste_profit.append(profit(S_k))
    kmax = liste_profit.index(max(liste_profit))
    
    




def profit(S):
    n = len(S)
    for k in range(n):
        for i in range(n):
            if S[k][i] == 1:
                profit += obj[i]
            else:
                profit += 1 - obj[i]
    return profit

