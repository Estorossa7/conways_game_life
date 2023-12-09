#import multiprocessing
#from life import game
#import os
#
#def my_function(num):
#    x = 100
#    y = 0
#    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
#    game(num)
#
#if __name__ == "__main__":
#    num_processes = 2  # Define the number of processes
#    processes = []
#    
#    for i in range(num_processes):
#        num = i+1
#        process = multiprocessing.Process(target=my_function,args=[num])
#        processes.append(process)
#        print("game started!!!")
#        process.start()
#
#    for process in processes:
#        process.join()  # Wait for all processes to finish

import pygame
import multiprocessing
from game import game
import os

pygame.init()

def instances(num):
    posi = [(10,50), (10,500), (400,50), (400,500), (800,50), (800,500), (1180,50), (1180,500)]
    x, y = posi[num]
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    print(num,x,y)
    game()

if __name__=="__main__":
    num_processes = 8  # Define the number of processes
    processes = []
    
    for i in range(num_processes):
        process = multiprocessing.Process(target=instances, args=[i])
        processes.append(process)
        process.start()

    for process in processes:
        process.join()  # Wait for all processes to finish
