import pygame
import random

screen = pygame.display.set_mode([1024,512])

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,51,51)
Title_color = (204,255,255)
BLUE = (51,102,204)
pad_width = 1024
pad_height = 512
hero1_width = 47
hero1_height = 47
enemys_width = 47
enemys_height = 47
FPS = 60

def drawObject(obj,x,y):
    global gamepad
    gamepad.blit(obj,(x,y))  

def drawText(text,size,color,x,y):
    sysfont = pygame.font.SysFont("malgungothic",size)
    text_surface = sysfont.render(text,True,color)
    text_rect=text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface,text_rect)

def drawScore(score):
    global gamepad
    
    drawText("점수 : "+ str(score),20,BLACK,900,7)

def drawCastlehit(castle_hitcount):
    global gamepad
    
    drawText("성 내구도 : "+str(castle_hitcount),20,BLACK,80,7)

def pressAnykey():
    waiting = True
    while waiting:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                initGame.running = False
            if event.type == pygame.KEYUP:
                waiting = False
                
def endGame():
    global gamepad,background_music
    
    background_music.stop()
    screen.fill(Title_color)
    drawText("게임 오버",50,RED,pad_width/2,pad_height/4)
    drawText("Score : "+ str(score),20,BLACK,pad_width/2,pad_height*3/5)
    drawText("아무 버튼이나 눌러 다시 시작",15,BLACK,pad_width/2,pad_height*4/5)
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                initGame.running = False
            if event.type == pygame.KEYUP:
                waiting = False
    initGame()

#def endScreen():
    
#    screen.fill(Title_color)
#    drawText("게임 오버",50,RED,pad_width/2,pad_height/4)
#    drawText("Score : "+ str(score),20,BLACK,pad_width/2,pad_height*3/5)
#    drawText("아무 버튼이나 눌러 다시 시작",15,BLACK,pad_width/2,pad_height*4/5)
#    initGame.runnung = True
#    pygame.display.flip()
#    pressAnykey()
        

def title():
    global title_music
    
    screen.fill(Title_color)
    drawText("DEFENCE",50,BLUE,pad_width/2,pad_height/4)
    drawText("방향키로 이동, 왼쪽Ctrl로 공격해서 성을 방어하세요",20, BLACK, pad_width/2,pad_height*3/5)
    drawText("아무 버튼이나 눌러 시작",15,BLACK,pad_width/2,pad_height*4/5)
    title_music = pygame.mixer.Sound('OSS 기말/타이틀.wav')
    title_music.play(-1)
    pygame.display.flip()
    pressAnykey()

def runGame():
    global gamepad, hero1, clock, background
    global enemys, bullet, boom
    global score, shot_sound, title_music, background_music
    
    title_music.stop()
    background_music = pygame.mixer.Sound('OSS 기말/배경음악.wav')
    background_music.play(-1)
    
    isShotEnemy = False
    boom_count = 0
    enemy_hitcount = 0
    castle_hitcount = 5
    score = 0
    
    x = pad_width * 0.1 + 4
    y = pad_height * 0.5 + 1
    
    background_x = 0
    
    bullet_xy = []
    
    #적 위치 조정
    enemys_x = 1006
    enemys_y = random.randrange(0,10) * 50 + 7
    random.shuffle(enemys)
    enemy = enemys[0]
    
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                #캐릭터 조작
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 50
                    if y < 7:
                        y = 7
                elif event.key == pygame.K_DOWN:
                    y += 50
                    if y > 457:
                        y = 457
                elif event.key == pygame.K_LEFT:
                    x -= 50
                    if x < 6:
                        x = 6
                elif event.key == pygame.K_RIGHT:
                    x += 50
                    if x > 206:
                        x = 206
                elif event.key == pygame.K_LCTRL:
                    bullet_x = x + hero1_width
                    bullet_y = y + hero1_height/2
                    bullet_xy.append([bullet_x,bullet_y])
                    pygame.mixer.Sound.play(shot_sound)
                    
        
        gamepad.fill(WHITE)
        
        #배경 그리기
        drawObject(background,background_x,0)
        
        
        # 적이 오는 움직임
        enemys_x -= 3 + (score * 0.1)
        if score == 100:
            castle_hitcount += 1
        
        if enemys_x <= 6:
            castle_hitcount -= 1
            enemys_x = 1006
            enemys_y = random.randrange(0,10) * 50 + 7
            random.shuffle(enemys)
            enemy = enemys[0]
        # 총알 움직임
        if len(bullet_xy) != 0:
            for i, bxy in enumerate(bullet_xy):
                bxy[0]+=15
                bullet_xy[i][0]=bxy[0]
                if bxy[0] >= pad_width:
                    bullet_xy.remove(bxy)
                    
                if bxy[0]>enemys_x:
                    if bxy[1] > enemys_y and bxy[1] < enemys_y + enemys_height:
                        bullet_xy.remove(bxy)
                        enemy_hitcount += 1
                        isShotEnemy = True
                        
                if bxy[0] >=pad_width:
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass
                    
        #캐릭터 그리기
        drawObject(hero1,x,y)
        #적 그리기
        if enemy != None:
            drawObject(enemy,enemys_x,enemys_y)
        #총알 그리기
        if len(bullet_xy) != 0:
            for bx,by in bullet_xy:
                drawObject(bullet,bx,by)
                
        if not isShotEnemy:
            drawObject(enemy,enemys_x,enemys_y)
        else:
            drawObject(enemy,enemys_x,enemys_y)
            drawObject(boom, enemys_x-10,enemys_y-10)
            boom_count += 1
            if boom_count > 10:
                boom_count = 0
                
                if enemy_hitcount > 2:
                    enemys_x = 1006 
                    enemys_y = random.randrange(0,10) * 50 + 7
                    enemy_hitcount = 0
                    score += 1
                isShotEnemy = False
               
        drawScore(score)
        drawCastlehit(castle_hitcount)        
        
        pygame.display.update()
        clock.tick(60)
        
        if castle_hitcount < 1:
            endGame()
            
    pygame.quit()
    quit()


def initGame():
    global gamepad, hero1, clock,background
    global enemys, bullet, boom
    global shot_sound
    
    enemys=[]
    running = True
    
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caption('OSS 기말')
    hero1 = pygame.image.load('OSS 기말/원2.png')
    # hero1 = pygame.transform.scale(hero1,(46,46)) 
    background = pygame.image.load('OSS 기말/격자.png')
    enemys.append(pygame.image.load('OSS 기말/적.png'))
    
    #for i in range(3):
    #    enemys.append(None)
    
    bullet = pygame.image.load('OSS 기말/총알.png')
    boom = pygame.image.load('OSS 기말/폭발.png')
    boom = pygame.transform.scale(boom,(65,65))
    
    shot_sound = pygame.mixer.Sound('OSS 기말/shot.wav')
    
    clock = pygame.time.Clock()
    
    runGame()
    endScreen()

pygame.init()      
title()
initGame()