import pygame
import random

breedte, hoogte = 600, 600

n = 20

Rooster_grootte = breedte // n

Kleur_Achtergrond = (255, 255, 255)  # Wit
Kleur_Rooster = (200, 200, 200)  # Licht Grijs
Kleur_Pad = (0, 0, 0)  # Zwart
Kleur_Lijn = (255, 0, 0)  # Rood

class Rooster:
    def __init__(self, n):
        self.n = n
        self.Rooster = [[False] * n for _ in range(n)]
        self.saw = []

    def start_saw(self, middelpunt):
        middelpunt = (self.n // 2, self.n // 2)
        self.saw = [middelpunt]
        self.Rooster[middelpunt[0]][middelpunt[1]] = True

    def zoek_buren(self, cel):
        x, y = cel
        buren = []
        richtingen = [(0, 1), (0, -1), (1, 0), (-1, 0)] 

        for dx, dy in richtingen:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n and not self.Rooster[nx][ny]:
                buren.append((nx, ny))

        return buren

    def groei_saw(self):
        huidige_cel = self.saw[-1]
        buren = self.zoek_buren(huidige_cel)

        if not buren:  
            return

        volgende_cel = random.choice(buren)
        self.Rooster[volgende_cel[0]][volgende_cel[1]] = True
        self.saw.append(volgende_cel)

    def teken_Rooster(self, scherm):
        for r in range(self.n):
            for c in range(self.n):
                x = c * Rooster_grootte
                y = r * Rooster_grootte
                pygame.draw.rect(scherm, Kleur_Rooster, (x, y, Rooster_grootte, Rooster_grootte), 1)

    def teken_Pad(self, scherm):
        for i in range(1, len(self.saw)):
            vorige_cel = self.saw[i - 1]
            huidige_cel = self.saw[i]
            vorige_positie = (vorige_cel[1] * Rooster_grootte + Rooster_grootte // 2, vorige_cel[0] * Rooster_grootte + Rooster_grootte // 2)
            huidige_positie = (huidige_cel[1] * Rooster_grootte + Rooster_grootte // 2, huidige_cel[0] * Rooster_grootte + Rooster_grootte // 2)
            pygame.draw.line(scherm, Kleur_Lijn, vorige_positie, huidige_positie, 2)
            pygame.draw.circle(scherm, Kleur_Pad, vorige_positie, Rooster_grootte // 4)

    def toon_rooster(self):
        for rij in self.Rooster:
            print(' '.join(['X' if cel else '.' for cel in rij]))

pygame.init()

Rooster = Rooster(n)

middelpunt = (n // 2, n // 2)
Rooster.start_saw(middelpunt)

stappen = 100

for _ in range(stappen):
    Rooster.groei_saw()

grootte = (breedte, hoogte)
scherm = pygame.display.set_mode(grootte)
pygame.display.flip()
pygame.display.set_caption("Self-Avoiding Walk")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    scherm.fill(Kleur_Achtergrond)

    Rooster.teken_Rooster(scherm)

    Rooster.teken_Pad(scherm)

    pygame.display.update()

pygame.quit()


