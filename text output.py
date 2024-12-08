import pygame
import os	

class Settings():
    Window = pygame.rect.Rect(0,0,400,400)
    font_size = 40
    red = 0
    green =0
    blue = 0




def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 50"
    pygame.init()
    screen = pygame.display.set_mode(Settings.Window.size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Text output")


    runing = True 
    while runing :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing= False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    runing = False



        if pygame.key.get_pressed()[pygame.K_PLUS]:
            Settings.font_size += 1
        if pygame.key.get_pressed()[pygame.K_MINUS] :
            Settings.font_size -=1
                #Red increes 
        if pygame.key.get_pressed()[pygame.K_r]and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            Settings.red += 1
            print("Spiuft")
            if Settings.red == 256:
                Settings.red = 255
            #Red decrees
        elif pygame.key.get_pressed()[pygame.K_r]:
            Settings.red -= 1
            print("normal")
            if Settings.red == -1:
                Settings.red = 0
        

                #Green Increes 
        if pygame.key.get_pressed()[pygame.K_g]and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            Settings.green += 1
            print("green Up")
            if Settings.green == 256:
                Settings.green = 255
            #Green decrees
        elif pygame.key.get_pressed()[pygame.K_g]:
            Settings.green -= 1
            print("green down")
            if Settings.green == -1:
                Settings.green = 0




                #Blue Increes 
        if pygame.key.get_pressed()[pygame.K_b]and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            Settings.blue += 1
            print("Blue Up")
            if Settings.blue == 256:
                Settings.blue = 255
                #Blue decrees
        elif pygame.key.get_pressed()[pygame.K_b]:
            Settings.blue -= 1
            print("Blue down")
            if Settings.blue == -1:
                Settings.blue = 0

        font = pygame.font.Font(pygame.font.get_default_font(),Settings.font_size)
        text = font.render("MOIN!",True,[Settings.red,Settings.green,Settings.blue])
        text_rect = text.get_rect()
        text_rect.center = Settings.Window.center

        
        screen.fill((200, 200, 200))
        screen.blit(text, text_rect)
        pygame.display.flip()
        

        clock.tick(60)
    pygame.quit()


if __name__ =="__main__":
    main()