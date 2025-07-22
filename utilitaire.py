"""
    Fonctions utilitaires (calculs)
"""
from config import alpha, beta
import numpy as np 

def profit(S, obj):
    n = len(S)
    profit = 0
    for k in range(n):
        if S[k] == 1:
            profit += obj[k][1]
    return profit 

def eta(i: int, obj, b):
    # Fonction qui calcule l'heuristique 
    return b * obj[i][1]/obj[i][0]

def construitProb(obj, candidats, b, T):
    m = len(candidats)
    prob = [(T[candidats[i]] ** alpha) * (eta(candidats[i], obj, b) ** beta) for i in range(m)]
    s = sum(prob)
    prob = [prob[k] / s for k in range(m)]
    return prob

def choixCandidats(candidats, prob) :
     return np.random.choice(candidats, p=prob)
