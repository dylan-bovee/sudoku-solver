import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur_fenetre = 600
hauteur_fenetre = 600

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Grille Sudoku avec caractères")

# Taille de chaque case
taille_case = largeur_fenetre // 9

# Définition de la police pour le texte
police = pygame.font.Font(None, 50)  # Police par défaut, taille 50

# Exemple de grille avec quelques chiffres (0 signifie case vide)
grille = [
    [0, 7, 2, 9, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 6, 0, 8, 0],
    [0, 0, 0, 0, 4, 0, 0, 6, 0],
    [9, 6, 0, 0, 0, 4, 1, 0, 8],
    [0, 4, 8, 7, 0, 5, 0, 9, 6],
    [0, 0, 5, 6, 0, 8, 0, 0, 3],
    [0, 0, 0, 4, 0, 2, 0, 1, 0],
    [8, 5, 0, 0, 6, 0, 3, 2, 7],
    [1, 0, 0, 8, 5, 0, 0, 0, 0]
]

def afficher_texte(surface, texte, x, y):
    """Affiche un texte centré dans une case."""
    if texte != 0:  # Ne pas afficher les cases vides (0)
        texte_surface = police.render(str(texte), True, (0, 0, 0))  # Rendu du texte
        texte_rect = texte_surface.get_rect(center=(x, y))  # Centrage dans la case
        surface.blit(texte_surface, texte_rect)  # Affichage du texte

# Remplir l'arrière-plan en blanc
fenetre.fill((255, 255, 255))

# Dessiner la grille 9x9 avec des bordures épaisses pour les blocs 3x3
for i in range(10):  # De 0 à 9 pour inclure les bords
    x = i * taille_case
    y = i * taille_case

    # Épaisseur de la ligne
    epaisseur = 3 if i % 3 == 0 else 1  # Épaisseur plus grande toutes les 3 lignes

    # Dessiner les lignes horizontales
    pygame.draw.line(fenetre, (0, 0, 0), (0, y), (largeur_fenetre, y), epaisseur)

    # Dessiner les lignes verticales
    pygame.draw.line(fenetre, (0, 0, 0), (x, 0), (x, hauteur_fenetre), epaisseur)

# Dessiner une bordure autour de la grille
pygame.draw.rect(fenetre, (0, 0, 0), (0, 0, largeur_fenetre, hauteur_fenetre), 5)

# Afficher les chiffres de la grille dans les cases
for ligne in range(9):
    for colonne in range(9):
        valeur = grille[ligne][colonne]
        x_centre = colonne * taille_case + taille_case // 2
        y_centre = ligne * taille_case + taille_case // 2
        afficher_texte(fenetre, valeur, x_centre, y_centre)

# Mise à jour de l'affichage
pygame.display.flip()

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
