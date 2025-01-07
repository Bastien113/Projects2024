import pygame
import sys

pygame.init()

screenSize = 300 
squareSize = screenSize // 3 
lineWidth = 10  
lineColor = (0, 0, 0)  
xColor = (66, 66, 66) 
oColor = (28, 170, 156)
victoryColor = (255, 0, 0)
white = (255, 255, 255)

ecran = pygame.display.set_mode((screenSize, screenSize))
pygame.display.set_caption("Morpion")

plateau = [[" " for _ in range(3)] for _ in range(3)]
joueur_actuel = "X"

def dessiner_lignes():
    for i in range(1, 3):
        pygame.draw.line(ecran, lineColor, (0, i * squareSize), (screenSize, i * squareSize), lineWidth)
    for i in range(1, 3):
        pygame.draw.line(ecran, lineColor, (i * squareSize, 0), (i * squareSize, screenSize), lineWidth)

def dessiner_XO():
    for ligne in range(3):
        for col in range(3):
            if plateau[ligne][col] == "X":
                dessiner_X(ligne, col)
            elif plateau[ligne][col] == "O":
                dessiner_O(ligne, col)

def dessiner_X(ligne, col):
    start_x = col * squareSize + 20
    start_y = ligne * squareSize + 20
    end_x = (col + 1) * squareSize - 20
    end_y = (ligne + 1) * squareSize - 20
    pygame.draw.line(ecran, xColor, (start_x, start_y), (end_x, end_y), lineWidth)
    pygame.draw.line(ecran, xColor, (start_x, end_y), (end_x, start_y), lineWidth)

def dessiner_O(ligne, col):
    centre_x = col * squareSize + squareSize // 2
    centre_y = ligne * squareSize + squareSize // 2
    rayon = squareSize // 3
    pygame.draw.circle(ecran, oColor, (centre_x, centre_y), rayon, lineWidth)

def dessiner_ligne_victoire(joueur, ligne, col, direction):
    couleur = victoryColor
    if direction == "horizontal":
        y = ligne * squareSize + squareSize // 2
        pygame.draw.line(ecran, couleur, (20, y), (screenSize - 20, y), lineWidth)
    elif direction == "vertical":
        x = col * squareSize + squareSize // 2
        pygame.draw.line(ecran, couleur, (x, 20), (x, screenSize - 20), lineWidth)
    elif direction == "diag1":
        pygame.draw.line(ecran, couleur, (20, 20), (screenSize - 20, screenSize - 20), lineWidth)
    elif direction == "diag2":
        pygame.draw.line(ecran, couleur, (screenSize - 20, 20), (20, screenSize - 20), lineWidth)

def verifier_victoire(joueur):
    for ligne in range(3):
        if plateau[ligne][0] == plateau[ligne][1] == plateau[ligne][2] == joueur:
            return True
    for col in range(3):
        if plateau[0][col] == plateau[1][col] == plateau[2][col] == joueur:
            return True
    if plateau[0][0] == plateau[1][1] == plateau[2][2] == joueur:
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] == joueur:
        return True
    return False

def reinitialiser_jeu():
    global plateau, joueur_actuel
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueur_actuel = "X"

def jeu():
    global joueur_actuel
    ecran.fill(white)
    dessiner_lignes()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                souris_x = event.pos[0] // squareSize
                souris_y = event.pos[1] // squareSize

                if plateau[souris_y][souris_x] == " ":
                    plateau[souris_y][souris_x] = joueur_actuel
                    dessiner_XO()
                    joueur_actuel = "O" if joueur_actuel == "X" else "X"

            dessiner_XO()
        pygame.display.update()

if __name__ == "__main__":
    jeu()