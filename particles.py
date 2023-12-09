import pygame
from sys import exit
from random import randint
from pygame.math import Vector2
from hyparams import *

class Particle:
    def __init__(self,idx): 
        #self.x = randint(0,cell_number - 1)
        #self.y = randint(0,cell_number - 1)
        self.idx = idx

        self.state_prob = [0.2, 0.8]
        self.state = self.get_initial_state() 

        self.position = self.particle_position()
        self.no_live_neighbours = 0
    
    def randomize(self):
        num = randint(0,999)
#        div = randint(1,9)
        div = 33
        if num % div == 0:
            flag = 1
        else:
            flag = 0
        return flag 

    def get_initial_state(self):
#        flag = self.randomize()

        flag = randint(0,1)

        return flag

    def particle_position(self):
        return Vector2(int(self.idx % cell_number), int(self.idx / cell_number))

    def get_true_offset_value(self, cell_pos):
        return int(cell_pos.x * cell_size + sim_offset), int(cell_pos.y * cell_size + sim_offset)

    def get_position(self):
        return self.position
    
    def particle_update(self, live_neighbours):
        self.no_live_neighbours = live_neighbours
        self.particle_state_update()

    def particle_state_update(self):
        if self.state:
            #   when cell alive
            if self.no_live_neighbours < 2:
                self.state = self.cell_death()

            elif self.no_live_neighbours > 3:
                self.state = self.cell_death()
            
            else:
                self.state = self.cell_alive()
            
        else:
            #   when cell dead
            if self.no_live_neighbours == 3:
                self.state = self.cell_alive()
            else:
                self.state = self.cell_death()
                 
    def cell_alive(self):
        return 1

    def cell_death(self):
        return 0

    def get_state(self):
         return self.state