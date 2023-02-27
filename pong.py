import pygame
from time import sleep as zzz
import random

pygame.init()

screen = pygame.display.set_mode((600,400))

player_rect = pygame.Rect(0, 0, 20, 80)
enemy_rect = pygame.Rect(580, 0, 20, 80)
ball_rect = pygame.Rect( 300-20, 200-20, 20, 20)
player_speed = 5
ball_speed = 7
enemy_speed = 5
ball_move = [ball_speed*random.choice([1,-1]), ball_speed*random.choice([1, -1])]

score = 0
enemy_score = 0

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
    
    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and player_rect.y < 320:
        dir = 1
    elif keys[pygame.K_UP] and player_rect.y > 0:
        dir = -1
    else:
        dir = 0
    player_rect = player_rect.move((0, dir*player_speed))

    # Ball Movement, scoring
    if player_rect.colliderect(ball_rect) or ball_rect.x <= 0 or ball_rect.x >= 600-20 or enemy_rect.colliderect(ball_rect):
        ball_move[0] = -ball_move[0]
    if ball_rect.y <= 0 or ball_rect.y >= 400-20:
        ball_move[1] = -ball_move[1]
    if ball_rect.x <= 0:
        enemy_score += 1
        print(score, enemy_score)
    if ball_rect.x >= 580:
        score += 1
        print(score, enemy_score)

    if enemy_score >= 7 or score >= 7:
        pygame.quit()

    ball_rect = ball_rect.move(ball_move)

    # Enemy movement
    if (ball_rect.centery < enemy_rect.centery):
        if enemy_rect.y > 0:
            enemy_rect = enemy_rect.move([0, -enemy_speed])
    elif (ball_rect.centery > enemy_rect.centery):
        if enemy_rect.y < 520:
            enemy_rect = enemy_rect.move([0, enemy_speed])

    # Render
    screen.fill(0)
    pygame.draw.rect(screen, (255,255,255), player_rect)
    pygame.draw.rect(screen, (255,255,255), ball_rect)
    pygame.draw.rect(screen, (255,255,255), enemy_rect)
    
    pygame.display.flip()

    zzz(0.01)