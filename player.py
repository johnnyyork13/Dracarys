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
        self.dragon_one = pygame.image.load("dragon_one.png")
        self.dragon_two = pygame.image.load("dragon_two.png")
        self.dragon_image_list = [self.dragon_one, self.dragon_two]
        self.dragon_image_count = 0
        self.fire_one = pygame.image.load("fire_one.png")
        self.fire_two = pygame.image.load("fire_two.png")
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

    def attack(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.fire_x = self.x + self.width
            self.fire_y = self.y + 30
            self.win.blit(self.fire_list[self.fire_count//3], (self.fire_x, self.fire_y))
            self.fire_count += 1
            if self.fire_count >= 6:
                self.fire_count = 0


    def draw(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_s]:
            self.win.blit(self.dragon_image_list[self.dragon_image_count // 8], (self.x, self.y))
            self.dragon_image_count += 1
            if self.dragon_image_count >= 16:
                self.dragon_image_count = 0
        else:
            self.win.blit(self.dragon_image_list[0], (self.x, self.y))
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
        self.boat_image = pygame.image.load("boat.png")
        self.arrow_image = pygame.image.load('arrow.png')
        self.boat_fire_one = pygame.image.load("boat_fire_one.png")
        self.boat_fire_two = pygame.image.load("boat_fire_two.png")
        self.boat_fire_three = pygame.image.load("boat_fire_three.png")
        self.boat_fire_list = [self.boat_fire_one, self.boat_fire_two, self.boat_fire_three]
        self.fire_count = 0
        self.on_fire = False
        self.burning = False
        #arrow one
        self.arrow_x = self.x
        self.arrow_y = self.y

    def movement(self, playerx):
        if self.x > playerx + self.width*2:
            self.x -= self.vel
        elif self.x < playerx + self.width*2:
            self.x += self.vel

    def attack(self):
        if self.arrow_x > 0 and self.arrow_y > 0:
            self.arrow_x -= self.vel*2
            self.arrow_y -= self.vel*2
        else:
            self.arrow_x = self.x
            self.arrow_y = self.y
    
        self.win.blit(self.arrow_image, (self.arrow_x, self.arrow_y))
        

    def draw(self):
        if self.on_fire:
            self.burning = True
        if self.burning:
            self.win.blit(self.boat_fire_list[self.fire_count // 12], (self.x, self.y))
            self.fire_count += 1
            if self.fire_count >= 36:
                self.fire_count = 0

        self.win.blit(self.boat_image, (self.x, self.y))
