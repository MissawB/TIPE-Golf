###################### Discretisation d'une image
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



##########Dictionnaire donnant des information sur le parcours

data = [
    {
        "player": "A.Ancer",
        "round": 1,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 93, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 5, "location": "green"},
        ]
    },
    {
        "player": "A.Ancer",
        "round": 2,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 135, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 5.7, "location": "green"},
        ]
    },
    {
        "player": "A.Ancer",
        "round": 3,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 105, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 8.3, "location": "green"},
        ]
    },
    {
        "player": "A.Ancer",
        "round": 4,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 117, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 15, "location": "fairway"},
            {"shot_number": 3, "distance_to_hole": 2, "location": "green"},
        ]
    },
    {
        "player": "W.Clark",
        "round": 1,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 112, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 3, "location": "green"},
        ]
    },
    {
        "player": "W.Clark",
        "round": 2,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 99, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 2, "location": "green"},
        ]
    },
    {
        "player": "W.Clark",
        "round": 3,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 112, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 10, "location": "green"},
        ]
    },
    {
        "player": "W.Clark",
        "round": 4,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 118, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 5, "location": "green"},
        ]
    },
    {
        "player": "R.Mcllroy",
        "round": 1,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 122, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 10, "location": "green"},
        ]
    },
    {
        "player": "R.Mcllroy",
        "round": 2,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 117, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 4, "location": "green"},
        ]
    },
    {
        "player": "R.Mcllroy",
        "round": 3,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 103, "location": "rough"},
            {"shot_number": 2, "distance_to_hole": 14, "location": "bunker"},
            {"shot_number": 3, "distance_to_hole": 0.7, "location": "green"},
        ]
    },
    {
        "player": "R.Mcllroy",
        "round": 4,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 93, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 4.6, "location": "green"},
        ]
    },
    {
        "player": "S.Scheffler",
        "round": 1,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 89, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 5.7, "location": "green"},
        ]
    },
    {
        "player": "S.Scheffler",
        "round": 3,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 103, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 6, "location": "green"},
        ]
    },
    {
        "player": "S.Scheffler",
        "round": 4,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 89, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 5.3, "location": "green"},
        ]
    },
    {
        "player": "Ca.Smith",
        "round": 1,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 87, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 11, "location": "green"},
        ]
    },
    {
        "player": "Ca.Smith",
        "round": 2,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 112, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 3, "location": "green"},
        ]
    },
    {
        "player": "Ca.Smith",
        "round": 3,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 98, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 11, "location": "green"},
        ]
    },
    {
        "player": "Ca.Smith",
        "round": 4,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 98, "location": "fairway"},
            {"shot_number": 3, "distance_to_hole": 3, "location": "green"},
        ]
    },
    {
        "player": "T.Fleetwood",
        "round": 1,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 105, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 3.333, "location": "green"},
        ]
    },
    {
        "player": "T.Fleetwood",
        "round": 3,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 92, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 2, "location": "green"},
        ]
    },
    {
        "player": "T.Fleetwood",
        "round": 4,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 109, "location": "fairway"},
            {"shot_number": 3, "distance_to_hole": 5.3, "location": "green"},
        ]
    },
    {
        "player": "M.Moldovan",
        "round": 1,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 87, "location": "rough"},
            {"shot_number": 2, "distance_to_hole": 15, "location": "green"},
        ]
    },
    {
        "player": "M.Moldovan",
        "round": 2,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 126, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 3.33, "location": "green"},
        ]
    },
    {
        "player": "M.Moldovan",
        "round": 3,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 87, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 1.3, "location": "green"},
        ]
    },
    {
        "player": "M.Moldovan",
        "round": 4,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 97, "location": "fairway"},
            {"shot_number": 3, "distance_to_hole": 4, "location": "green"},
        ]
    },
    {
        "player": "A.Potgieter",
        "round": 1,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 111, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 5.6, "location": "green"},
        ]
    },
    {
        "player": "A.Potgieter",
        "round": 2,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 109, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 2, "location": "green"},
        ]
    },
    {
        "player": "A.Potgieter",
        "round": 3,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 99, "location": "rough"},
            {"shot_number": 2, "distance_to_hole": 50, "location": "fairway"},
            {"shot_number": 3, "distance_to_hole": 9, "location": "green"},
        ]
    },
    {
        "player": "A.Potgieter",
        "round": 4,
        "hole": 10,
        "shots": [
            {"shot_number": 1, "distance_to_hole": 90, "location": "fairway"},
            {"shot_number": 2, "distance_to_hole": 3.6, "location": "green"},
        ]
    },
]

# Filtrer les données pour le Trou 10
trou_10_data = [
    {
        "player": d["player"],
        "round": d["round"],
        "shots": d["shots"]
    }
    for d in data if d["hole"] == 10
]

# Afficher les données filtrées
for entry in trou_10_data:
    print(f"Joueur: {entry['player']}, Round: {entry['round']}")
    for shot in entry['shots']:
        print(f"  Coup {shot['shot_number']}: Distance au Trou = {shot['distance_to_hole']}, Localisation = {shot['location']}")

# Transformer les données en une matrice
matrix = []
for entry in trou_10_data:
    for shot in entry['shots']:
        matrix.append([
            entry['player'],
            entry['round'],
            shot['shot_number'],
            shot['distance_to_hole'],
            shot['location']
        ])

# Afficher la matrice
for row in matrix:
    print(row)

##########Création d'une matrice de transition'
# Assurez-vous que le dictionnaire est correctement nommé
state_index = location_to_index

# Exemple d'extraction des transitions avec la correction
def extraire_transitions(data):
    transitions = []
    for entry in data:
        shots = entry['shots']
        for i in range(len(shots) - 1):
            current_state = shots[i]['location']
            next_state = shots[i + 1]['location']
            if current_state in state_index and next_state in state_index:
                transitions.append((state_index[current_state], state_index[next_state]))
    return transitions

transitions = extraire_transitions(trou_10_data)

# États possibles
states = ["tee", "fairway", "rough", "bunker", "green", "hole"]
num_states = len(states)

# Initialisation de la matrice de transition
transition_matrix = np.zeros((num_states, num_states))

# Conversion des localisations en indices
location_to_index = {location: index for index, location in enumerate(states)}

# Remplissage de la matrice de transition à partir des données
for entry in trou_10_data:
    shots = entry['shots']
    for i in range(len(shots) - 1):
        from_location = shots[i]['location']
        to_location = shots[i + 1]['location']
        from_index = location_to_index[from_location]
        to_index = location_to_index[to_location]
        transition_matrix[from_index, to_index] += 1

# Transformation en probabilités
row_sums = transition_matrix.sum(axis=1, keepdims=True)
row_sums[row_sums == 0] = 1  # Éviter la division par zéro
transition_matrix = transition_matrix / row_sums

# Affichage de la matrice de transition
transition_df = pd.DataFrame(transition_matrix, index=states, columns=states)
print(transition_df)

# Extraction de la sous-matrice Q (exclut l'état absorbant "hole")
Q = transition_matrix[:-1, :-1]

# Calcul de la matrice fondamentale
I = np.eye(Q.shape[0])
N = np.linalg.inv(I - Q)

# Calcul de la durée d'absorption (nombre moyen de coups pour finir)
expected_steps = N.sum(axis=1)[0]
print(f"Nombre de coups moyen pour finir le parcours à partir du tee: {expected_steps:.2f}")