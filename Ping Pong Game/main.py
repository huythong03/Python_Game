import pygame, sys
from settings import WIDTH, HEIGHT
from table import Table

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

class Pong:
    def __init__(self, screen):
        self.screen = screen
        self.FPS = pygame.time.Clock()
    
    def draw(self):
        pygame.display.flip()
    
    def main(self):
        #Menu bắt đầu tại đây
        table = Table(self.screen) #Chuyển vào bảng player_option đã lưu vào table.game_mod
        while True:
            self.screen.fill("black")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            table.player_move()
            table.update()
            self.draw()
            self.FPS.tick(30)

if __name__ == "__main__":
    play = Pong(screen)
    play.main()
