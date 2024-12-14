import random
import numpy as np
import pygame

scale = 5

WALL = 0
FLOOR = 1
COLORS = [(255, 255, 255),
          (255, 0, 0),
          (0, 255, 0),
          (0, 0, 255)]

fill_prob = .4
generations = 8

shape = (150, 90)
new_map = np.ones(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        choice = random.uniform(0, 1)
        new_map[i][j] = WALL if choice < fill_prob else FLOOR

for generation in range(generations):
    for i in range(shape[0]):
        for j in range(shape[1]):
            submap = new_map[max(i-1, 0):min(i+2, new_map.shape[0]),max(j-1, 0):min(j+2, new_map.shape[1])]
            wall1away = len(np.where(submap.flatten() == WALL)[0])
            submap = new_map[max(i-2, 0):min(i+3, new_map.shape[0]),max(j-2, 0):min(j+3, new_map.shape[1])]
            wall2away = len(np.where(submap.flatten() == WALL)[0])

            if generation < 5:
                if wall1away >= 5 or wall2away <= 7:
                    new_map[i][j] = WALL
                else:
                    new_map[i][j] = FLOOR
                if i==0 or j==0 or i==shape[0]-1 or j==shape[1]-1:
                    new_map[i][j] = FLOOR
            else:
                if wall1away >= 5:
                    new_map[i][j] = WALL
                else:
                    new_map[i][j] = FLOOR

screen = pygame.display.set_mode((shape[0] * scale, shape[1] * scale))
running = True

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.image.save(screen, "./cellular_automata.png")
            running = False


    for i in range(shape[0]):
        for j in range(shape[1]):
            if new_map[i][j] == WALL:
                pygame.draw.rect(screen, random.choice(COLORS), (i * scale, j * scale, scale, scale))

        pygame.display.flip()
