from utilitaire import choixCandidats, construitProb, profit
from mise_a_jour import mettreAjourTetSolution, miseAJourCandidats
from config import alpha, beta, rho, Tmin, Tmax
import numpy as np
from visualisation import plot_progress, plot_selection
import random

# -------------------------------
# Select test case here (1, 2, or 3)
test_case = 3
# -------------------------------

if test_case == 1:
    # 20 items, large capacity
    obj = [
        (12, 24), (7, 13), (11, 23), (8, 15), (9, 16),
        (15, 28), (6, 12), (14, 27), (10, 20), (13, 25),
        (5, 10), (16, 30), (9, 18), (7, 14), (8, 17),
        (12, 26), (11, 22), (10, 19), (13, 24), (14, 29)
    ]
    b = 70
    nbAnts = 10
    nb_it = 30

elif test_case == 2:
    # 50 items, very large capacity
    random.seed(42)
    obj = [(random.randint(5, 20), random.randint(10, 40)) for _ in range(50)]
    b = 15
    nbAnts = 20
    nb_it = 50

elif test_case == 3:
    # 100 items, huge capacity
    random.seed(123)
    obj = [(random.randint(1, 30), random.randint(5, 100)) for _ in range(100)]
    b = 33
    nbAnts = 5
    nb_it = 70

else:
    raise ValueError("Invalid test_case value. Choose 1, 2, or 3.")

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
            candidats = miseAJourCandidats(obj, candidats, b2)
        

    T = mettreAjourTetSolution(obj, T, S, PbestOfAll)


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










