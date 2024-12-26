#########Calcul et affichage de n z-score

import matplotlib.pyplot as plt

def zscore(e, t, u):
    return abs(e - t) / u

def nzscore(E, T, u):
    n = len(E)
    n2 = len(T)
    if n != n2:
        return "Problème de la taille de tableau"
    R = []
    for i in range(n):
        R.append(zscore(E[i], T[i], u))
    return R

# Matrice des valeurs théoriques
T = [0.85344, 1.70688, 2.52984, 3.38328, 4.17576, 4.99872, 5.76072, 6.52272, 7.28472,
     8.04672, 8.93064, 9.96696, 11.21664, 12.74064, 14.59992, 16.85544, 19.56816, 22.76856,
     26.27376, 29.96184, 33.6804, 37.21608, 40.35552, 42.85488, 44.53128, 45.4152]

# Matrice des valeurs expérimentales
E = [0.82296, 1.61544, 2.4384, 3.23088, 4.05384, 4.8768, 5.66928, 6.49224,
     7.19328, 8.10768, 8.8392, 9.72312, 11.06424, 12.83208, 14.6304, 16.9164, 19.75104,
     22.86, 26.0604, 29.718, 33.528, 36.8808, 39.9288, 42.85488, 44.5008, 44.6532]

# Incertitude
u = 0.08

# Calcul des z-scores
z_scores = nzscore(E, T, u)

# Visualisation des résultats
plt.figure(figsize=(10, 6))
plt.plot(z_scores, marker='o', linestyle='-', color='b', label='Z-scores')
plt.axhline(y=2, color='r', linestyle='--', label='Seuil de z-score = 2')
plt.xlabel('Index')
plt.ylabel('Z-score')
plt.title('Graphique des Z-scores pour les valeurs expérimentales et théoriques')
plt.legend()
plt.grid(True)
plt.show()
