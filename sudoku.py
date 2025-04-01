import pygame
import sys
import time

# Initialisation de Pygame
pygame.init()

# Dimensions
LARGEUR_FENETRE = 810  # Largeur de la fenêtre
HAUTEUR_FENETRE = 700
TAILLE_GRILLE = int(LARGEUR_FENETRE * 0.70)  # Grille prend 75% de la largeur de la fenêtre
TAILLE_CASE = TAILLE_GRILLE // 9  # Taille des cases du Sudoku

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS_CLAIR = (245, 245, 245)
BLEU = (0, 0, 255)

# Police
police_titre = pygame.font.Font(None, 50)
police_texte = pygame.font.Font(None, 40)
police_grille = pygame.font.Font(None, 45)
police_info = pygame.font.Font(None, 30)

# Initialisation de la fenêtre
fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
pygame.display.set_caption("Sudoku Solver")

# Variables globales pour la grille, le compteur et le temps
grille = [[0] * 9 for _ in range(9)]
iterations = 0
temps_resolution = 0

def charger_grille(fichier):
    """Charge une grille de Sudoku depuis un fichier texte."""
    global grille, grille_initiale
    try:
        with open(fichier, "r") as f:
            lignes = f.readlines()
            grille = [list(map(int, ligne.strip().split())) for ligne in lignes if ligne.strip()]
        
        # Vérification de la structure
        if len(grille) != 9 or any(len(ligne) != 9 for ligne in grille):
            raise ValueError("Format incorrect du fichier")

        # Stocker une copie de la grille initiale
        grille_initiale = [row[:] for row in grille]  

        print(f"Grille chargée depuis {fichier} :")  # Debug
        for ligne in grille:
            print(ligne)

    except (FileNotFoundError, ValueError) as e:
        print(f"Erreur : {e}")
        grille = [[0] * 9 for _ in range(9)]  # Grille vide en cas d'erreur
        grille_initiale = [row[:] for row in grille]  # Grille vide également


def afficher_texte(surface, texte, x, y, couleur=NOIR, police=police_grille):
    """Affiche un texte centré."""
    texte_surface = police.render(texte, True, couleur)
    texte_rect = texte_surface.get_rect(center=(x, y))
    surface.blit(texte_surface, texte_rect)

def dessiner_bouton(texte, x, y, largeur, hauteur, couleur=NOIR):
    """Dessine un bouton stylisé."""
    pygame.draw.rect(fenetre, couleur, (x, y, largeur, hauteur), border_radius=10)
    texte_surface = police_texte.render(texte, True, BLANC)
    texte_rect = texte_surface.get_rect(center=(x + largeur // 2, y + hauteur // 2))
    fenetre.blit(texte_surface, texte_rect)

def menu_selection():
    """Affiche le menu de sélection des grilles."""
    while True:
        fenetre.fill(BLANC)

        # Titre
        titre = police_titre.render("Choisissez une grille", True, NOIR)
        fenetre.blit(titre, (LARGEUR_FENETRE // 2 - titre.get_width() // 2, 50))

        # Boutons de sélection de grille (centrés horizontalement)
        button_width = 300
        button_height = 60
        y_offset = 140
        for i, texte in enumerate(["Grille 1", "Grille 2", "Grille 3", "Grille 4", "Grille 5"]):
            dessiner_bouton(texte, LARGEUR_FENETRE // 2 - button_width // 2, y_offset + i * 80, button_width, button_height)

        pygame.display.flip()

        # Attente du choix
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if LARGEUR_FENETRE // 2 - button_width // 2 <= x <= LARGEUR_FENETRE // 2 + button_width // 2:
                    if 140 <= y <= 200:
                        charger_grille("grille1.txt")
                    elif 220 <= y <= 280:
                        charger_grille("grille2.txt")
                    elif 300 <= y <= 360:
                        charger_grille("grille3.txt")
                    elif 380 <= y <= 440:
                        charger_grille("grille4.txt")
                    elif 460 <= y <= 520:
                        charger_grille("grille5.txt")
                    return  # Sortie du menu pour afficher la grille

def dessiner_grille():
    """Affiche la grille avec les chiffres et les boutons."""
    fenetre.fill(GRIS_CLAIR)

    # Dessiner la bordure extérieure de la grille
    pygame.draw.rect(fenetre, NOIR, (52, 52, TAILLE_GRILLE, TAILLE_GRILLE), 5)

    # Dessiner les lignes et colonnes
    for i in range(10):
        epaisseur = 3 if i % 3 == 0 else 1
        pygame.draw.line(fenetre, NOIR, (52, 52 + i * TAILLE_CASE), (52 + TAILLE_GRILLE, 52 + i * TAILLE_CASE), epaisseur)
        pygame.draw.line(fenetre, NOIR, (52 + i * TAILLE_CASE, 52), (52 + i * TAILLE_CASE, 52 + TAILLE_GRILLE), epaisseur)

    # Afficher les chiffres
    for ligne in range(9):
        for colonne in range(9):
            if grille[ligne][colonne] != 0:
                x_centre = 52 + colonne * TAILLE_CASE + TAILLE_CASE // 2
                y_centre = 52 + ligne * TAILLE_CASE + TAILLE_CASE // 2
                couleur = NOIR if grille_initiale[ligne][colonne] != 0 else BLEU  # Bleu pour chiffres nouveau
                afficher_texte(fenetre, str(grille[ligne][colonne]), x_centre, y_centre, couleur)

    # Affichage du temps et des itérations
    espace_cadran = 20
    largeur_cadran = LARGEUR_FENETRE - (52 + TAILLE_GRILLE + espace_cadran)
    pygame.draw.rect(fenetre, GRIS_CLAIR, (52 + TAILLE_GRILLE + espace_cadran, 52, largeur_cadran, TAILLE_GRILLE), 0)
    
    afficher_texte(fenetre, f"Temps: {temps_resolution:.2f}s", 52 + TAILLE_GRILLE + espace_cadran + largeur_cadran // 2, 100, NOIR, police_info)
    afficher_texte(fenetre, f"Itérations: {iterations}", 52 + TAILLE_GRILLE + espace_cadran + largeur_cadran // 2, 150, NOIR, police_info)

    # Boutons
    button_width = (LARGEUR_FENETRE - 100) // 2
    button_height = 60
    dessiner_bouton("Retour", 50, HAUTEUR_FENETRE - 70, button_width, button_height)
    dessiner_bouton("Résoudre", 50 + button_width, HAUTEUR_FENETRE - 70, button_width, button_height)

    pygame.display.flip()


def est_valide(grille, ligne, colonne, num):
    """Vérifie si un chiffre peut être placé à une position donnée."""
    if num in grille[ligne]:
        return False
    if any(grille[i][colonne] == num for i in range(9)):
        return False

    ligne_debut, colonne_debut = (ligne // 3) * 3, (colonne // 3) * 3
    for i in range(3):
        for j in range(3):
            if grille[ligne_debut + i][colonne_debut + j] == num:
                return False
    return True
def mettre_a_jour_domaines(grille):
    """Crée une matrice des possibilités pour chaque case vide."""
    domaines = [[set(range(1, 10)) if grille[i][j] == 0 else set() for j in range(9)] for i in range(9)]
    
    for ligne in range(9):
        for colonne in range(9):
            if grille[ligne][colonne] != 0:
                num = grille[ligne][colonne]
                for i in range(9):
                    domaines[i][colonne].discard(num)  # Supprime des colonnes
                    domaines[ligne][i].discard(num)  # Supprime des lignes
                
                ligne_debut, colonne_debut = (ligne // 3) * 3, (colonne // 3) * 3
                for i in range(3):
                    for j in range(3):
                        domaines[ligne_debut + i][colonne_debut + j].discard(num)  # Supprime de la sous-grille
    return domaines

def backtracking_avec_heuristique(grille, domaines):
    """Backtracking amélioré avec heuristique MRV et propagation des contraintes."""
    global iterations
    iterations += 1

    # Trouver la meilleure case à remplir
    meilleure_case = trouver_meilleure_case(grille, domaines)
    if meilleure_case is None:
        return True  # Toutes les cases sont remplies
    
    ligne, colonne = meilleure_case
    for num in sorted(domaines[ligne][colonne]):  # Trier les valeurs possibles pour homogénéiser
        if est_valide(grille, ligne, colonne, num):
            grille[ligne][colonne] = num  # Placer le chiffre
            
            # Sauvegarde des domaines avant modification
            domaines_sauvegarde = [row[:] for row in domaines]
            
            # Mise à jour des domaines avec la propagation
            domaines[ligne][colonne] = set()
            for i in range(9):
                domaines[i][colonne].discard(num)
                domaines[ligne][i].discard(num)

            ligne_debut, colonne_debut = (ligne // 3) * 3, (colonne // 3) * 3
            for i in range(3):
                for j in range(3):
                    domaines[ligne_debut + i][colonne_debut + j].discard(num)

            # Récursion
            if backtracking_avec_heuristique(grille, domaines):
                return True
            
            # Annuler si ça ne marche pas
            grille[ligne][colonne] = 0
            domaines = domaines_sauvegarde  # Restaurer les domaines
    
    return False  # Aucun chiffre valide trouvé
def trouver_meilleure_case(grille, domaines):
    """Trouve la case vide avec le moins de choix possibles (MRV)."""
    min_options = 10  # Il y a au max 9 choix possibles
    meilleure_case = None
    
    for ligne in range(9):
        for colonne in range(9):
            if grille[ligne][colonne] == 0:
                nb_options = len(domaines[ligne][colonne])
                if nb_options < min_options:
                    min_options = nb_options
                    meilleure_case = (ligne, colonne)
    
    return meilleure_case

def resoudre_sudoku_heuristique(grille):
    """Résolution avec heuristique MRV et propagation des contraintes."""
    global iterations, temps_resolution
    iterations = 0
    temps_resolution = 0

    start_time = time.time()
    
    domaines = mettre_a_jour_domaines(grille)
    backtracking_avec_heuristique(grille, domaines)
    
    temps_resolution = time.time() - start_time

while True:
    menu_selection()

    while True:
        dessiner_grille()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 <= x <= (LARGEUR_FENETRE - 50) // 2 and HAUTEUR_FENETRE - 70 <= y <= HAUTEUR_FENETRE:
                    break  # Retour au menu
                elif (LARGEUR_FENETRE // 2 + 50) <= x <= (LARGEUR_FENETRE - 50) and HAUTEUR_FENETRE - 70 <= y <= HAUTEUR_FENETRE:
                    resoudre_sudoku_heuristique(grille)  # Utilise l'algorithme amélioré
        else:
            continue
        break