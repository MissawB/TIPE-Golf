########Distribution des coups réels

import matplotlib.pyplot as plt
import numpy as np

# Données tiré de GPA tour
coups = [3, 4, 5, 6]
frequences = [79, 308, 51, 4]

# Calcul de la moyenne pondérée des coups
moyenne_coups = np.average(coups, weights=frequences)

# Graphique du nombre de coups moyen réel
plt.bar(coups, frequences, edgecolor='black')
plt.axvline(moyenne_coups, color='r', linestyle='dashed', linewidth=1, label=f'Moyenne: {moyenne_coups:.2f}')
plt.xlabel('Nombre de coups')
plt.ylabel('Fréquence')
plt.title('Distribution du nombre de coups pour atteindre le trou en réalité')
plt.legend()

# Afficher le graphique
plt.show()