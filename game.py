import pygame
from sys import exit
from random import randint
from pygame.math import Vector2
from hyparams import *

from particles import Particle

global screen

class Main:
    def __init__(self, screen):
        self.particle_list = [Particle(i) for i in range(cell_number*cell_number)]
        self.screen = screen

    def get_live_neighbours(self, particle):
        number = 0
        neighbour_idx_list = []
        idx = particle.idx
        for i in [-1,1,0]:
             for j in [-cell_number, cell_number,0]:
                n = int(idx + i + j)
                if n >= 0 and n<(cell_number*cell_number):
                    neighbour_idx_list.append(n)
                if len(neighbour_idx_list)==8:
                    break
        for idx in neighbour_idx_list:
            if self.particle_list[idx].get_state():
                number += 1
        return number
    
    def update(self):
        for particle in self.particle_list:
            live_neighbours = self.get_live_neighbours(particle)
            particle.particle_update(live_neighbours)

    def draw_sim_surf(self):
        self.sim_bg_color = (32,32,32)
        sim_rect = pygame.Rect(sim_offset,sim_offset, cell_number * cell_size,cell_number * cell_size)
        pygame.draw.rect( self.screen, self.sim_bg_color, sim_rect)

    def draw_particle(self,particle):
        x, y = particle.get_true_offset_value(particle.get_position())
        particle_rect = pygame.Rect(x,y, cell_size, cell_size)

        if particle.get_state():
            pygame.draw.rect( self.screen, alive_color, particle_rect)
        else:
            pygame.draw.rect( self.screen, dead_color, particle_rect)

    def draw_elements(self):
        self.draw_sim_surf()

        # drawing particles
        for particle in self.particle_list:
            self.draw_particle(particle)

def game():

    screen = pygame.display.set_mode((cell_number * cell_size + 2 * sim_offset , cell_number * cell_size + 2 * sim_offset ))

    pygame.display.set_caption('simple sim')

    clock = pygame.time.Clock()

    main_game = Main(screen)

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE,screen_update_timer)

# game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == SCREEN_UPDATE:
                main_game.update()

        screen.fill((0, 0, 0))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(60)



















