from hyparams import *

import pygame
from sys import exit
import  random

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.current_board = self.set_init_board()
        self.logic = [[1,1,1],[1,0,1],[1,1,1]]
        self.past_board = self.current_board.copy()

    def set_init_board(self):
        return [[random.choice([0,0,0,1]) for _ in range(cell_number)] for _ in range(cell_number)]

    def alive_rules(self, n):
        if n < 2:
            return 0
        elif n > 3:
            return 0
        else:
            return 1
        
    def dead_rules(self,n):
        if n == 3:
            return 1
        else:
            return 0
    
    def elementwise_product(self,list1,list2):
        result = []
        for seq1, seq2 in zip(list1,list2):
            prods = []
            for u, v in zip(seq1, seq2):
                prods.append(u * v)
            result.append(prods)
        return result

    def count_neighbour(self,list):
        sum = 0
        for i in list:
            sum = sum + i.count(1)
        return sum
    
    def update_board(self):
        self.past_board = self.current_board.copy()
        for row in range(cell_number-2):
            for col in range(cell_number-2):
                sub_board = [[self.past_board[row+p][col+q] for q in range(3)] for p in range(3)]
                result = self.elementwise_product(sub_board,self.logic)
                neighbour = self.count_neighbour(result)
                if self.past_board[row+1][col+1]:
                    state = self.alive_rules(neighbour)
                else:
                    state = self.dead_rules(neighbour)
                self.current_board[row+1][col+1] = state


    def draw_elements(self):
        for row in range(cell_number):
            for col in range(cell_number):
                cell_rect = pygame.Rect(sim_offset + col * cell_size,
                                        sim_offset + row * cell_size,
                                        cell_size,cell_size)
                if self.current_board[row][col]:
                    pygame.draw.rect(self.screen,alive_color,cell_rect)
                else:
                    pygame.draw.rect(self.screen,dead_color,cell_rect)
    
    def get_past_board(self):
        return self.past_board

    def get_current_board(self):
        return self.current_board
        
def main():
    pygame.init()

    screen = pygame.display.set_mode((2*sim_offset + cell_number * cell_size,
                                      2*sim_offset + cell_number * cell_size))
    clock = pygame.time.Clock()

    main_game = Game(screen)

    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill((175,215,70))
        main_game.draw_elements()
        main_game.update_board()
        pygame.display.update()
        clock.tick(framerate)



main()