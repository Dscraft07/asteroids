import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # self.velocity je zděděná z CircleShape, defaultně (0,0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        """
        Metoda se volá při zničení asteroidu.
        1. Okamžitě zabije (kill) sám sebe.
        2. Pokud je asteroid malý (radius <= ASTEROID_MIN_RADIUS), jen se zničí.
        3. V opačném případě vytvoří 2 nové asteroidy se zmenšeným poloměrem a
           novými směry pohybu.
        """
        # Tento asteroid je vždy zničen
        self.kill()

        # Pokud je tento asteroid malý, už se nerozděluje
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Vypočítáme poloměr nových asteroidů
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Náhodný úhel mezi 20 a 50 stupni
        random_angle = random.uniform(20, 50)

        # Vytvoření dvou nových vektorů rotací stávající velocity
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Vytvoření dvou nových asteroidů na stejné pozici
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Nastavení jejich rychlosti
        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2
