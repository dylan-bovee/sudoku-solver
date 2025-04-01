import pygame
import time

# Taille de la grille
M = 9
TAILLE_CASE = 50
MARGE = 20
LARGEUR_FENETRE = M * TAILLE_CASE + 2 * MARGE
HAUTEUR_FENETRE = M * TAILLE_CASE + 2 * MARGE

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (200, 200, 200)
BLEU = (0, 0, 255)

# Initialisation de la grille
sudoku_grille = [
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

# Fonction de dessin
def dessiner_grille(fenetre):
    fenetre.fill(BLANC)
    for i in range(M + 1):
        epaisseur = 3 if i % 3 == 0 else 1
        pygame.draw.line(fenetre, NOIR, (MARGE, MARGE + i * TAILLE_CASE), (MARGE + M * TAILLE_CASE, MARGE + i * TAILLE_CASE), epaisseur)
        pygame.draw.line(fenetre, NOIR, (MARGE + i * TAILLE_CASE, MARGE), (MARGE + i * TAILLE_CASE, MARGE + M * TAILLE_CASE), epaisseur)
    
    font = pygame.font.Font(None, 40)
    for i in range(M):
        for j in range(M):
            if sudoku_grille[i][j] != 0:
                texte = font.render(str(sudoku_grille[i][j]), True, NOIR)
                fenetre.blit(texte, (MARGE + j * TAILLE_CASE + 15, MARGE + i * TAILLE_CASE + 10))

def est_valide(grille, ligne, colonne, num):
    for x in range(9):
        if grille[ligne][x] == num or grille[x][colonne] == num:
            return False
    debut_ligne, debut_colonne = (ligne // 3) * 3, (colonne // 3) * 3
    for i in range(3):
        for j in range(3):
            if grille[debut_ligne + i][debut_colonne + j] == num:
                return False
    return True

def resoudre_sudoku(grille, fenetre):
    for ligne in range(M):
        for colonne in range(M):
            if grille[ligne][colonne] == 0:
                for num in range(1, 10):
                    if est_valide(grille, ligne, colonne, num):
                        grille[ligne][colonne] = num
                        dessiner_grille(fenetre)
                        pygame.display.update()
                        time.sleep(0.05)
                        if resoudre_sudoku(grille, fenetre):
                            return True
                        grille[ligne][colonne] = 0
                        dessiner_grille(fenetre)
                        pygame.display.update()
                return False
    return True

def main():
    pygame.init()
    fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
    pygame.display.set_caption("Sudoku Solver")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    resoudre_sudoku(sudoku_grille, fenetre)
        
        dessiner_grille(fenetre)
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()
