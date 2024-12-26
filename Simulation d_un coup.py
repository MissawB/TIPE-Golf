#############Simulation d'un coup


import PIL.Image as pili
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches


# Charger et simplifier l'image du trou
Trou10 = pili.open('D:\\TIPE 52\\USOpenTrou10NouvellesCouleurs.PNG')
Trou10 = Trou10.convert('RGB')
D1 = np.array(Trou10)

def simplifie(D1):
    l, c, _ = D1.shape
    DonnéesTrou10 = np.zeros((l, c))
    for i in range(l):
        for j in range(c):
            r, g, b = D1[i, j]
            if 210 < r < 256 and 20 < g < 50 and 30 < b < 60:
                DonnéesTrou10[i, j] = 1
            elif 0 <= r < 30 and 90 < g < 240 and 0 <= b < 30:
                DonnéesTrou10[i, j] = 2
            elif 55 < r < 70 and 190 < g < 215 and 235 < b < 256:
                DonnéesTrou10[i, j] = 3
            elif 25 < r < 40 and 25 < g < 40 and 25 < b < 40:
                DonnéesTrou10[i, j] = 4
            elif 210 < r < 256 and 210 < g < 256 and 160 < b < 190:
                DonnéesTrou10[i, j] = 5
            elif 50 < r < 70 and 60 < g < 80 and 190 < b < 210:
                DonnéesTrou10[i, j] = 6
            elif 240 < r < 256 and 200 < g < 220 and 40 < b < 55:
                DonnéesTrou10[i, j] = 7
    return DonnéesTrou10

parcours = simplifie(D1)

#On cherche l'ensemble des points du green et du tee
tee_positions = np.argwhere(parcours == 6)
green_positions = np.argwhere(parcours == 7)
if len(tee_positions) == 0 or len(green_positions) == 0:
    raise ValueError("Tee ou green non trouvés dans l'image.")

# On définit la position initilal et celle du trou
tee_position = (160,55)
x_tee,y_tee=tee_position
green_position = (90,395)
x_green,y_green=green_position
distance_parcours= np.sqrt((x_green-x_tee)**2+(y_green-y_tee)**2)

# Données des coups réels pour le Trou 10
data = [
    {"player": "A.Ancer", "round": 1, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 93, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 5, "location": "green"}]},
    {"player": "A.Ancer", "round": 2, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 135, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 5.7, "location": "green"}]},
    {"player": "A.Ancer", "round": 3, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 105, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 8.3, "location": "green"}]},
    {"player": "A.Ancer", "round": 4, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 117, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 15, "location": "fairway"}, {"shot_number": 3, "distance_to_hole": 2, "location": "green"}]},
    {"player": "W.Clark", "round": 1, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 112, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 3, "location": "green"}]},
    {"player": "W.Clark", "round": 2, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 99, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 2, "location": "green"}]},
    {"player": "W.Clark", "round": 3, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 112, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 10, "location": "green"}]},
    {"player": "W.Clark", "round": 4, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 118, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 5, "location": "green"}]},
    {"player": "R.Mcllroy", "round": 1, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 122, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 10, "location": "green"}]},
    {"player": "R.Mcllroy", "round": 2, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 117, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 4, "location": "green"}]},
    {"player": "R.Mcllroy", "round": 3, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 103, "location": "rough"}, {"shot_number": 2, "distance_to_hole": 14, "location": "bunker"}, {"shot_number": 3, "distance_to_hole": 0.7, "location": "green"}]},
    {"player": "R.Mcllroy", "round": 4, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 93, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 4.6, "location": "green"}]},
    {"player": "S.Scheffler", "round": 1, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 89, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 5.7, "location": "green"}]},
    {"player": "S.Scheffler", "round": 3, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 103, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 6, "location": "green"}]},
    {"player": "S.Scheffler", "round": 4, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 89, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 5.3, "location": "green"}]},
    {"player": "Ca.Smith", "round": 1, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 87, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 11, "location": "green"}]},
    {"player": "Ca.Smith", "round": 2, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 112, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 3, "location": "green"}]},
    {"player": "Ca.Smith", "round": 3, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 98, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 11, "location": "green"}]},
    {"player": "Ca.Smith", "round": 4, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 98, "location": "fairway"}, {"shot_number": 3, "distance_to_hole": 3, "location": "green"}]},
    {"player": "T.Fleetwood", "round": 1, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 105, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 3.333, "location": "green"}]},
    {"player": "T.Fleetwood", "round": 3, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 92, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 2, "location": "green"}]},
    {"player": "T.Fleetwood", "round": 4, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 109, "location": "fairway"}, {"shot_number": 3, "distance_to_hole": 5.3, "location": "green"}]},
    {"player": "M.Moldovan", "round": 1, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 87, "location": "rough"}, {"shot_number": 2, "distance_to_hole": 15, "location": "green"}]},
    {"player": "M.Moldovan", "round": 2, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 126, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 3.33, "location": "green"}]},
    {"player": "M.Moldovan", "round": 3, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 87, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 1.3, "location": "green"}]},
    {"player": "M.Moldovan", "round": 4, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 97, "location": "fairway"}, {"shot_number": 3, "distance_to_hole": 4, "location": "green"}]},
    {"player": "A.Potgieter", "round": 1, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 111, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 5.6, "location": "green"}]},
    {"player": "A.Potgieter", "round": 2, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 109, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 2, "location": "green"}]},
    {"player": "A.Potgieter", "round": 3, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 99, "location": "rough"}, {"shot_number": 2, "distance_to_hole": 50, "location": "fairway"}, {"shot_number": 3, "distance_to_hole": 9, "location": "green"}]},
    {"player": "A.Potgieter", "round": 4, "hole": 10, "shots": [{"shot_number": 1, "distance_to_hole": 90, "location": "fairway"}, {"shot_number": 2, "distance_to_hole": 3.6, "location": "green"}]}
]


#Création d'une liste de variable aléatoire pour chaque coup
distances_random=[]

def calcul_de_distance(i):
    distances=[]
    for entry in data:
        if entry['hole'] == 10:
            for shot in entry['shots']:
                if i>0 and i<3:
                    if shot['shot_number']==i:
                        distances.append(shot['distance_to_hole'])
                else:
                    if shot['shot_number']==3:
                        distances.append(shot['distance_to_hole'])

    # Calculer la moyenne (μ) et l'écart type (σ) des distances
    mean = sum(distances) / len(distances)
    variance = sum((x - mean) ** 2 for x in distances) / len(distances)
    std_dev = math.sqrt(variance)

    # Générer un nombre aléatoire avec une distribution gaussienne
    random_distance = random.gauss(mean, std_dev)

    return random_distance

for i in range(1,10):
    distances_random.append(calcul_de_distance(i))

print(distances_random)
# Simulation des coups basés sur les données réelles
def simulate_shots(player_data, tee_position, green_position):
    x, y = tee_position
    positions = [(x, y)]

    for shot in player_data:
        distance_totale= np.sqrt((x_green-x)**2+(y_green-y)**2)
        if distances_random[shot['shot_number']-1]>distance_parcours or distances_random[shot['shot_number']-1]> distances_random[0]:
            distance = (distances_random[shot['shot_number']]*distance_parcours)/120
        else:
             distance = (distances_random[shot['shot_number']-1]*distance_parcours)/120
        distance_y= y_green-y
        ajustement=np.arccos(distance_y/distance_totale)
        angle = random.uniform((9*np.pi/20),  (11*np.pi/20))
        dx = int(abs(distance) * np.cos(angle+ajustement))
        dy = int(abs(distance) * np.sin(angle+ajustement))
        x, y = x + dx, y + dy
        x = min(max(x, 0), parcours.shape[0] - 1)
        y = min(max(y, 0), parcours.shape[1] - 1)
        positions.append((x, y))
        if (x,y) in green_positions:
            break
    return positions

# Simulation pour un joueur
player_data = [shot for shot in trou_10_data[0]['shots']]
positions = simulate_shots(player_data, tee_position, green_position)

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
plt.imshow(parcours, cmap=cmap)  # Utilisation de la carte de couleurs personnalisée

# Ajouter une légende
labels = ['Hors limite(Out of bounds)', 'Herbe haute (Rough)', 'Herbe basse (Fairway)', 'Eau', 'Arbre', 'Sable (Bunker)', 'Départ(Tee)', 'Arrivée (Green)']
patches = [mpatches.Patch(color=colors[i], label=labels[i]) for i in range(len(labels))]
plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Affichage du parcours et des coups
plt.imshow(parcours, cmap=cmap)
x, y = zip(*positions,green_position)
plt.plot(y, x, 'ro-')  # Notons que x et y sont inversés pour l'affichage
plt.scatter([green_position[1]], [green_position[0]], color='green')  # Position du green
plt.title(f"Trajectoire des coups au round ")
plt.show()