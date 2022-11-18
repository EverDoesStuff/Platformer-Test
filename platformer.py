import pygame

WIDTH, HEIGHT = 500, 500
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
GREY = (100,100,100)
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
running = True
PLAYERIMG = pygame.image.load('Platformer Game\player.png')
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 64
PLAYER = pygame.transform.scale(PLAYERIMG,(PLAYER_WIDTH,PLAYER_HEIGHT))
Player = pygame.Rect(10,HEIGHT-PLAYER_HEIGHT-100,PLAYER_WIDTH,PLAYER_HEIGHT)
clock = pygame.time.Clock()
FPS = 60
VEL = 5
JUMPVEL = 120
BLOCKWIDTH, BLOCKHEIGHT = 70, 20
blocks = []

def drawWin():
    WIN.fill(GREY)
    WIN.blit(PLAYER,(Player.x,Player.y))

    block1 = pygame.draw.rect(WIN,BLACK,(50,HEIGHT-100,BLOCKWIDTH,BLOCKHEIGHT))
    block2 = pygame.draw.rect(WIN,BLACK,(200,HEIGHT-200,BLOCKWIDTH,BLOCKHEIGHT))
    block3 = pygame.draw.rect(WIN,BLACK,(350,HEIGHT-250,BLOCKWIDTH,BLOCKHEIGHT))
    block4 = pygame.draw.rect(WIN,BLACK,(300,HEIGHT-320,BLOCKWIDTH,BLOCKHEIGHT))
    blocks.append(block1)
    blocks.append(block2)
    blocks.append(block3)
    blocks.append(block4)

    pygame.display.update() 

def movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        Player.x += VEL
    if keys[pygame.K_a]:
        Player.x -= VEL
    if keys[pygame.K_SPACE]:
        for block in blocks:
            if Player.y+PLAYER_HEIGHT == HEIGHT or Player.colliderect(block):
                Player.y -= JUMPVEL

    for block in blocks:
        if Player.colliderect(block) and PlayerBottom <= block.y + BLOCKHEIGHT and PlayerBottom >= block.y:
            Player.y = block.y - PLAYER_HEIGHT
        
    if PlayerBottom < HEIGHT:
        Player.y += 2

while running:
    clock.tick(FPS)
    PlayerBottom, PlayerRight = Player.y + PLAYER_HEIGHT, Player.x + PLAYER_WIDTH
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    drawWin()
    movement()