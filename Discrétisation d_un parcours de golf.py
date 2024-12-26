###########Discrétisation d'un parcours de golf

import PIL.Image as pili
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches

# Transformation d'une image en matrice
Trou10 = pili.open('D:\\TIPE 52\\USOpenTrou10NouvellesCouleurs.PNG')

# Image en mode RGB
Trou10 = Trou10.convert('RGB')
D1 = np.array(Trou10)

# Initialiser la matrice Données avec les mêmes dimensions que D1
Données = np.zeros((D1.shape[0], D1.shape[1]))

def simplifie(D1):
    # Obtenir les dimensions de l'image
    l, c, _ = D1.shape
    # Initialiser une matrice pour stocker les résultats
    DonnéesTrou10 = np.zeros((l, c))

    # Parcourir chaque pixel de l'image
    for i in range(l):
        for j in range(c):
            r, g, b = D1[i, j]
            # Rouge (herbe haute/Rough)
            if 210 < r < 256 and 20 < g < 50 and 30 < b < 60:
                DonnéesTrou10[i, j] = 1
            # Vert (herbe basse/Fairway)
            elif 0 <= r < 30 and 90 < g < 240 and 0 <= b < 30:
                DonnéesTrou10[i, j] = 2
            # Bleu (Eau)
            elif 55 < r < 70 and 190 < g < 215 and 235 < b < 256:
                DonnéesTrou10[i, j] = 3
            # Brun (arbre)
            elif 25 < r < 40 and 25 < g < 40 and 25 < b < 40:
                DonnéesTrou10[i, j] = 4
            # Beige (sable/bunker)
            elif 210 < r < 256 and 210 < g < 256 and 160 < b < 190:
                DonnéesTrou10[i, j] = 5
            # Bleu Foncé (tee)
            elif 50 < r < 70 and 60 < g < 80 and 190 < b < 210:
                DonnéesTrou10[i, j] = 6
            # Vert clair (arrivée/green)
            elif 240 < r < 256 and 200 < g < 220 and 40 < b < 55:
                DonnéesTrou10[i, j] = 7

    return DonnéesTrou10

# Appliquer la fonction de simplification à l'image D1
Données = simplifie(D1)

# Définir les couleurs correspondantes pour chaque catégorie
colors = ['#FFFFFF', # 0: Blanc (arrière-plan, non utilisé)
          '#D32F2F', # 1: Rouge (herbe haute/Rough)
          '#4CAF50', # 2: Vert (herbe basse/Fairway)
          '#2196F3', # 3: Bleu (Eau)
          '#3E2723', # 4: Brun (arbre)
          '#FFF59D', # 5: Beige (sable/bunker)
          '#3F51B5', # 6: Bleu Foncé (tee)
          '#8BC34A'] # 7: Vert clair (arrivée/green)

# Créer une carte de couleurs personnalisée
cmap = mcolors.ListedColormap(colors)

# Afficher la matrice discrétisée
plt.imshow(Données, cmap=cmap)  # Utilisation de la carte de couleurs personnalisée

# Ajouter une légende
labels = ['Hors limite(Out of bounds)', 'Herbe haute (Rough)', 'Herbe basse (Fairway)', 'Eau', 'Arbre', 'Sable (Bunker)', 'Départ(Tee)', 'Arrivée (Green)']
patches = [mpatches.Patch(color=colors[i], label=labels[i]) for i in range(len(labels))]
plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Afficher la barre de couleurs
plt.colorbar(ticks=[0, 1, 2, 3, 4, 5, 6, 7],location='bottom', format='%d')

#Afficher la matrice
plt.suptitle('Matrice Discrétisé')
plt.show()