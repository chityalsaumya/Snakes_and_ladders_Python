from turtle import textinput
from matplotlib.text import Text
import pygame
from random import randint
import time
import mysql.connector
import pygame_textinput
pygame.init()
from threading import Timer
mydb= mysql.connector.connect(host='localhost',database='Players',user='root',password='')

# Create TextInput-object
def inputfield(num) :
    global playerName1
    # global playerName2
    # global playerName3
    # global playerName4
    textinput1 = pygame_textinput.TextInputVisualizer()
    # textinput2 = pygame_textinput.TextInputVisualizer()
    # textinput3 = pygame_textinput.TextInputVisualizer()
    # textinput4 = pygame_textinput.TextInputVisualizer()

    screen = pygame.display.set_mode((w,h),pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    while True:
        screen.fill((225, 225, 225))

        events = pygame.event.get()
        

        # Feed it with events every frame
        textinput1.update(events)
        # textinput2.update(events)
        # textinput3.update(events)
        # textinput4.update(events)
        # Blit its surface onto the screen
        screen.blit(menubg,(0,0))
        mouse=pygame.mouse.get_pos()
        button("Your name",mouse[0],mouse[1],490,300,200,60,red,b_red,30,50)
        button("        ",mouse[0],mouse[1],490,390,200,60,green,b_green,30,50)
        button("Back",mouse[0],mouse[1],100,100,200,50,red,b_red,30,1)
        if(num == 1):
            playerName1 = textinput1.value
            screen.blit(textinput1.surface,(500,400))
            button("Submit",mouse[0],mouse[1],600,600,200,50,green,b_green,30,21)
            # play(21)
        # elif(num == 2):
        #     playerName1 = textinput1.value
        #     playerName2 = textinput2.value
        #     screen.blit(textinput1.surface,(500,300))
        #     screen.blit(textinput2.surface,(500,400))
        #     button("Submit",mouse[0],mouse[1],600,600,200,50,green,b_green,30,22)
           
        # elif(num == 3):
        #     playerName1 = textinput1.value
        #     playerName2 = textinput2.value
        #     playerName3 = textinput3.value
        #     screen.blit(textinput1.surface,(500,300))
        #     # screen.blit(textinput2.surface,(500,400))
        #     # screen.blit(textinput3.surface,(500,500))
        #     button("Submit",mouse[0],mouse[1],600,600,200,50,green,b_green,30,23)
        #     # play(3)
        # else:
            
        #     playerName1 = textinput1.value
        #     # playerName2 = textinput2.value
        #     # playerName3 = textinput3.value
        #     # playerName4 = textinput4.value
        #     screen.blit(textinput1.surface,(500,200))
        #     screen.blit(textinput2.surface,(500,300))
        #     screen.blit(textinput3.surface,(500,400))
        #     screen.blit(textinput4.surface,(500,500))
        #     button("Submit",mouse[0],mouse[1],600,600,200,50,green,b_green,30,24)
        #     # play(4)
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        pygame.display.update()
        clock.tick(30)


clock=pygame.time.Clock()

#Initialize
pygame.init()
w=1366
h=768

icon=pygame.image.load("icon.jpg")
GD=pygame.display.set_mode((w,h),pygame.FULLSCREEN)
pygame.display.set_caption("Snakes N Ladders")
pygame.display.set_icon(icon)
pygame.display.update()

#Graphics:
black=(10,10,10)
white=(250,250,250)
red= (200,0,0)
b_red=(240,0,0)
green=(0,200,0)
b_green=(0,230,0)
blue=(0,0,200)
grey=(50,50,50)
yellow=(150,150,0)
purple=(43,3,132)
b_purple=(60,0,190)

board= pygame.image.load("Snakes-and-Ladders-Bigger.jpg")
dice1=pygame.image.load("Dice1.png")
dice2=pygame.image.load("Dice2.png")
dice3=pygame.image.load("Dice3.png")
dice4=pygame.image.load("Dice4.png")
dice5=pygame.image.load("Dice5.png")
dice6=pygame.image.load("Dice6.png")
newdice=pygame.image.load("newdice.gif")
redgoti=pygame.image.load("redgoti.png")
yellowgoti=pygame.image.load("yellowgoti.png")
greengoti=pygame.image.load("greengoti.png")
bluegoti=pygame.image.load("bluegoti.png")
menubg=pygame.image.load("snake_bg.jpg")
p=pygame.image.load("playbg.jpg")
intbg=pygame.image.load("welcome_bg.jpg")
intbg2=pygame.image.load("bg2.jpg")
intbg3=pygame.image.load("bg3.jpg")
intbg4=pygame.image.load("bg4.jpg")
intbg5=pygame.image.load("bg5.jpg")


pygame.mixer.music.load("music.wav")
snakesound=pygame.mixer.Sound("snake.wav")
win=pygame.mixer.Sound("win.wav")
lose=pygame.mixer.Sound("lose.wav")
ladder=pygame.mixer.Sound("ladder.wav")

#mouse pos
mouse=pygame.mouse.get_pos()
click=pygame.mouse.get_pressed()


#Message displaying for buttons
def message_display(text,x,y,fs):
    largeText = pygame.font.Font('freesansbold.ttf',fs)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    GD.blit(TextSurf, TextRect)

def text_objects(text, font):
    textSurface = font.render(text, True,white)
    return textSurface, textSurface.get_rect()

#Message displaying for field
def message_display1(text,x,y,fs,c):
    largeText = pygame.font.Font('freesansbold.ttf',fs)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (x,y)
    GD.blit(TextSurf, TextRect)
    

def text_objects1(text, font,c):
    textSurface = font.render(text, True,c)
    return textSurface, textSurface.get_rect()

#Goti movement function
def goti(a):
    l1=[[406,606],[456,606],[506,606],[556,606],[606,606],[656,606],[706,606],[756,606],[806,606],[856,606],[906,606],[906,560],[856,560],[806,560],[756,560],[706,560],[656,560],[606,560],[556,560],[506,560],[456,560],[456,506],[506,506],[556,506],[606,506],[656,506],[706,506],[756,506],[806,506],[856,506],[906,506],[906,460],[856,460],[806,460],[756,460],[706,460],[656,460],[606,460],[556,460],[506,460],[456,460],[456,406],[506,406],[556,406],[606,406],[656,406],[706,406],[756,406],[806,406],[856,406],[906,406],[906,360],[856,360],[806,360],[756,360],[706,360],[656,360],[606,360],[556,360],[506,360],[456,360],[456,306],[506,306],[556,306],[606,306],[656,306],[706,306],[756,306],[806,306],[856,306],[906,306],[906,260],[856,260],[806,260],[756,260],[706,260],[656,260],[606,260],[556,260],[506,260],[456,260],[456,206],[506,206],[556,206],[606,206],[656,206],[706,206],[756,206],[806,206],[856,206],[906,206],[906,160],[856,160],[806,160],[756,160],[706,160],[656,160],[606,160],[556,160],[506,160],[456,160]]
    l2=l1[a]
    x=l2[0]-25
    y=l2[1]-25
    return x,y
     

def text_objects1(text, font):
    textSurface = font.render(text, True,black)
    return textSurface, textSurface.get_rect()

#Ladder check
def ladders(x):
    if x==1: return 38
    elif x==4:return 14
    elif x==9:return 31
    elif x==28:return 84
    elif x==21:return 42
    elif x==51:return 67
    elif x==80:return 99
    elif x==72:return 91
    else:return x

#Snake Check
def snakes(x): 
    if x==17:return 7
    elif x==54:return 34
    elif x==62:return 19
    elif x==64:return 60
    elif x==87:return 36
    elif x==93:return 73
    elif x==95: return 75
    elif x==98: return 79
    else:return x

def dice(a):
    if a==1:
        a=dice1
    elif a==2:
        a=dice2
    elif a==3:
        a=dice3
    elif a==4:
        a=dice4
    elif a==5:
        a=dice5
    elif a==6:
        a=dice6

    time=pygame.time.get_ticks()
    dicerolling(a)
    GD.blit(a,(300,300))
    while pygame.time.get_ticks()-time<1500:
        pygame.display.update()    

#for mute and unmute    
def button2(text,xmouse,ymouse,x,y,w,h,i,a,fs):
    #mouse pos
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            return True
        
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)    
    
    

#Buttons for playing:
def button1(text,xmouse,ymouse,x,y,w,h,i,a,fs):
    #mouse pos
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            return True
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)
    

#Turn
def turn(score,l,s):
    
    a=randint(1,6)#player dice roll
    if a==6:
        six=True
    else:
        six=False
    p=dice(a)
    score+=a
    if score<=100:
        lad=ladders(score) #checking for ladders for player
        if lad!=score:
            l=True
            pygame.mixer.Sound.play(ladder)
            time=pygame.time.get_ticks()
            score=lad 
        snk=snakes(score)
        if snk!=score: #checking for snakes for player
            s=True
            pygame.mixer.Sound.play(snakesound)
            score=snk
           
    else: #checks if player score is not grater than 100
        score-=a
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<1500:
            message_display1("Can't move!",650,50,35,black)
            pygame.display.update()
    return score,l,s,six
    

#Quitting:
def Quit():
    pygame.quit()
    quit()

#Buttons:
def button(text,xmouse,ymouse,x,y,w,h,i,a,fs,b):
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            if b==1:
                options()
            elif b==5:
                return 5
            elif b==0:
                Quit()
          
            elif b=="s" or b==2 or b==3 or b==4:
                return b
            elif b==7:
                options()
            elif b==21:
                play(21)
            elif b==22:
                play(2)
            elif b==23:
                play(3)
            elif b==24:
                play(4)  
              
            else :return True
                   
            
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)


def dicerolling(a):
    time=pygame.time.get_ticks()
    # while pygame.time.get_ticks()-time<150:
    #     GD.blit(a,(300,300))
    #     pygame.display.update()
    while True:
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<50:    
            GD.blit(dice5,(300,300))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<50:
            GD.blit(dice3,(300,300))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<50:
            GD.blit(dice6,(300,300))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<50:
            GD.blit(dice1,(300,300))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<50:
            GD.blit(dice6,(300,300))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<50:    
            GD.blit(dice2,(300,300))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<50:
            GD.blit(dice1,(300,300))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<50:
            GD.blit(dice1,(300,300))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<50:
            GD.blit(dice6,(300,300))
            pygame.display.update()
        for event in pygame.event.get():
            return
        pygame.display.update()
   


def intro():
    time=pygame.time.get_ticks()
    while pygame.time.get_ticks()-time<500:
        GD.blit(intbg,(0,0))
        pygame.display.update()
    while True:
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:    
            GD.blit(intbg2,(0,0))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:
            GD.blit(intbg3,(0,0))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:
            GD.blit(intbg4,(0,0))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:
            GD.blit(intbg5,(0,0))
            pygame.display.update()
            
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                return
        pygame.display.update()


    
#Main Menu
def main():
        
    pygame.mixer.music.play(-1)

    
    menu=True
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Quit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    Quit()

        #mouse pos
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        GD.blit(menubg,(0,0))
        button("Play",mouse[0],mouse[1],(w/2-100),h/2,200,100,green,b_green,60,1)

        button("Quit",mouse[0],mouse[1],(w/2-100),(h/2)+200,200,100,red,b_red,60,0)

        mouse=pygame.mouse.get_pos()
        if button2("Mute Music",mouse[0],mouse[1],1166,0,200,50,purple,b_purple,25):
            pygame.mixer.music.pause()
        if button2("Play Music",mouse[0],mouse[1],1166,75,200,50,purple,b_purple,25):
            pygame.mixer.music.unpause()
        
        
        pygame.display.update()


#Options Menu:
def options():
    flag=True
    while flag==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Quit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    Quit()


        #mouse pos
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        b1=b2=b3=b4=b5=-1
        GD.blit(menubg,(0,0))
        #Single player button
        b1=button("Single Player",mouse[0],mouse[1],(w/2-150),250,300,50,green,b_green,30,"s")
        #2 player button
        b2=button("2 Players",mouse[0],mouse[1],(w/2)-150,350,300,50,green,b_green,30,2)
        #3 player
        b3=button("3 Players",mouse[0],mouse[1],(w/2)-150,450,300,50,green,b_green,30,3)
        #4 player
        b4=button("4 Players",mouse[0],mouse[1],(w/2)-150,550,300,50,green,b_green,30,4)
        #Back button
        b5=button("Back",mouse[0],mouse[1],0,650,200,50,red,b_red,30,5)
        if b5==5:
            main()
        if b1=="s":
            # play(21)
            inputfield(1)
        if b2==2:
            play(2)
            # inputfield(2)
        if b3==3:
            play(3)
            # inputfield(3)
        if b4==4:
            play(4)
            # inputfield(4)
        
        pygame.display.update()


def play(b):
    b6=-1
    time=3000
    if b6==7:
        options()
    GD.blit(p,(0,0))
    GD.blit(board,(w/2-250,h/2-250))
    xcr=xcy=xcg=xcb=406-25
    ycr=ycy=ycg=ycb=606-25
    GD.blit(redgoti,(xcy,ycy))
    if 5>b>1 or b==21:
        GD.blit(yellowgoti,(xcy,ycy))
            
    if 5>b>2 or b==21:
        GD.blit(greengoti,(xcg,ycg))
            
    if 5>b>2:
        GD.blit(bluegoti,(xcb,ycb))
    p1="Player 1"
    p1score=0
    if b==21:
        p2="Computer"
        p2score=0
    if 5>b>1:
        p2="Player 2"
        p2score=0
    if 5>b>2:
        p3="Player 3"
        p3score=0
    if 5>b>3:
        p4="Player 4"
        p4score=0
    t=1
    play=True
    while True:
        l=False
        s=False
        time=3000
        GD.blit(p,(0,0))
        GD.blit(board,(w/2-250,h/2-250))
        mouse=pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    Quit()

            
        if b==21:
            #(player,score,text,xmouse,ymouse,x,y,w,h,i,a,fs)
            # global playerName1
            if button1(playerName1,mouse[0],mouse[1],100,700,200,50,red,grey,30):
                if t==1:
                    p1score,l,s,six=turn(p1score,l,s)
                    message_display1("Six, play again",650,450,50,white)-time<1500
                    
                    if not six:
                        
                        t+=1
                    xcr,ycr=goti(p1score)
                    if p1score==100:
                        time=pygame.time.get_ticks()
                        mycursor = mydb.cursor()
                        sqlform = "INSERT into users(full_name,Status) values(%s,%s)"
                        player = [(playerName1, 'Won')]
                        mycursor.executemany(sqlform, player)
                        mydb.commit()
                        while pygame.time.get_ticks()-time<3000:
                            message_display1(playerName1,650,450,50,white)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                            
                        break
                    
            
            if button1("Computer",mouse[0],mouse[1],400,700,200,50,yellow,grey,30):
                if t==2:
                    p2score,l,s,six=turn(p2score,l,s)
                    message_display1("Six, play again",650,450,50,white)-time<1500
                    xcy,ycy=goti(p2score)
                    if not six:
                        t+=1
                        if b<3 or b==21:
                            t=1
                    
                    if p2score==100:
                        time=pygame.time.get_ticks()
                        mycursor = mydb.cursor()
                        sqlform = "INSERT into users(full_name,Status) values(%s,%s)"
                        player = [("Computer", "Won")]
                        mycursor.executemany(sqlform, player)
                        mydb.commit()
                        while pygame.time.get_ticks()-time<5000:
                            message_display1("Computer Wins",650,450,50,white)
                            pygame.mixer.Sound.play(lose)
                            pygame.display.update()
                        break
        if 5>b>1:
            if button1("Player1",mouse[0],mouse[1],100,700,200,50,red,grey,30):
                if t==1:
                 
                    p1score,l,s,six=turn(p1score,l,s)
                    message_display1("Six, play again",650,450,50,white)-time<1500
                    xcr,ycr=goti(p1score)
                    if not six:
                        t+=1
                    if p1score==100:
                        time=pygame.time.get_ticks()
                        mycursor = mydb.cursor()
                        sqlform = "INSERT into users(full_name,Status) values(%s,%s)"
                        player = [("Player1", 'Won')]
                        mycursor.executemany(sqlform, player)
                        mydb.commit()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 1 Wins",650,450,50,white)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
                
            if button1("Player2",mouse[0],mouse[1],400,700,200,50,yellow,grey,30):
                if t==2:
                    p2score,l,s,six=turn(p2score,l,s)
                    message_display1("Six, play again",650,450,50,white)-time<1500
                    xcy,ycy=goti(p2score)
                    if not six:
                        t+=1
                        if b<3:
                            t=1
                    
                    if p2score==100:
                        time=pygame.time.get_ticks()
                        mycursor = mydb.cursor()
                        sqlform = "INSERT into users(full_name,Status) values(%s,%s)"
                        player = [("Player2", 'Won')]
                        mycursor.executemany(sqlform, player)
                        mydb.commit()
                        while pygame.time.get_ticks()-time<5000:
                            message_display1("Player2 Wins",650,450,50,white)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
                
        if 5>b>2:
            if button1("Player3",mouse[0],mouse[1],700,700,200,50,green,grey,30):
                if t==3:
                    p3score,l,s,six=turn(p3score,l,s)
                    message_display1("Six, play again",650,450,50,white)-time<1500
                    xcg,ycg=goti(p3score)
                    if not six:
                        t+=1
                        if b<4:
                            t=1
                    
                    if p3score==100:
                        time=pygame.time.get_ticks()
                        mycursor = mydb.cursor()
                        sqlform = "INSERT into users(full_name,Status) values(%s,%s)"
                        player = [("Player3", 'Won')]
                        mycursor.executemany(sqlform, player)
                        mydb.commit()
                        while pygame.time.get_ticks()-time<5000:
                            message_display1("Player3 Wins",650,450,50,white)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
                
        if 5>b>3:   
            if button1("Player4",mouse[0],mouse[1],1000,700,200,50,blue,grey,30):
                if t==4:
                    p4score,l,s,six=turn(p4score,l,s)
                    xcb,ycb=goti(p4score)
                    if not six:
                        t+=1
                        if b<5:
                            t=1
                    
                    if p4score==100:
                        time=pygame.time.get_ticks()
                        mycursor = mydb.cursorscore()
                        sqlform = "INSERT into users(full_name,Status) values(%s,%s)"
                        player = [("Player4", 'Won')]
                        mycursor.executemany(sqlform, player)
                        mydb.commit()
                        while pygame.time.get_ticks()-time<5000:
                            message_display1("Player4 Wins",650,450,50,white)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break

        
        b6=button("Back",mouse[0],mouse[1],0,0,200,50,red,b_red,30,7)
        GD.blit(redgoti,(xcr,ycr))
        if 5>b>1 or b==21:
            GD.blit(yellowgoti,(xcy+2,ycy))
            
            
        if 5>b>2:
            GD.blit(greengoti,(xcg+4,ycg))
            
             
        if 5>b>3:
            GD.blit(bluegoti,(xcb+6,ycb))
            
        if l:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<1500:
                message_display1("There's a Ladder!",650,450,70,white)
                pygame.display.update()
        if s:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<1500:
                message_display1("There's a Snake!",650,450,70,red)
                pygame.display.update()

        clock.tick(7)
        pygame.display.update()
        
            
        
intro()    
main()
