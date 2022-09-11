import pygame

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)



class Player:

    def __init__(self, win, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.win = win
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.x = 100
        self.y = SCREEN_HEIGHT/2
        self.width = 50
        self.height = 50
        self.vel = 6
        self.x_collide = False
        self.y_collide = False
        self.deltax = 0
        self.deltay = 0
        self.fireball_list = []
        self.dragon_one = pygame.image.load("./sprites/dragon_one.png")
        self.dragon_two = pygame.image.load("./sprites/dragon_two.png")
        self.dragon_image_list = [self.dragon_one, self.dragon_two]
        self.dragon_image_count = 0
        self.fire_one = pygame.image.load("./sprites/fire_one.png")
        self.fire_two = pygame.image.load("./sprites/fire_two.png")
        self.fire_list = [self.fire_one, self.fire_two]
        self.fire_count = 0
        self.fire_x = self.x + self.width
        self.fire_y = self.y + 30
        

    def movement(self, collision):
        keys = pygame.key.get_pressed()

        self.deltax = 0
        self.deltay = 0

        #GRAVITY
        self.deltay += 2

        if keys[pygame.K_d]:
            self.deltax += self.vel
        if keys[pygame.K_a]:
            self.deltax -= self.vel
        if keys[pygame.K_w]:
            self.deltay -= self.vel
        if keys[pygame.K_s]:
            self.deltay += self.vel

        #Check for X AXIS collision
        if not collision[0]:
            self.x += self.deltax
        #Check for Y AXIS collision
        if not collision[1]:
            self.y += self.deltay


    def collision(self):
        x_collide = False
        y_collide = False

        if self.x + self.deltax < 0 or self.x + self.deltax + self.width > self.SCREEN_WIDTH:
            x_collide = True
        else:
            x_collide = False
        if self.y + self.deltay < 0 or self.y + self.deltay + self.height > self.SCREEN_HEIGHT:
            y_collide = True
        else:
            y_collide = False

        return [x_collide, y_collide]

    def attack(self, boat):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            fire_rect = pygame.Rect(self.fire_x, self.fire_y, self.width, self.height)
            boat_rect = pygame.Rect(boat[0], boat[1], boat[2], boat[3])
            if fire_rect.colliderect(boat_rect):
                on_fire = True
                return on_fire


    def draw(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_s]:
            self.win.blit(self.dragon_image_list[self.dragon_image_count // 8], (self.x, self.y))
            self.dragon_image_count += 1
            if self.dragon_image_count >= 16:
                self.dragon_image_count = 0
        else:
            self.win.blit(self.dragon_image_list[0], (self.x, self.y))

        if keys[pygame.K_SPACE]:
            self.fire_x = self.x + self.width
            self.fire_y = self.y + 30
            self.win.blit(self.fire_list[self.fire_count//3], (self.fire_x, self.fire_y))
            self.fire_count += 1
            if self.fire_count >= 6:
                self.fire_count = 0
        #pygame.draw.rect(self.win, BLUE, (self.x, self.y, self.width, self.height))


class Boat:

    def __init__(self, win, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.win = win
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.x = SCREEN_WIDTH + 50
        self.y = SCREEN_HEIGHT - 80
        self.width = 50
        self.height = 50
        self.vel = 2
        self.boat_image = pygame.image.load("./sprites/boat.png")
        self.arrow_image = pygame.image.load('./sprites/arrow.png')
        self.boat_fire_one = pygame.image.load("./sprites/boat_fire_one.png")
        self.boat_fire_two = pygame.image.load("./sprites/boat_fire_two.png")
        self.boat_fire_three = pygame.image.load("./sprites/boat_fire_three.png")
        self.boat_fire_list = [self.boat_fire_one, self.boat_fire_two, self.boat_fire_three]
        self.boat_sink_one = pygame.image.load("./sprites/boat_sink_one.png")
        self.boat_sink_two = pygame.image.load("./sprites/boat_sink_two.png")
        self.boat_sink_list = [self.boat_sink_one, self.boat_sink_two]
        self.boat_fire_count = 0
        self.fire_cycle_count = 0
        self.boat_sink_count = 0
        self.on_fire = False
        self.undamaged = True
        self.burning = False
        self.sinking = False
        self.respawn = False
        #arrow one
        self.arrow_x = self.x
        self.arrow_y = self.y

    def movement(self, playerx):
        if self.undamaged:
            if self.x > playerx + self.width*2:
                self.x -= self.vel
            elif self.x < playerx + self.width*2:
                self.x += self.vel

    def attack(self):
        if not self.sinking:
            if self.arrow_x > 0 and self.arrow_y > 0:
                self.arrow_x -= self.vel*2
                self.arrow_y -= self.vel*2
            else:
                self.arrow_x = self.x
                self.arrow_y = self.y
        
            self.win.blit(self.arrow_image, (self.arrow_x, self.arrow_y))
        

    def draw(self):
        def undamaged(img):
            self.win.blit(img, (self.x, self.y))

        def burning(img_list, boat_img):
            print('burning', self.burning)
            self.undamaged = False
            self.win.blit(boat_img, (self.x, self.y))
            self.win.blit(img_list[self.boat_fire_count // 10], (self.x, self.y))
            self.boat_fire_count += 1
            if self.boat_fire_count >= 30:
                self.boat_fire_count = 0
                self.fire_cycle_count += 1
            elif self.fire_cycle_count > 3:
                print('cycle count')
                self.burning = False
                self.sinking = True
                return
            
        def sinking(img_list):
            print('sinking', self.boat_sink_count)
            self.win.blit(img_list[self.boat_sink_count // 18], (self.x, self.y))
            self.boat_sink_count += 1
            if self.boat_sink_count >= 36:
                self.sinking = False
                self.respawn = True

        def respawn():
            self.x = 1200
            self.undamaged = True
            self.burning = False
            self.sinking = False
            self.respawn = False
            self.boat_fire_count = 0
            self.fire_cycle_count = 0
            self.boat_sink_count = 0



            
        if self.undamaged:
            undamaged(self.boat_image)
        if self.on_fire and self.undamaged:
            self.burning = True
        if self.burning:
            burning(self.boat_fire_list, self.boat_image)
        if self.sinking:
            sinking(self.boat_sink_list)
        if self.respawn:
            respawn()