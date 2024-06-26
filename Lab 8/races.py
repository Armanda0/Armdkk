import random, sys,pygame
pygame.init()
FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 5
ENEMY_STEP = 10
BLACK = (0, 0, 0)
SCORE  = 0
SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # установление экрана
pygame.display.set_caption("Aruka's racer game") #название экрана
clock = pygame.time.Clock()
global NUM_OF_COINS # глобальная переменная для плдсчета кол-во монет
NUM_OF_COINS=0
score_font = pygame.font.SysFont("Verdana", 20) #шрифт для счетчиков
bg = pygame.image.load("AnimatedStreet.png") #background
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 

    def update(self):
        global SCORE
        self.rect.move_ip(0, ENEMY_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
            SCORE += 1 # если энеми проехал всю высоту экрана, это плюс к скору
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)
            #генерирование новой позиции для машины
    def draw(self, surface):
        surface.blit(self.image, self.rect)
# определяет класс для машин их поведекние и отображение на экране

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed() #get the state of all keyboard buttons
        #the first if statements of each of the 2 following blocks of code
        #is so that the player wouldn't leave the playing area we display in the pygame window
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
# определяет класс для игрока отображение и поведение
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('goldcoin.png')
        self.image=pygame.transform.scale(self.image,(25,25))
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0)
    def update(self):
        self.rect.move_ip(0,5)
        if(self.rect.bottom>SCREEN_HEIGHT):
            self.top=0
            self.rect.center=(random.randint(30,350),0)
    def spawn(self):
        self.rect.center=(random.randint(30,350),0)
    def draw(self,surface):
        surface.blit(self.image,self.rect)
        # определяет класс для монет 
P1 = Player()
E1 = Enemy()
C1=Coin()
#обновляет состояние игрока врагов и монет
enemies = pygame.sprite.Group()
enemies.add(E1)
#adding coins to the sprite group
coins=pygame.sprite.Group()
coins.add(C1)

while True: # игровой цикл начинается
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.update()
    C1.update()
    
    if pygame.sprite.spritecollideany(P1, coins):
       NUM_OF_COINS+=1
       C1.spawn() #как только игрок тронул монету, нужно создать новую

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.quit()
        sys.exit()
#проверяет столкновение игрока с монетами и срагами и увеличивает счет и завершает игру при столкновении
    SURF.blit(bg, (0, 0))
    score_img = score_font.render('Number of passing cars: '+str(SCORE), True, BLACK)
    coin_score_img=score_font.render('Number of collected coins: '+str(NUM_OF_COINS),True,BLACK)
    SURF.blit(score_img, (10, 10)) #позиция счетчика машин
    SURF.blit(coin_score_img,(30,30)) #позиция счетчика монет
    E1.draw(SURF)
    P1.draw(SURF)
    C1.draw(SURF)
    pygame.display.update()
    clock.tick(FPS)
    #отображает фон счет и так же количество монет а так жне всехъ врагов игрока и монет на экране
    #обновляет экран и упраляет частотой кад