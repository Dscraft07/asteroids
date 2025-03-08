import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        # Počáteční rychlost nastavíme až při střelbě
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        # Vykreslíme střelu jako bílý kruh
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Pohyb střely: aktualizace pozice na základě velocity a dt
        self.position += self.velocity * dt
