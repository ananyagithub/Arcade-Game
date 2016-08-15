import pygame,sys
from pygame.locals import *

pygame.init()
canvas=pygame.display.set_mode((600,600))
pygame.display.set_caption("Maario")
canvas.fill((0,0,0))
mainClock = pygame.time.Clock()
fps=20

start=pygame.image.load("start.png")
start_r=start.get_rect()
start_r.centerx=300
start_r.centery=300
canvas.blit(start,start_r)

mario=pygame.image.load("maryo.png")
mario_r=mario.get_rect()
mario_r.centerx=25
mario_r.centery=300

dragon=pygame.image.load("dragon.png")
dragon_r=dragon.get_rect()
dragon_r.centerx=550
dragon_r.centery=300

upper=pygame.image.load("cactus_bricks.png")
upper_r=upper.get_rect()
upper_r.centerx=300
upper_r.centery=-50

botter=pygame.image.load("fire_bricks.png")
botter_r=botter.get_rect()
botter_r.centerx=300
botter_r.centery=650

end=pygame.image.load("end.png")
end_r=end.get_rect()
end_r.centerx=300
end_r.centery=300

white=(255,255,255)
font1=pygame.font.SysFont(None,80,True,False)
text="HIGH SCORE !!!!!"
txt=font1.render(text,1,white)
txt_r=txt.get_rect()
txt_r.centerx=300
txt_r.centery=200


font=pygame.font.SysFont(None,20,True,False)
text2="Highscore : "
text1="Score : "
text3="Level : "

txt1=font.render(text1,1,white)
txt2=font.render(text2,1,white)
txt3=font.render(text3,1,white)
txt1_r=txt1.get_rect()
txt2_r=txt2.get_rect()
txt3_r=txt3.get_rect()

txt1_r.topleft=(165,50)
txt2_r.topleft=(255,50)
txt3_r.topleft=(370,50)

run=0
mark=str(run)
marks=font.render(mark,1,white)
marks_r=marks.get_rect()
marks_r.topleft=(220,50)

m=0
mstr=str(m)
maxm=font.render(mstr,1,white)
maxm_r=maxm.get_rect()
maxm_r.topleft=(338,50)

speed=10
new=0

l=1
level=str(l)
lev=font.render(level,1,white)
lev_r=lev.get_rect()
lev_r.topleft=(420,50)

flag=0

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            flag=1
            break
    if flag == 1:
        break

fall=25
pygame.time.set_timer(fall,15000)
up=False
down=False
end1=False
flow=10
fly=True


def die():
    upper_r.centery=upper_r.centery+25
    botter_r.centery=botter_r.centery-25
    txt1_r.top=txt1_r.top+25
    txt2_r.top=txt2_r.top+25
    txt3_r.top=txt3_r.top+25
    marks_r.top=marks_r.top+25
    maxm_r.top=maxm_r.top+25
    lev_r.top=lev_r.top+25
    
    global l
    l=l+1

def callme():
    global end1,up,down,run,l
    end1=False
    up=False
    down=False
    run=0
    l=1
    botter_r.centery=650
    upper_r.centery=-50
    txt1_r.top=50
    txt2_r.top=50
    txt3_r.top=50
    marks_r.top=50
    maxm_r.top=50
    lev_r.top=50
    mario_r.centery=300
    fireList.clear()
    

fireList=[]
shoot=26
pygame.time.set_timer(shoot,900)

pygame.mixer.music.load("d.mp3")
pygame.mixer.music.play(-1,0)

class flames:
    def __init__(self):
        self.fire=pygame.image.load("fireball.png")
        self.fire_r=self.fire.get_rect()
        self.fire_r.centerx=465
        self.fire_r.centery=dragon_r.centery
    def update(self):
        self.fire_r.centerx=self.fire_r.centerx-20
    def collide(self):
        if(self.fire_r.left<=mario_r.right and ((mario_r.top<self.fire_r.bottom<mario_r.bottom) or (mario_r.top<self.fire_r.top<mario_r.bottom)) ):
            return True


while True:
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit() 
                sys.exit()
            elif event.key==K_UP:
                up=True
            elif event.key==K_DOWN:
                down=True
        elif event.type==KEYUP:
            if event.key==K_UP:
                up=False
            elif event.key==K_DOWN:
                down=False
        elif event.type == fall:
            die()
        elif event.type==shoot:
            newflame=flames()
            fireList.append(newflame)
        elif event.type==QUIT:
            pygame.quit()
            sys.exit()
        
            
            
    if up:
        if (mario_r.top <= upper_r.bottom):
            end1=True
        else:
            mario_r.centery=mario_r.centery-speed
    elif down:
        if (mario_r.bottom >= botter_r.top):
            end1=True
        else:
            mario_r.centery=mario_r.centery+speed
    if end1:
        pygame.mixer.music.stop()
        dead=pygame.mixer.Sound("die.mp3")
        dead.play(1,0)
        canvas.fill((0,0,0))
        if (run>m):
            m=run
            z=str(m)
            z1=font1.render(z,1,white)
            z1_r=z1.get_rect()
            z1_r.centerx=300
            z1_r.centery=350
            canvas.blit(z1,z1_r)
            canvas.blit(txt,txt_r)
            pygame.display.update()
            pygame.time.wait(4000)
            canvas.fill((0,0,0))
        canvas.blit(end,end_r)
        pygame.display.update()
        pygame.time.set_timer(fall,0)
        pygame.time.wait(2000)
        while end1:
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    else :
                        pygame.time.set_timer(fall,15000)
                        dead.stop()
                        pygame.mixer.music.play(-1,0)
                        callme()
                elif event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                    
                        
            pygame.display.update()
         
    if fly:
        if (dragon_r.top<=upper_r.bottom):
            fly=False
        else:
            dragon_r.centery=dragon_r.centery-flow       
    else:
        if (dragon_r.bottom>=botter_r.top):
            fly=True
        else:
            dragon_r.centery=dragon_r.centery+flow
    
    canvas.fill((0,0,0))

    for f in fireList:
        flames.update(f)

    for f in fireList:
        if (flames.collide(f)==True):
            end1=True

    for f in fireList:
        if f.fire_r.centerx<=0:
            fireList.remove(f)
    
    mstr=str(m)
    maxm=font.render(mstr,1,white)
    canvas.blit(maxm,maxm_r)

    level=str(l)
    lev=font.render(level,1,white)
    canvas.blit(lev,lev_r)
    
    run=run+1
    mark=str(run)
    marks=font.render(mark,1,(255,255,255))
    canvas.blit(marks,marks_r)

    for f in fireList:
        canvas.blit(f.fire,f.fire_r)

    canvas.blit(txt1,txt1_r)
    canvas.blit(txt2,txt2_r)
    canvas.blit(txt3,txt3_r)
    canvas.blit(mario,mario_r)
    canvas.blit(dragon,dragon_r)
    canvas.blit(upper,upper_r)
    canvas.blit(botter,botter_r)
    
    mainClock.tick(fps)
    pygame.display.update()
pygame.display.update()





    
