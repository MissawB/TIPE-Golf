import PIL.Image as pili
import numpy as np
import matplotlib.pyplot as plt
import random
import math

# Transformation d'une image en matrice
Trou10 = pili.open('D:\\TIPE 52\\Images pour diapo\\USOpenTrou10NouvellesCouleurs.PNG')

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

# Simplifier l'image pour obtenir la matrice du parcours
parcours = simplifie(D1)

# Dictionnaire de données
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

# Vérification des positions du tee et du green
tee_positions = np.argwhere(parcours == 6)
green_positions = np.argwhere(parcours == 7)

if len(tee_positions) == 0:
    raise ValueError("Position du tee (bleu foncé) non trouvée dans l'image.")
if len(green_positions) == 0:
    raise ValueError("Position du green (vert clair) non trouvée dans l'image.")

# On définit la position initiale et celle du trou
tee_position = (160,55)
x_tee,y_tee=tee_position
green_position = (90,395)
x_green,y_green=green_position
distance_parcours= np.sqrt((x_green-x_tee)**2+(y_green-y_tee)**2)


def calcul_de_distance(i):
    distances = []
    for entry in data:
        if entry['hole'] == 10:
            for shot in entry['shots']:
                if i == 1 and shot['shot_number'] == 1:
                    distances.append(shot['distance_to_hole'])
                elif i == 2 and shot['shot_number'] == 2:
                    distances.append(shot['distance_to_hole'])
                elif i >= 3 and shot['shot_number'] == 3:
                    distances.append(shot['distance_to_hole'])

    if not distances:
        print(f"Aucune distance trouvée pour le coup numéro {i}. Retour par défaut de 0.")
        return 0  # ou une autre valeur par défaut appropriée

    # Calculer la moyenne (μ) et l'écart type (σ) des distances
    mean = sum(distances) / len(distances)
    variance = sum((x - mean) ** 2 for x in distances) / len(distances)
    std_dev = math.sqrt(variance)

    # Générer un nombre aléatoire avec une distribution gaussienne
    random_distance = random.gauss(mean, std_dev)

    return random_distance

# Fonction pour simuler un coup de golf
def simuler_coup(position, distance, angle, parcours):
    l, c = parcours.shape
    x, y = position
    distance_totale = np.sqrt((green_position[0] - x) ** 2 + (green_position[1] - y) ** 2)
    distance_y = green_position[1] - y
    distance_x=green_position[0] - x
    ajustement = np.arccos(distance_y / distance_totale)
    dx = int(distance * np.cos(angle + ajustement))
    dy = int(distance * np.sin(angle + ajustement))
    x_new, y_new = x + dx, y + dy
    if 0 <= x_new < l and 0 <= y_new < c:
        return (x_new, y_new)
    else:
        return (x, y)

# Fonction pour simuler un parcours de golf à partir du tee
def simuler_parcours(parcours, tee_position, green_position, num_simulations=100, max_coups=6):
    transitions = np.zeros((8, 8))
    coups_moyens = []

    for sim in range(num_simulations):
        position = tee_position
        coups = 0
        malus_zone = 1
        while position not in green_positions and coups < max_coups:
            current_zone = parcours[position]
            angle = random.uniform((9*np.pi/20),  (11*np.pi/20))
            distance = (calcul_de_distance(coups+1)*distance_parcours)/150* malus_zone
            if distance == 0:
                print(f"Simulation {sim + 1}: Distance calculée nulle pour le coup {coups + 1}.")
                break
            new_position = simuler_coup(position, distance, angle, parcours)
            new_zone = parcours[new_position]
            transitions[int(current_zone)][int(new_zone)] += 1
            coups += 1
            print(f"Simulation {sim + 1}, coup {coups}: de {position} à {new_position} (zone {current_zone} à {new_zone})")

            if new_zone == 7:  # Si la balle atteint le green, arrêter la simulation
                break
            elif new_zone == 5:  # Si la balle atteint du sable, elle est fortement ralentie
                position = new_position
                malus_zone = 8
            elif new_zone == 4:  # Si la balle atteint les arbres, le golfeur frappe moins fort pour en sortir
                position = new_position
                malus_zone = 3
            elif new_zone == 3:  # Si la balle atteint de l'eau, le prochain tir revient en arrière
                # À vous de décider la position, ici on laisse la position inchangée
                malus_zone = malus_zone
            elif new_zone == 2:  # Si la balle atteint le fairway, elle n'est pas ralentie
                position = new_position
                malus_zone = 1
            elif new_zone == 1:  # Si la balle atteint des hautes herbes, elle est légèrement ralentie
                position = new_position
                malus_zone = 1.25
            elif new_zone == 0: # Si la balle sort des limites on abandonne le parcours (problème de simulation)
                break
        if position in green_positions:
            if position!=green_position:
                coups_moyens.append(coups + 1)  # Ajouter 1 pour le coup final dans le trou
            else:
                coups_moyens.append(coups) # Direct dans le trou


    # Normaliser la matrice de transition
    for i in range(8):
        row_sum = transitions[i].sum()
        if row_sum > 0:
            transitions[i] /= row_sum

    return transitions, coups_moyens

# Simuler le parcours de golf
transition_matrix, coups_moyens = simuler_parcours(parcours, tuple(tee_position), tuple(green_position))

print("Matrice de Transition:")
print(transition_matrix)

# Afficher la matrice de transition avec les légendes
fig, ax = plt.subplots()
cax = ax.matshow(transition_matrix, cmap='hot')
fig.colorbar(cax)

# Ajouter les légendes aux axes
zones_labels = [
    'Hors limite', # Zone 0 (Pas utilisé)
    'Rough',       # Zone 1 (Herbe haute)
    'Fairway',     # Zone 2 (Allée)
    'Eau',         # Zone 3 (Eau)
    'Arbre',       # Zone 4 (Arbre)
    'Bunker',      # Zone 5 (Sable)
    'Tee',         # Zone 6 (Départ)
    'Green'        # Zone 7 (Arrivée)
]

ax.set_xticks(np.arange(len(zones_labels)))
ax.set_yticks(np.arange(len(zones_labels)))
ax.set_xticklabels(zones_labels)
ax.set_yticklabels(zones_labels)

plt.xlabel('Zones cibles')
plt.ylabel('Zones de départ')
plt.title('Matrice de transition des zones du parcours')

plt.show()

# Afficher le nombre de coups moyen pour atteindre le green
coups_moyens = np.array(coups_moyens)
moyenne_coups = np.mean(coups_moyens)

print(f"Nombre de coups moyen pour atteindre le trou: {moyenne_coups:.2f}")

# Graphique du nombre de coups moyen
plt.hist(coups_moyens, bins=range(int(min(coups_moyens)), int(max(coups_moyens)) + 1), edgecolor='black')
plt.axvline(moyenne_coups, color='r', linestyle='dashed', linewidth=1)
plt.xlabel('Nombre de coups')
plt.ylabel('Fréquence')
plt.title('Distribution du nombre de coups pour atteindre le trou')
plt.show()