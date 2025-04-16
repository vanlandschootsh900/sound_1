import pygame
import random
import sys
import time

FPS = 60

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

TITLE ='pygame template'

PURPLE = (160, 32, 240, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

sound_1 = 'bad-to-the-bone-made-with-Voicemod.ogg'
sound_2 = ''
sound_3 = ''
pygame.mixer.init()




def init_game ():
    
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
   
    
    pygame.display.set_caption(TITLE)
    return screen






def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False 
    return True

def bad_bone():
    pygame.mixer.sound('bad-to-the-bone-made-with-Voicemod.ogg')
    pygame.mixer.Sound.play(loops=0, maxtime=0,fade_ms=0)



def main():
    
    screen = init_game()
    clock = pygame.time.Clock()



    running = True
    while running:
        running = handle_events()
        screen.fill(WHITE) # Use color from config
        
        
        bad_bone




        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()