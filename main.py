from utilitaire import choixCandidats, construitProb, profit
from config import alpha, beta, rho, Tmin, Tmax
import numpy as np
from visualisation import plot_progress, plot_selection


# Example data for the knapsack problem
# obj = list of (ri, pi) where ri is the size, pi is the profit
obj = [(10, 25), (40, 20), (1, 15), (4, 40), (5, 50)]
b = 15  # Capacity of the backpack
nb_it = 10  # Number of iterations
nbAnts = 5  # Number of ants

SbestOfAll, PbestOfAll = [], []
n = len(obj)
T = [Tmax] * n
PbestOfAll = 0
SbestOfAll = [0] * n

profits_over_time = [] # Visualisation module 

for it in range(nb_it):
    S = [n * [0] for _ in range(nbAnts)]

    for k in range(nbAnts):
        b2 = b
        oO = np.random.randint(0, n)
        S[k][oO] = 1
        b2 -= obj[oO][0]
        candidats = [i for i in range(n) if i != oO]
        
        while b2 > 0 and candidats != []:
            # Construire les probas 
            prob = construitProb(obj, candidats, b2, T)
            candidat = choixCandidats(candidats, prob)
            S[k][candidat] = 1
            b2 -= obj[candidat][0]
            candidats.remove(candidat)
    # Evaluate all solutions for this iteration
    best_profit_this_iter = PbestOfAll
    for k in range(nbAnts):
        p = profit(S[k], obj)
        if p > PbestOfAll:
            PbestOfAll = p
            SbestOfAll = S[k][:]
        if p > best_profit_this_iter:
            best_profit_this_iter = p
    profits_over_time.append(best_profit_this_iter)

# Display the optimal solution
print("Optimal selection (0/1 for each object):", SbestOfAll)
print("Selected objects:", [i for i, x in enumerate(SbestOfAll) if x == 1])
print("Total profit:", PbestOfAll)

# Visualize progress and selection
plot_progress(profits_over_time)
plot_selection(SbestOfAll, obj)










