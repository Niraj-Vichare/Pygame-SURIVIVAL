import random
import pygame
import time
pygame.init()

window = pygame.display.set_mode([800, 800])
clock=pygame.time.Clock()
current_time=0

power = 20

playerX = 20
playerY = 760
player_movX = 0
player_movY = 0

goalX=random.randint(10,760)
goalY=random.randint(10,760)

orangeX = []
orangeY = []
orange_movX = []
orange_movY = []

for i in range(5):
    orangeX.append(random.randint(10, 700))
    orangeY.append(random.randint(10, 760))
    orange_movX.append(random.choice([.2, .5, .3, 1]))
    orange_movY.append(random.choice([.2, .5, .3, 1]))

enemyX = []
enemyY = []
enemy_movX = []
enemy_movY = []
for i in range(5):
    enemyX.append(random.randint(10, 700))
    enemyY.append(random.randint(10, 760))
    enemy_movX.append(random.choice([.2, .5, .3, 1]))
    enemy_movY.append(random.choice([.2, .5, .3, 1]))

purpleX = []
purpleY = []
purple_movX = []
purple_movY = []
for i in range(5):
    purpleX.append(random.randint(10, 700))
    purpleY.append(random.randint(10, 760))
    purple_movX.append(random.choice([.2, .5, .3, 1]))
    purple_movY.append(random.choice([.2, .5, .3, 1]))

redX = []
redY = []
red_movX = []
red_movY = []
for i in range(5):
    redX.append(random.randint(10, 700))
    redY.append(random.randint(10, 760))
    red_movX.append(random.choice([.2, .5, .3, 1]))
    red_movY.append(random.choice([.2, .5, .3, 1]))

def display():
    ans = pygame.font.Font('C:\Program Files (x86)\Adobe\Reader 11.0\Resource\Font\AdobeArabic-Bold.otf', 32)
    ans = ans.render(str(power), True, (255, 255, 255))
    window.blit(ans, (10, 5))


run = True


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_movX = -1
            if event.key == pygame.K_RIGHT:
                player_movX = 1
            if event.key == pygame.K_UP:
                player_movY = -1
            if event.key == pygame.K_DOWN:
                player_movY = 1

        if event.type == pygame.KEYUP:
            player_movX = 0
            player_movY = 0

    playerX += player_movX
    playerY += player_movY

    current_time=pygame.time.get_ticks()

    player=pygame.draw.rect(window,'blue',rect=[playerX,playerY,20,20])
    goal=pygame.draw.rect(window,'white',rect=[goalX,goalY,30,30])
    if player.colliderect(goal):
        goalX=random.randint(10,760)
        goalY = random.randint(10, 760)
        power+=5


    if playerX<=0:
        playerX=0
    if playerX>=770:
        playerX=770
    if playerY<=0:
        playerY=0
    if playerY>=770:
        playerY=770


    for k in range(5):
        enemyX[k] += enemy_movX[k]
        enemyY[k] += enemy_movY[k]
        orangeX[k] += orange_movX[k]
        orangeY[k] += orange_movY[k]
        purpleX[k] += purple_movX[k]
        purpleY[k] += purple_movY[k]
        redX[k] +=red_movX[k]
        redY[k]+=red_movY[k]



    for j in range(5):
        enemy = pygame.draw.rect(window, "green", rect=[enemyX[j], enemyY[j], 10, 10])
        if enemyX[j] >= 800 or enemyX[j] <= 0:
            enemy_movX[j] *= -1
        if enemyY[j] >= 800 or enemyY[j] <= 0:
            enemy_movY[j] *= -1
        if player.colliderect(enemy):
            power -= 10
            enemyX[j] = random.randint(10, 700)
            enemyY[j] = random.randint(10, 760)

    for p in range(5):
        purple = pygame.draw.rect(window, "purple", rect=[purpleX[p], purpleY[p], 10, 10])
        if purpleX[p] >= 800 or purpleX[p] <= 0:
            purple_movX[p] *= -1
        if purpleY[p] >= 800 or purpleY[p] <= 0:
            purple_movY[p] *= -1
        if player.colliderect(purple):
            power -= 10
            purpleX[p] = random.randint(10, 700)
            purpleY[p] = random.randint(10,780)

    for r in range(5):
        red = pygame.draw.rect(window, "red", rect=[redX[r], redY[r], 10, 10])
        if redX[r] >= 800 or redX[r] <= 0:
            red_movX[r] *= -1
        if redY[r] >= 800 or redY[r] <= 0:
            red_movY[r] *= -1
        if player.colliderect(red):
            power -= 10
            redX[r] = random.randint(10, 700)
            redY[r] = random.randint(10,760)


    for l in range(5):
        orange = pygame.draw.rect(window, "orange", rect=[orangeX[l], orangeY[l], 10, 10])
        if orangeX[l] >= 800 or orangeX[l] <= 0:
            orange_movX[l] *= -1
        if orangeY[l] >= 800 or orangeY[l] <= 0:
            orange_movY[l] *= -1
        if player.colliderect(orange):
            power -= 10
            orangeX[l] = random.randint(10, 700)
            orangeY[l] = random.randint(10,700)





    if power <= 0:
        run = False

    clock.tick(900)
    pygame.display.update()
    window.fill("Black")
