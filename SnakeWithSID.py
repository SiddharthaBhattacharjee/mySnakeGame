#Modules Imported
import subprocess
import sys
import random
from tkinter import *
from tkinter import messagebox
import webbrowser
import os

try:
    import  mysql.connector as MC
except:
    subprocess.run(['pip','install','mysql-connector-python'])
    import mysql.connector as MC

try:
    import  pygame
except:
    subprocess.run(['pip','install','pygame'])
    import pygame

#****************
try:
    with open("resources/pw.txt", "r") as g:
        pw= g.read()
except:
    pw=input("Enter MySQL Password : ")
    with open("resources/pw.txt", "w") as g:
        g.write(pw)

db="snake"
try:
    mydb = MC.connect(host="localhost",user="root",passwd=pw)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE if not exists snake")
    mydb.close()
except Exception as exc:
    print("Connection failed 1 !")
    print("ERROR : ",exc)
try:
    Con_o = MC.connect(host="localhost",user="root",passwd=pw,database=db)
    if Con_o.is_connected():
        pass

except Exception as e:
    print("Connection Failed !")
    print("ERROR : ",e)
try:
    Cur = Con_o.cursor()
    st = "create table data(name VARCHAR(20) PRIMARY KEY, value INT(11) NOT NULL);"
    Cur.execute(st)
    Con_o.commit()


    Cur = Con_o.cursor()
    st = "insert into data(name,value) values('velocity',8)"
    Cur.execute(st)
    Con_o.commit()


    Cur = Con_o.cursor()
    st = "insert into data(name,value) values('CheatCodes',0)"
    Cur.execute(st)
    Con_o.commit()


    Cur = Con_o.cursor()
    st = "insert into data(name,value) values('snake_colour',1)"
    Cur.execute(st)
    Con_o.commit()


    Cur = Con_o.cursor()
    st = "insert into data(name,value) values('HighScore',0)"
    Cur.execute(st)
    Con_o.commit()
    Con_o.close()
except Exception as e:
    print("Data base found",e)

def data_w(name,value):
    try:
        Con_o = MC.connect(host="localhost",user="root",passwd=pw,database=db)
        if Con_o.is_connected():
            pass

    except Exception as e:
        print("Connection Failed !")
        print("ERROR : ",e)

    Cur = Con_o.cursor()
    st = "UPDATE data SET value = "+str(value)+" WHERE name = '"+str(name)+"';"
    Cur.execute(st)
    Con_o.commit()
    Con_o.close()

def data_r(name):
    try:
        Con_o = MC.connect(host="localhost",user="root",passwd=pw,database=db)
        if Con_o.is_connected():
            pass
    except Exception as e:
        print("Connection Failed !")
        print("ERROR : ",e)

    Cur = Con_o.cursor()
    st = "SELECT value FROM data WHERE name = '"+str(name)+"';"
    Cur.execute(st)
    val = Cur.fetchall()
    Con_o.commit()
    Con_o.close()
    value = (val[0])[0]
    return value


#File Backups
'''
if (not os.path.exists('resources/CheatCodes.txt')):
    with open("resources/CheatCodes.txt", "w") as q:
        q.write("0")

if (not os.path.exists('resources/HighScore.txt')):
    with open("resources/HighScore.txt", "w") as e:
        e.write("0")

if (not os.path.exists('resources/snake_colour.txt')):
    with open("resources/snake_colour.txt", "w") as t:
        t.write("1")

if (not os.path.exists('resources/velocity.txt')):
    with open("resources/velocity.txt", "w") as u:
        u.write("8")
'''


#Global Variables to be changed
'''
with open("resources/velocity.txt", "r") as g:
    init_velocity = int(g.read())

with open("resources/CheatCodes.txt", "r") as h:
    CC = int(h.read())

with open("resources/snake_colour.txt", "r") as i:
    SC = int(i.read())
'''

#New database portion
init_velocity = data_r('velocity')
CC = data_r('CheatCodes')
SC = data_r('snake_colour')

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (102,0,102)
yellow = (255,255,0)
fps = 30
resume = True

#Game specific fungtions

def web(url):
    webbrowser.open(url)


def screen_score(text,color,x,y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def screen_text(text,color,x,y):
    screen_text = s_font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
def screen_title(text,color,x,y):
    screen_text = t_font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snake_list ,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color,[x, y, snake_size, snake_size])

def settings():
    #Global Variables
    global init_velocity
    global CC
    global Con
    global SC

    init_velocity = data_r('velocity')
    CC = data_r('CheatCodes')
    SC = data_r('snake_colour')

    def ResetHS():
        #change
        '''
        if messagebox.askokcancel('CONFIRM','Do you really want to Reset Your Highscore?'):
            with open("resources/HighScore.txt", "w") as f:
                f.write('0')'''
        data_w('HighScore',0) #New database dungtion

    def Restore():
        global init_velocity
        global CC

        if messagebox.askokcancel('CONFIRM','Do you really want to Restore Default Settings?'):

            init_velocity = 8

            #change
            '''
            with open("resources/velocity.txt", "w") as g:
                g.write('8')
            GDV.set(2)

            CC = 0
            with open("resources/CheatCodes.txt", "w") as h:
                h.write('0')
            CCV.set(0)

            with open("resources/snake_colour.txt", "w") as i:
                i.write('1')
            SCV.set(1)'''
            #new database fungtion
            data_w('velocity',8)
            GDV.set(2)
            data_w('CheatCodes',0)
            CCV.set(0)
            data_w('snake_colour',1)
            SCV.set(1)

    def Confirm():
        if messagebox.askokcancel('CONFIRM','Do you want to change the settings?'):
            mode = GDV.get()
            cheat = CCV.get()
            SColor = SCV.get()
            global CC
            global init_velocity

            if mode == 1:
                init_velocity = 4
                '''with open("resources/velocity.txt", "w") as g:
                    g.write('4')'''
                data_w('velocity',4)
            if mode == 2:
                init_velocity = 8
                '''with open("resources/velocity.txt", "w") as g:
                    g.write('8')'''
                data_w('velocity',8)
            if mode == 3:
                '''with open("resources/velocity.txt", "w") as g:
                    g.write('12')'''
                init_velocity = 12
                data_w('velocity',12)

            if cheat == 0:
                CC = 0
                '''with open("resources/CheatCodes.txt", "w") as h:
                    h.write('0')'''
                data_w('CheatCodes',0)
            if cheat == 1:
                CC = 1
                '''with open("resources/CheatCodes.txt", "w") as h:
                    h.write('1')'''
                data_w('CheatCodes',1)

            if SColor == 1:
                '''with open("resources/snake_colour.txt", "w") as i:
                    i.write('1')'''
                data_w('snake_colour',1)
                SC = 1

            if SColor == 2:
                '''with open("resources/snake_colour.txt", "w") as i:
                    i.write('2')'''
                data_w('snake_colour',2)
                SC = 2
            if SColor == 3:
                '''with open("resources/snake_colour.txt", "w") as i:
                    i.write('3')'''
                data_w('snake_colour',3)
                SC = 3
            if SColor == 4:
                '''with open("resources/snake_colour.txt", "w") as i:
                    i.write('4')'''
                data_w('snake_colour',4)
                SC = 4
            if SColor == 5:
                '''with open("resources/snake_colour.txt", "w") as i:
                    i.write('5')'''
                data_w('snake_colour',5)
                SC = 5
            if SColor == 6:
                '''with open("resources/snake_colour.txt", "w") as i:
                    i.write('6')'''
                data_w('snake_colour',6)
                SC = 6


            root.destroy()

    root = Tk()
    root.title("SETTINGS")
    root.configure(bg="Gray55")
    root.geometry("460x380+1000+150")
    root.maxsize(width = 460, height = 380)

    #Radio Variable
    GDV = IntVar()
    if init_velocity == 4:
        GDV.set(1)
    if init_velocity == 8:
        GDV.set(2)
    if init_velocity == 12:
        GDV.set(3)

    CCV = IntVar()
    if CC == 0:
        CCV.set(0)
    if CC == 1:
        CCV.set(1)

    SCV = IntVar() #(colour code R=1, B=2 , G=3, W=4, Y=5, P=6)
    if SC == 1:
        SCV.set(1)
    if SC == 2:
        SCV.set(2)
    if SC == 3:
        SCV.set(3)
    if SC == 4:
        SCV.set(4)
    if SC == 5:
        SCV.set(5)
    if SC == 6:
        SCV.set(6)



    text_0 = Label(root, text= "GAME SETTINGS",bg='Gray55',font=('Helvetica',20,'bold'))
    text_1 = Label(root, text= "Game Difficulty :",bg='Gray55',font=('Helvetica',14,'bold'))
    text_2 = Label(root, text= "Cheat Codes :",bg='Gray55',font=('Helvetica',14,'bold'))
    text_3 = Label(root, text= "High Score :",bg='Gray55',font=('Helvetica',14,'bold'))
    text_4 = Label(root, text= "Snake Colour :",bg='Gray55',font=('Helvetica',14,'bold'))
    text_5 = Label(root, text= "Reset Settings :",bg='Gray55',font=('Helvetica',14,'bold'))
    text_e_1 = Label(root,text='',bg='Gray55')
    text_e_3 = Label(root,text='',bg='Gray55')
    text_e_5 = Label(root,text='',bg='Gray55')
    text_e_7 = Label(root,text='',bg='Gray55')
    text_e_10 = Label(root,text='',bg="Gray55")


    text_0.grid(row=0)

    text_e_1.grid(row=1)
    text_e_3.grid(row=3)
    text_e_5.grid(row=5)
    text_e_7.grid(row=7)
    text_e_10.grid(row=10)

    text_1.grid(row=2,sticky = E)
    text_2.grid(row=4,sticky = E)
    text_3.grid(row=6,sticky = E)
    text_4.grid(row=8,sticky = E)
    text_5.grid(row=11,sticky = E)

    GD_1 = Radiobutton(root,text='Easy',font=('Helvetica',10,'bold'),bg="Gray55",value=1 , variable = GDV)
    GD_2 = Radiobutton(root,text='Normal',font=('Helvetica',10,'bold'),bg="Gray55",value=2 , variable = GDV)
    GD_3 = Radiobutton(root,text='Hard',font=('Helvetica',10,'bold'),bg="Gray55",value=3 , variable = GDV)

    CC_0 = Radiobutton(root,text='Disable',font=('Helvetica',10,'bold'),bg="Gray55",value=0 , variable = CCV)
    CC_1 = Radiobutton(root,text='Enable',font=('Helvetica',10,'bold'),bg="Gray55",value=1 , variable = CCV)

    HSR = Button(root, text="Reset",width=8,height=1,relief=RIDGE,bd=4,command = ResetHS)

    SC_1 = Radiobutton(root,text='Red',font=('Helvetica',10,'bold'),bg="Gray55",value=1 , variable = SCV)
    SC_2 = Radiobutton(root,text='Blue',font=('Helvetica',10,'bold'),bg="Gray55",value=2 , variable = SCV)
    SC_3 = Radiobutton(root,text='Green',font=('Helvetica',10,'bold'),bg="Gray55",value=3 , variable = SCV)
    SC_4 = Radiobutton(root,text='White',font=('Helvetica',10,'bold'),bg="Gray55",value=4 , variable = SCV)
    SC_5 = Radiobutton(root,text='Yellow',font=('Helvetica',10,'bold'),bg="Gray55",value=5 , variable = SCV)
    SC_6 = Radiobutton(root,text='Purple',font=('Helvetica',10,'bold'),bg="Gray55",value=6 , variable = SCV)

    RS = Button(root, text="Restore",width=8,height=1,relief=RIDGE,bd=4,command = Restore)

    Check_button = Button(root, text="CONFIRM",width=8,height=1,relief=RIDGE,bd=4,command=Confirm)

    GD_1.grid(row=2,column=1,sticky=W)
    GD_2.grid(row=2,column=2,sticky=W)
    GD_3.grid(row=2,column=3,sticky=W)

    CC_0.grid(row=4,column=1,sticky=W)
    CC_1.grid(row=4,column=2,sticky=W)

    HSR.grid(row=6,column=1,sticky=W)

    SC_1.grid(row=8,column=1,sticky=W)
    SC_2.grid(row=8,column=2,sticky=W)
    SC_3.grid(row=8,column=3,sticky=W)
    SC_4.grid(row=9,column=1,sticky=W)
    SC_5.grid(row=9,column=2,sticky=W)
    SC_6.grid(row=9,column=3,sticky=W)

    RS.grid(row=11,column=1,sticky=W)

    Check_button.grid(row=14, column=3)




    root.mainloop()


def welcome():
    global black
    exit_game = False
    blink_i = 0
    blink_f = 2
    pygame.mixer.music.load('musics/back.mp3')
    pygame.mixer.music.play(-1)
    while not exit_game:
        mouse = pygame.mouse.get_pos()
        gameWindow.fill(black)
        gameWindow.blit(logo, (0 , int(screen_height/2)-220))
        screen_title('NAKE with SID',white,210,int(screen_height/2)-80)
        gameWindow.blit(settings_logo, (screen_width-50 , 10))
        gameWindow.blit(fb_logo, (20 , screen_height-50))
        gameWindow.blit(gm_logo, (80 , screen_height-50))
        gameWindow.blit(ig_logo, (140, screen_height-50))
        gameWindow.blit(tw_logo, (200, screen_height-50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                root_t = Tk()
                root_t.withdraw()
                if messagebox.askokcancel('QUIT?','Do you really want to QUIT the game?'):
                    pygame.quit()
                    quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    exit_game == True
                    gameloop()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if screen_width-50+40 > mouse[0] > screen_width-50  and 10+40 > mouse[1] > 10:
                        settings()

                    if 20+40 > mouse[0] > 20  and screen_height-50+40 > mouse[1] > screen_height-50:
                        web('https://www.facebook.com/sanjaybhattacharjee.sanju')
                    if 80+40 > mouse[0] > 80  and screen_height-50+40 > mouse[1] > screen_height-50:
                        web('mailto:siddharthabhatt3456@gmail.com')
                    if 140+40 > mouse[0] > 140  and screen_height-50+40 > mouse[1] > screen_height-50:
                        web('https://www.instagram.com/progamersid_x/')
                    if 200+40 > mouse[0] > 200  and screen_height-50+40 > mouse[1] > screen_height-50:
                        web('https://twitter.com/Sanjayb87300198')

        blink_i += 1

        if blink_i == 20:
            blink_f += 1
            blink_i = 0

        if blink_f%2 == 0:
            screen_text("Press Enter to Start Game", white,186,int(screen_height/2))

        pygame.display.update()
        clock.tick(30)



#Game loop
def gameloop():
    #game specific variables
    exit_game = False
    game_over = False
    score = 0
    ka = 1
    #change
    '''
    with open("resources/HighScore.txt", "r") as f:
        highscore = int(f.read())'''
    highscore = data_r('HighScore')

    score_str = "SCORE : 0" + "  HIGHSCORE :" + str(highscore)

    global init_velocity
    global CC
    global white
    global red
    global black
    global green
    global blue
    global purple
    global yellow
    global fps
    global resume

    #colour defining Statement change
    '''
    with open("resources/snake_colour.txt", "r") as i:
        SC_f = int(i.read())'''
    SC_f = data_r('snake_colour')

    if SC_f == 1:
        snake_color = red
        text_color = white
        food_color = green
        sf_color = blue
    if SC_f == 2:
        snake_color = blue
        text_color = white
        food_color = green
        sf_color = red
    if SC_f == 3:
        snake_color = green
        text_color = white
        food_color = blue
        sf_color = red
    if SC_f == 4:
        snake_color =white
        text_color = green
        food_color = blue
        sf_color = red
    if SC_f == 5:
        snake_color = yellow
        text_color = white
        food_color = green
        sf_color = red
    if SC_f == 6:
        snake_color = purple
        text_color = white
        food_color = green
        sf_color = red

    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size=20
    food_size=16
    superfood_size = 22
    SFIT = 0
    SFS = 0
    SF_timer = 300

    food_x = random.randint(26,screen_width-20)
    food_y = random.randint(100,screen_height-100)

    superfood_x = random.randint(30,screen_width-30)
    superfood_y = random.randint(100,screen_height-100)

    #Variables for snake length
    snake_list = []
    snake_length = 1

    pygame.mixer.music.load('musics/start.wav')
    pygame.mixer.music.play()

    #Loop Starting
    while not exit_game:

        if game_over:

            '''with open("resources/HighScore.txt", "w") as f:
                f.write(str(highscore))''' #change
            data_w('HighScore',highscore)

            gameWindow.fill(black)
            screen_title("GAME OVER !", red,140, int(screen_height/2)-70)
            screen_text("Press Enter To Continue", red, 180, int(screen_height/2)-20)
            gameWindow.blit(settings_logo, (screen_width-50 , 10))
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():

                #EXIT EVENT
                if event.type == pygame.QUIT:
                    root_t = Tk()
                    root_t.withdraw()
                    if messagebox.askokcancel('QUIT?','Do you really want to QUIT the game?'):
                        exit_game = True


                #Retry Event
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

                #settings event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if screen_width-50+40 > mouse[0] > screen_width-50  and 10+40 > mouse[1] > 10:
                            settings()
                pygame.display.update()

        elif not resume:
            #pause logic
            while not resume:
                gameWindow.fill(black)
                screen_title("GAME PAUSED", white,120, int(screen_height/2)-80)
                screen_text("Press Enter To RESUME", white, 190, int(screen_height/2)-20)
                gameWindow.blit(settings_logo, (screen_width-50 , 10))
                mouse = pygame.mouse.get_pos()
                for event in pygame.event.get():

                    #EXIT EVENT
                    if event.type == pygame.QUIT:
                        root_t = Tk()
                        root_t.withdraw()
                        if messagebox.askokcancel('QUIT?','Do you really want to QUIT the game?'):
                            resume = True
                            exit_game = True


                    #Retry Event
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            resume = True

                    #settings event
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if screen_width-50+40 > mouse[0] > screen_width-50  and 10+40 > mouse[1] > 10:
                                settings()
                pygame.display.update()


        else:
            for event in pygame.event.get():

                #EXIT EVENT
                if event.type == pygame.QUIT:
                    root_t = Tk()
                    root_t.withdraw()
                    if messagebox.askokcancel('QUIT?','Do you really want to QUIT the game?'):
                        exit_game = True

                # EVENT FOR KEY DOWN
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        if velocity_x >= 0:
                            velocity_x = init_velocity
                            velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        if velocity_x <= 0:
                            velocity_x = -init_velocity
                            velocity_y = 0

                    if event.key == pygame.K_UP:
                        if velocity_y <= 0:
                            velocity_y = -init_velocity
                            velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        if velocity_y >= 0:
                            velocity_y = init_velocity
                            velocity_x = 0
                    #test code wasd
                    if event.key == pygame.K_d:
                        if velocity_x >= 0:
                            velocity_x = init_velocity
                            velocity_y = 0

                    if event.key == pygame.K_a:
                        if velocity_x <= 0:
                            velocity_x = -init_velocity
                            velocity_y = 0

                    if event.key == pygame.K_w:
                        if velocity_y <= 0:
                            velocity_y = -init_velocity
                            velocity_x = 0

                    if event.key == pygame.K_s:
                        if velocity_y >= 0:
                            velocity_y = init_velocity
                            velocity_x = 0
                    #test code wasd/
                    if event.key == pygame.K_ESCAPE:
                        resume = False

                    #cheat codes
                    if CC == 1:

                        if event.key == pygame.K_h:
                            score = highscore

                        if event.key == pygame.K_j:
                            score += 10

                        if event.key == pygame.K_r:
                            food_x = random.randint(26,screen_width-20)
                            food_y = random.randint(80,screen_height-20)

                        if event.key == pygame.K_x:
                            SFIT = 10

                        if event.key == pygame.K_u:
                            if init_velocity>0:
                                init_velocity = init_velocity-2

                        if event.key == pygame.K_v:
                            init_velocity = init_velocity+2

                        if event.key == pygame.K_c:
                            init_velocity = 8

                        if event.key == pygame.K_p:
                            init_velocity = 0

                        if event.key == pygame.K_m:
                            highscore = 0

            #GAME DEFINATIONS
            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x)< 16 and abs(snake_y - food_y)< 16:
                score += 10
                SFIT += 1
                pygame.mixer.music.load('musics/food.wav')
                pygame.mixer.music.play()
                if score > int(highscore):
                    highscore = score
                score_str = "SCORE :" + str(score)+ "  HIGHSCORE :" + str(highscore)
                food_x = random.randint(26,screen_width-20)
                food_y = random.randint(80,screen_height-20)
                snake_length += 5


            if SFIT >= 10:
                SFS = 1
                SFIT = 0

            if abs(snake_x - superfood_x)< 18 and abs(snake_y - superfood_y)< 18 and SFS == 1 and SF_timer>0:
                score += 50
                pygame.mixer.music.load('musics/superfood.wav')
                pygame.mixer.music.play()
                if score > int(highscore):
                    highscore = score
                score_str = "SCORE :" + str(score) + "  HIGHSCORE :" + str(highscore)
                superfood_x = random.randint(30,screen_width-30)
                superfood_y = random.randint(90,screen_height-30)
                SFS=0
                SF_timer=300
                ka = 1


            gameWindow.fill(black)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            #game over logics (before plotting snake)
            if snake_x<4 or snake_x>screen_width-19 or snake_y<4 or snake_y>screen_height-19:
                pygame.mixer.music.load('musics/gameover.wav')
                pygame.mixer.music.play()
                game_over = True

            if head in snake_list[:-1]:
                pygame.mixer.music.load('musics/gameover.wav')
                pygame.mixer.music.play()
                game_over = True


            #pygame.draw.rect(gameWindow, red,[snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, snake_color , snake_list ,snake_size)

            pygame.draw.rect(gameWindow, food_color ,[food_x, food_y, food_size, food_size])

            if SFS == 1 and ka == 1:
                pygame.mixer.music.load('musics/SFappear.wav')
                pygame.mixer.music.play()
                ka = ka-1

            if SFS ==1 and SF_timer>0:
                pygame.draw.rect(gameWindow, sf_color ,[superfood_x, superfood_y, superfood_size, superfood_size])
                screen_score('Timer :',text_color,5,45)
                pygame.draw.rect(gameWindow, text_color,[135, 60, SF_timer , 8])
                SF_timer = SF_timer-2

            if SF_timer == 0 and SFS==1:
                SFS = 0
                SF_timer = 300
                ka = 1
                pygame.mixer.music.load('musics/SFtimeout.wav')
                pygame.mixer.music.play()



        screen_score(score_str,text_color,5,5)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

if __name__ == "__main__":

    #initialising pygame is necessary
    pygame.init()
    pygame.mixer.init()

    #creating window specs
    screen_width = 600
    screen_height = 600
    gameWindow = pygame.display.set_mode((screen_width,screen_height))

    #game title
    pygame.display.set_caption("SnakesWithSid")


    #logos
    logo = pygame.image.load('resources/logo2.png')
    settings_logo = pygame.image.load('resources/settings.jpg')
    fb_logo = pygame.image.load('resources/social_fb.png').convert()
    gm_logo = pygame.image.load('resources/social_gm.png').convert()
    ig_logo = pygame.image.load('resources/social_ig.png').convert()
    tw_logo = pygame.image.load('resources/social_tw.png').convert()

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None,45)
    s_font = pygame.font.SysFont(None,30)
    t_font = pygame.font.Font('freesansbold.ttf', 50)

    welcome()
