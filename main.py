import pygame
from constants import *

def main():
    # Inicializace pygame
    pygame.init()
    
    # Vytvoření okna s danými rozměry
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Hlavní herní cyklus
    while True:
        # Zpracování událostí
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Ukončí cyklus a program, když uživatel zavře okno
        
        # Krok 3: Vykreslení hry na obrazovku
        # Vyplníme obrazovku černou barvou (RGB: 0, 0, 0)
        screen.fill((0, 0, 0))
        
        # Aktualizace zobrazení - musí být voláno jako poslední krok
        pygame.display.flip()

if __name__ == "__main__":
    main()
