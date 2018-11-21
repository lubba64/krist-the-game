#imports

import sys, pygame
import time
import world
import os
import random
#pygame setup

size = width, height =  1280, 720
screen = pygame.display.set_mode(size)
black=0,0,0
pygame.init()
window_icon = pygame.image.load("spir_u1.png")
pygame.display.set_icon(window_icon)
#tiles load

#classes

class Tile_screen():
    def __init__(self,x,y,imagenum,c,collision):
        self.collision=collision
        self.x=x
        self.y=y
        self.imnum=int(imagenum)
        self.image=Tiles[self.imnum][2]+".png"
        self.a=pygame.image.load(self.image)
        self.rect=self.a.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y
        self.rect.width=tiledimX
        self.rect.height=tiledimY
    def setanimation(self,e,i):
        if Tiles[e][0]==None:
            tile[i].image=Tiles[e][2]+".png"
        else:
            tile[i].image=str(Tiles[e][Tiles[e][0]+2])+".png"

    def __str__(self):
        return"""
        {0}
        {1}
        {2}
        """.format(self.x,self.y,self.image,)

class Sprite_Screen():
    def __init__(self,x,y,imagenum,moveset,chainnum,animation):
        self.chainnum=chainnum
        self.x=x
        self.y=y
        self.animation=animation
        self.imnum=0
        self.image=Sprites[self.imnum][self.animation]+".png"
        self.a=pygame.image.load(self.image)
        self.rect=self.a.get_rect()
        self.rect.top=y
        self.rect.left=x
        self.moveset=moveset
        self.rect.width=tiledimX
        self.rect.height=tiledimY
    def setanimation(self):
        if Sprites[self.imnum][0]==True:
            self.image=Sprites[self.imnum][self.animation]+".png"
        
    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        for Tile_screen in tile:
            if self.rect.colliderect(Tile_screen.rect) and Tile_screen.collision == "box":
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = Tile_screen.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = Tile_screen.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = Tile_screen.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = Tile_screen.rect.bottom
    def __str__(self):
        return"""
        {0}
        {1}
        {2}
        """.format(self.x,self.y,self.image)

class Title_screen():
    def __init__(self,x,y,imagenum):
        self.x=x
        self.y=y
        self.imnum=int(imagenum)
        self.image=Titlescreen_images[self.imnum]+".png"
        self.a=pygame.image.load(self.image)
        self.rect=self.a.get_rect()
        self.rect.top=y
        self.rect.left=x
    def __str__(self):
        return"""
        {0}
        {1}
        {2}
        """.format(self.x,self.y,self.image)

class player():
    def __init__(self,playerS,playerA,Class,Subclass,race,subrace,level,exp,kills,deaths,skp,copper,silver,gold,platinum,emerald,inventory,buffs,weapon,leggings,breastplate,helm,health,wisdom,speed,detection,power,leader,charge,magic,fortune):
        self.playerS=playerS
        self.playerA=playerA
        self.Class=Class
        self.subclass=Subclass
        self.race=race
        self.subrace=subrace
        self.level=level
        self.exp=exp
        self.kills=kills
        self.deaths=deaths
        self.skp=skp
        self.copper=copper
        self.silver=silver
        self.gold=gold
        self.platinum=platinum
        self.emerald=emerald
        self.inventory=inventory
        self.buffs=buffs
        self.weapon=weapon
        self.leggings=leggings
        self.breastplate=breastplate
        self.helm=helm
        self.health=health
        self.health_bonus=round(self.health/2)
        self.wisdom=wisdom
        self.wisdom_bonus=round(self.wisdom/2)
        self.speed=speed
        self.speed_bonus=round(self.speed/2)
        self.detection=detection
        self.detection_bonus=round(self.detection/2)
        self.power=power
        self.power_bonus=round(self.power/2)
        self.leader=leader
        self.leader_bonus=round(self.leader/2)
        self.charge=charge
        self.charge_bonus=round(self.charge/2)
        self.magic=magic
        self.magic_bonus=round(self.magic/2)
        self.fortune=fortune
        self.fourtune_bonus=round(self.fortune/2)

class weapon():
    def __init__(self,name,prefix,weapon_type,parts,enchantments):
        self.name=name
        self.prefix=prefix
        self.weapon_type=weapon_type
        self.parts=parts
        self.enchantments=enchantments

class enchantment():
    def __init__(self,stat,level):
        self.stat=stat
        self.level=level 

class armor():
    def __init__(self,defense,enchantments):
        self.defense=defense
        self.enchantments=enchantments
class leggings(armor):
    pass
class breastplate(armor):
    pass
class helm(armor):
    pass
#vars

#music vars
current_track=0
music_is_playing=False

#true false mispell
true=True
false=False

# current screen vars
titlescreen=True
gameloop=True
player_in_room=True
settings=False
inventory=False
play=False
gallery=False

# player vars
left,up,down,right=False,False,False,False
charachterRace=0
playeranim=0
lastarrowkeypressed=None
lastXkeypressed=None
lastYkeypressed=None
collidedY=False
collidedX=False

# screen vars
cpuspeed=0
screenW=16
screenH=9
tiledimX=80
tiledimY=80
maxSprites=10
spawnpoint=1
coorscanned=1
scanned_screen=spawnpoint
load_iterator=-1
water_clock=0
animation_speed=10
clock=pygame.time.Clock()
FPS=60
notfoundcollision=False
collision_iterator=0
#lists
#sort: put at the end

#window caption lists

window_captions=("1 2 krist is cool ",
"ever think about bread?",
"ventdrac wants you to play krist",
"not a platformer inc",
"ventdrac made this game all credit to ventdrac",
"play in 1280 720 for best resolution",
"DONT ask about harbor.mp3",
"spir is a cool guy"
)
pygame.display.set_caption("Krist: " + window_captions[random.randint(0,len(window_captions)-1)])


#tile lists
Row_Scanned=[]
tile=[]
Tiles=(
[1,0,"water1","water2","water3","water4"], # 1
[None,1,"brick_azure"],# 2
[None,1,"brick_black"],# 3
[None,1,"brick_blue"],# 4
[None,1,"brick_brown"],# 5
[None,1,"brick_chartreuse"],# 6
[None,1,"brick_cyan"],# 7
[None,1,"brick_gray"],# 8
[None,1,"brick_green"],# 9
[None,1,"brick_mint"],# 10
[None,1,"brick_orange"],# 11
[None,1,"brick_pink"],# 12
[None,1,"brick_red"],# 13
[None,1,"brick_rose"],# 14
[None,1,"brick_sand"],# 15
[None,1,"brick_violate"],# 16
[None,1,"brick_white"],# 17
[None,1,"brick_yellow"],# 18
[None,0,"dirt"],# 19
[None,0,"grass_flux"],# 20
[None,0,"grass_slime"],# 21
[None,0,"grass"],# 22
[None,1,"log"],# 23
[None,0,"path_stone"],# 24
[None,0,"pillar_marble_bottom"],# 25
[None,0,"pillar_marble_center"],# 26
[None,0,"pillar_marble_top"],# 27
[None,0,"sand"],# 28
[None,0,"stone_black"],# 29
[None,0,"stone_brown"],# 30
[None,0,"stone_frost"],# 31
[None,0,"stone_magma"],# 32
[None,0,"stone_pink"],# 33
[None,0,"stone_sand"],# 34
[None,0,"stone"],# 35
[None,0,"tile_marble"],# 36
[None,0,"wall_stone_bottom"],# 37
[None,0,"wall_stone_bottomleft"],# 38
[None,0,"wall_stone_bottomright"],# 39
[None,0,"wall_stone_center"],# 40
[None,0,"wall_stone_left"],# 41
[None,0,"wall_stone_right"],# 42
[None,0,"wall_stone_top"],# 43
[None,0,"wall_stone_topleft"],# 44
[None,0,"wall_stone_topright"],# 45
[None,0,"wall_wood_bottom"],# 46
[None,0,"wall_wood_bottomleft"],# 47
[None,0,"wall_wood_bottomright"],# 48
[None,0,"wall_wood_center"],# 49
[None,0,"wall_wood_left"],# 50
[None,0,"wall_wood_right"],# 51
[None,0,"wall_wood_top"],# 52
[None,0,"wall_wood_topleft"],# 53
[None,0,"wall_wood_topright"],# 54
[None,0,"Null"]) # 55

#sprites lists
loadedsprites=[]
Sprites=(
    [True,"spir_d1","spir_d2","spir_l1","spir_l2","spir_r1","spir_r2","spir_u1","spir_u2","spir_dr1","spir_dr2","spir_lr1","spir_lr2","spir_rr1","spir_rr2","spir_ur1","spir_ur2","spir_i1","spir_i2","spir_i3","spir_i4"],
    [True,'kurkur_d1', 'kurkur_d2', 'kurkur_l1', 'kurkur_l2', 'kurkur_r1', 'kurkur_r2', 'kurkur_u1', 'kurkur_u2', 'kurkur_dr1', 'kurkur_dr2', 'kurkur_lr1', 'kurkur_lr2', 'kurkur_rr1', 'kurkur_rr2', 'kurkur_ur1', 'kurkur_ur2', 'kurkur_i1', 'kurkur_i2', 'kurkur_i3', 'kurkur_i4'],
    [])

#sound lists
noises=("")
backround_noises=("The_Library.mp3","Harbor.mp3","Orphfianias.mp3","Sky_Islands.mp3")

#titlescreen
Titlescreen_images=("background_titlescreen","play","background_settings","background_gallery","background_play")
titlescreen_tiles=[]
settings_tiles=[]
play_tiles=[]
gallery_tiles=[]

#collisions
collision_sprites=("combat","npc","boss")
collision_types=("none","box","circle","rounded_brc","rounded_blc","rounded_trc","rounded_tlc")
#vars with classes
player=player(20,17,0,0,0,0,0,[],[],None,None,None,None,0,0,0,0,0,0,0,0,0)
player2=Sprite_Screen(100,100,17,None,maxSprites+1,17)
#functions

#sorts lists
def sort0(param):
    return param[0]

#moves npcs
def moveset(sprite):
    if sprite.moveset==0: #stationary
        pass
    if sprite.moveset==1: #up and down
        sprite.x+=10
    
#updates in game clocks
def Set_clocks():
    global water_clock,animation_speed,playeranim
    clock.tick(FPS)

    playeranim+=1
    if playeranim>10:
        playeranim=1
    
    animation_speed+=1
    if animation_speed>10:
        animation_speed=0
    if animation_speed==10:
        water_clock+=1

    if water_clock>3:
        water_clock=0
    Tiles[0][0]=water_clock

#checks mouse position and applies button function
def checkpos(titlescreennum,function,screen):
    global titlescreen,settings,play,gallery
    if pygame.mouse.get_pos()[0]>screen[titlescreennum].x and pygame.mouse.get_pos()[1]>screen[titlescreennum].y:
        if pygame.mouse.get_pos()[0]<screen[titlescreennum].rect.width+screen[titlescreennum].x and pygame.mouse.get_pos()[1]<screen[titlescreennum].rect.height+screen[titlescreennum].y:
            if function==0:
                titlescreen=False
            if function==1:
                settings=False
                play=False
                gallery=False
            if function==2:
                settings=True
            if function==3:
                play=True
            if function==4:
                gallery=True

#checks for exit event
def checkforquit():
    global titlescreen,gameloop,gallery,play,inventory,settings,player_in_room
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            titlescreen=False
            gameloop=False
            player_in_room=False
            settings=False
            inventory=False
            play=False
            gallery=False

#reduces code by making tile load for multiple screens more compact
def loadscreen(screenlist):
    for i in range(0,len(screenlist)):
        screenlist[i].a = pygame.image.load(screenlist[i].image)
        screenlist[i].a = pygame.transform.scale(screenlist[i].a,(screenlist[i].rect.width,screenlist[i].rect.height))
        screen.blit(screenlist[i].a,screenlist[i].rect)
    pygame.display.flip()

#title screen and other sub screens

#titlescreen setup
def appendtitlescreen():
    global titlescreen_tiles
    titlescreen_tiles.append(Title_screen(0,0,0))
    titlescreen_tiles.append(Title_screen(576,344,1))
    titlescreen_tiles.append(Title_screen(576,380,1))
    titlescreen_tiles.append(Title_screen(576,416,1))
    titlescreen_tiles.append(Title_screen(576,452,1))

#play screen settup
def appendplay():
    global play_tiles
    play_tiles.append(Title_screen(0,0,4))
    play_tiles.append(Title_screen(5,5,1))

#settings screen settup
def appendsettings():
    global settings_tiles
    settings_tiles.append(Title_screen(0,0,2))
    settings_tiles.append(Title_screen(5,5,1))

#gallery screen settup
def appendgallery():
    global gallery_tiles
    gallery_tiles.append(Title_screen(0,0,3))
    gallery_tiles.append(Title_screen(5,5,1))

appendgallery()
appendplay()
appendsettings()
appendtitlescreen()

while titlescreen:
    #checks for exit event
    checkforquit()

    #loads stuff to screen
    for i in range(0,len(titlescreen_tiles)):
        titlescreen_tiles[i].a = pygame.image.load(titlescreen_tiles[i].image)
        titlescreen_tiles[i].a = pygame.transform.scale(titlescreen_tiles[i].a,(titlescreen_tiles[i].rect.width,titlescreen_tiles[i].rect.height))
        screen.blit(titlescreen_tiles[i].a,titlescreen_tiles[i].rect)
    pygame.display.flip()
    if pygame.mouse.get_pressed()[0]==True:
        checkpos(1,0,titlescreen_tiles)
        checkpos(2,2,titlescreen_tiles)
        checkpos(3,3,titlescreen_tiles)
        checkpos(4,4,titlescreen_tiles)
    while play:
        checkforquit()
        loadscreen(play_tiles)
        if pygame.mouse.get_pressed()[0]==True:
            checkpos(1,1,play_tiles)
    while gallery:
        checkforquit()
        loadscreen(gallery_tiles)
        if pygame.mouse.get_pressed()[0]==True:
            checkpos(1,1,gallery_tiles)
    while settings:
        checkforquit()
        loadscreen(settings_tiles)
        if pygame.mouse.get_pressed()[0]==True:
            checkpos(1,1,settings_tiles)

#screen main
#screen setup
for i in range(0,screenH):
    for e in range(0,screenW):
        tile.append(Tile_screen(e*tiledimX,i*tiledimY,0,0,"none"))
        tile[i].a = pygame.image.load(tile[i].image)
        tile[i].a = pygame.transform.scale(tile[i].a,(tiledimX,tiledimY))
        screen.blit(tile[i].a,tile[i].rect)

#main game loop
while gameloop:

    #sprites load inc
    screen.fill(black)
    loadedsprites=[]
    sprites=open("kristsprites.txt","r")
    spriteslist=sprites.readline().split(" ")
    for i in range(0,maxSprites):
        loadedsprites.append(Sprite_Screen(int(spriteslist[i*5]),int(spriteslist[i*5+1]),spriteslist[i*5+2],spriteslist[i*5+3],i,int(spriteslist[i*5+4])))
    loadedsprites.append(player2)
    sprites.close()

    #load ground tiles
    world.World=open("krist_the_world.txt","r")
    while scanned_screen > coorscanned:
        for z in range(0,screenH):
            world.World.readline()
    for e in range(0,screenH):
        Row_Scanned.clear()
        Row_Scanned=world.World.readline().split(" ")
        Row_Scanned.pop()
        for i in range(0,screenW):
            load_iterator+=1
            tile[load_iterator].imnum = int(Row_Scanned[i])
            if Tiles[int(Row_Scanned[i])][0]==None:
                tile[load_iterator].image=Tiles[int(Row_Scanned[i])][2]+".png"
            else:
                tile[load_iterator].image=Tiles[int(Row_Scanned[i])][Tiles[int(Row_Scanned[i])][0]+1]+".png"
            tile[load_iterator].a = pygame.image.load(tile[load_iterator].image)
            tile[load_iterator].a = pygame.transform.scale(tile[load_iterator].a,(tiledimX,tiledimY))
            tile[load_iterator].collision = collision_types[Tiles[int(Row_Scanned[i])][1]]
            tile[load_iterator].imnum = int(Row_Scanned[i])
    world.World.close()

    #music
    if music_is_playing:
        pygame.mixer.stop()
        music_is_playing=False
    
    #player in room loop
    while player_in_room and gameloop:

        #sets clocks
        Set_clocks()   
        
        #music
        if not music_is_playing:
            music_is_playing=True
            pygame.mixer.music.load(backround_noises[current_track])
            pygame.mixer.music.play()

        #keypresses
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                gameloop=False
                player_in_room=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    up=True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    left=True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    right=True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    down=True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    up=False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    left=False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    right=False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    down=False

        #player movement
        if left:
            loadedsprites[-1].move_single_axis(0-player.playerS,0)
            lastarrowkeypressed="LEFT"
        if right:
            loadedsprites[-1].move_single_axis(player.playerS,0)
            lastarrowkeypressed="RIGHT"
        if up:
            loadedsprites[-1].move_single_axis(0,0-player.playerS)
            lastarrowkeypressed="UP"
        if down:
            loadedsprites[-1].move_single_axis(0,player.playerS)
            lastarrowkeypressed="DOWN"
        
        #player animations
        if down and right or down and left or down:
            if playeranim>0 and playeranim<6:
                player.playerA = 2
            else:
                player.playerA = 1
        if up and right or up and left or up:
            if playeranim>0 and playeranim<6:
                player.playerA=8
            else:
               player.playerA=7
        if right and not down and not up:
            if playeranim>0 and playeranim<6:
                player.playerA=6
            else:
                player.playerA=5
        if left and not down and not up:
            if playeranim>0 and playeranim<6:
                player.playerA=4
            else:
                player.playerA=3
        if not down:
            if lastarrowkeypressed=="DOWN":
                player.playerA=17
        if not up:
            if lastarrowkeypressed=="UP":
                player.playerA=18
        if not right:
            if lastarrowkeypressed=="RIGHT":
                player.playerA=19
        if not left:
            if lastarrowkeypressed=="LEFT":
                player.playerA=20

        #checks for playersprite being at edge
        if loadedsprites[-1].x < 0:
            gameloop=False
            player_in_room=False
        if loadedsprites[-1].x < 0:
            gameloop=False
            player_in_room=False
        if loadedsprites[-1].y + tiledimX > tiledimX*screenW:
            gameloop=False
            player_in_room=False
        if loadedsprites[-1].y + tiledimY > tiledimY*screenH:
            gameloop=False
            player_in_room=False

        loadedsprites[-1].animation=player.playerA
        #updates player sprite to new animations and vars
        #tile display
        for i in range(0,screenW*screenH):
            tile[i].setanimation(tile[i].imnum,i)
            tile[i].a = pygame.image.load(tile[i].image)
            tile[i].a = pygame.transform.scale(tile[i].a,(tiledimX,tiledimY))
            screen.blit(tile[i].a,tile[i].rect)
        
        #sprite display
        b=0
        lowestsprite=Sprite_Screen(0,0,0,0,0,1)
        alreadyloaded=[]
        for i in range(0,maxSprites+1):
            alreadyloaded.append([loadedsprites[i].y,loadedsprites[i].chainnum])
        alreadyloaded.sort(key=sort0)
        for e in range(0,maxSprites+1):
            notfoundmatch=True
            b=0
            while notfoundmatch:
                if alreadyloaded[e][0] == loadedsprites[b].y and alreadyloaded[e][1] == loadedsprites[b].chainnum:
                    lowestsprite=loadedsprites[b]
                    notfoundmatch=False
                b+=1
            moveset(lowestsprite)
            if e==maxSprites:
                loadedsprites[-1].setanimation()
            lowestsprite.a = pygame.image.load(lowestsprite.image)
            lowestsprite.a = pygame.transform.scale(lowestsprite.a,(tiledimX,tiledimY))
            screen.blit(lowestsprite.a,lowestsprite.rect)
        pygame.display.flip()

    load_iterator=0
pygame.quit()