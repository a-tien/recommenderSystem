import pygame as pg
import os
import time
import win32api

pg.init()

screen = pg.display.set_mode((1024, 640))
path = os.getcwd()
# title
pg.display.set_caption("HoneyMoon Bridge")

# set card
back = pg.image.load(path+"/poke_img/75_94/back.png")
s1 = pg.image.load(path+"/poke_img/75_94/spade_1.png")
s2 = pg.image.load(path+"/poke_img/75_94/spade_2.png")
s3 = pg.image.load(path+"/poke_img/75_94/spade_3.png")
s4 = pg.image.load(path+"/poke_img/75_94/spade_4.png")
s5 = pg.image.load(path+"/poke_img/75_94/spade_5.png")
s6 = pg.image.load(path+"/poke_img/75_94/spade_6.png")
s7 = pg.image.load(path+"/poke_img/75_94/spade_7.png")
s8 = pg.image.load(path+"/poke_img/75_94/spade_8.png")
s9 = pg.image.load(path+"/poke_img/75_94/spade_9.png")
s10 = pg.image.load(path+"/poke_img/75_94/spade_10.png")
s11 = pg.image.load(path+"/poke_img/75_94/spade_11.png")
s12 = pg.image.load(path+"/poke_img/75_94/spade_12.png")
s13 = pg.image.load(path+"/poke_img/75_94/spade_13.png")
h1 = pg.image.load(path+"/poke_img/75_94/heart_1.png")
h2 = pg.image.load(path+"/poke_img/75_94/heart_2.png")
h3 = pg.image.load(path+"/poke_img/75_94/heart_3.png")
h4 = pg.image.load(path+"/poke_img/75_94/heart_4.png")
h5 = pg.image.load(path+"/poke_img/75_94/heart_5.png")
h6 = pg.image.load(path+"/poke_img/75_94/heart_6.png")
h7 = pg.image.load(path+"/poke_img/75_94/heart_7.png")
h8 = pg.image.load(path+"/poke_img/75_94/heart_8.png")
h9 = pg.image.load(path+"/poke_img/75_94/heart_9.png")
h10 = pg.image.load(path+"/poke_img/75_94/heart_10.png")
h11 = pg.image.load(path+"/poke_img/75_94/heart_11.png")
h12 = pg.image.load(path+"/poke_img/75_94/heart_12.png")
h13 = pg.image.load(path+"/poke_img/75_94/heart_13.png")
d1 = pg.image.load(path+"/poke_img/75_94/diamond_1.png")
d2 = pg.image.load(path+"/poke_img/75_94/diamond_2.png")
d3 = pg.image.load(path+"/poke_img/75_94/diamond_3.png")
d4 = pg.image.load(path+"/poke_img/75_94/diamond_4.png")
d5 = pg.image.load(path+"/poke_img/75_94/diamond_5.png")
d6 = pg.image.load(path+"/poke_img/75_94/diamond_6.png")
d7 = pg.image.load(path+"/poke_img/75_94/diamond_7.png")
d8 = pg.image.load(path+"/poke_img/75_94/diamond_8.png")
d9 = pg.image.load(path+"/poke_img/75_94/diamond_9.png")
d10 = pg.image.load(path+"/poke_img/75_94/diamond_10.png")
d11 = pg.image.load(path+"/poke_img/75_94/diamond_11.png")
d12 = pg.image.load(path+"/poke_img/75_94/diamond_12.png")
d13 = pg.image.load(path+"/poke_img/75_94/diamond_13.png")
c1 = pg.image.load(path+"/poke_img/75_94/club_1.png")
c2 = pg.image.load(path+"/poke_img/75_94/club_2.png")
c3 = pg.image.load(path+"/poke_img/75_94/club_3.png")
c4 = pg.image.load(path+"/poke_img/75_94/club_4.png")
c5 = pg.image.load(path+"/poke_img/75_94/club_5.png")
c6 = pg.image.load(path+"/poke_img/75_94/club_6.png")
c7 = pg.image.load(path+"/poke_img/75_94/club_7.png")
c8 = pg.image.load(path+"/poke_img/75_94/club_8.png")
c9 = pg.image.load(path+"/poke_img/75_94/club_9.png")
c10 = pg.image.load(path+"/poke_img/75_94/club_10.png")
c11 = pg.image.load(path+"/poke_img/75_94/club_11.png")
c12 = pg.image.load(path+"/poke_img/75_94/club_12.png")
c13 = pg.image.load(path+"/poke_img/75_94/club_13.png")

# font size
font=pg.font.SysFont('Firacode',14)
s_font=pg.font.SysFont('Firacode',10)
l_font=pg.font.SysFont('Firacode',20)
e_font=pg.font.SysFont('Firacode',60)

# contract final tricks
finalTricks = 1

def cov(s):
    t = {
        '黑桃':'s',
        '紅心':'h',
        '方塊':'d',
        '梅花':'c',
        's':'黑桃',
        'h':'紅心',
        'd':'方塊',
        'c':'梅花',
        }
    return t[s]

def num_cov(s):
    t={
        'Ace':1,
        'K':13,
        'Q':12,
        'J':11,
        '10':10,
        '9':9,
        '8':8,
        '7':7,
        '6':6,
        '5':5,
        '4':4,
        '3':3,
        '2':2
    }
    return t[s]

def main():
    #set pointer///////////
    fin = pg.image.load(path+"/poke_img/fin.png")
    finX = 168
    finY = 585
    # player card /dont need to use finger///
    profile = open(path+'/profile.txt','r')
    player_card=load_pro(profile)
    p_card = player_card
    profile.close()
    # com card
    c_played = 0
    # Top cardimport pygame as pg
import os
import time
import win32api

pg.init()

screen = pg.display.set_mode((1024, 640))
path = os.getcwd()
# title
pg.display.set_caption("HoneyMoon Bridge")

# set card
back = pg.image.load(path+"/poke_img/75_94/back.png")
s1 = pg.image.load(path+"/poke_img/75_94/spade_1.png")
s2 = pg.image.load(path+"/poke_img/75_94/spade_2.png")
s3 = pg.image.load(path+"/poke_img/75_94/spade_3.png")
s4 = pg.image.load(path+"/poke_img/75_94/spade_4.png")
s5 = pg.image.load(path+"/poke_img/75_94/spade_5.png")
s6 = pg.image.load(path+"/poke_img/75_94/spade_6.png")
s7 = pg.image.load(path+"/poke_img/75_94/spade_7.png")
s8 = pg.image.load(path+"/poke_img/75_94/spade_8.png")
s9 = pg.image.load(path+"/poke_img/75_94/spade_9.png")
s10 = pg.image.load(path+"/poke_img/75_94/spade_10.png")
s11 = pg.image.load(path+"/poke_img/75_94/spade_11.png")
s12 = pg.image.load(path+"/poke_img/75_94/spade_12.png")
s13 = pg.image.load(path+"/poke_img/75_94/spade_13.png")
h1 = pg.image.load(path+"/poke_img/75_94/heart_1.png")
h2 = pg.image.load(path+"/poke_img/75_94/heart_2.png")
h3 = pg.image.load(path+"/poke_img/75_94/heart_3.png")
h4 = pg.image.load(path+"/poke_img/75_94/heart_4.png")
h5 = pg.image.load(path+"/poke_img/75_94/heart_5.png")
h6 = pg.image.load(path+"/poke_img/75_94/heart_6.png")
h7 = pg.image.load(path+"/poke_img/75_94/heart_7.png")
h8 = pg.image.load(path+"/poke_img/75_94/heart_8.png")
h9 = pg.image.load(path+"/poke_img/75_94/heart_9.png")
h10 = pg.image.load(path+"/poke_img/75_94/heart_10.png")
h11 = pg.image.load(path+"/poke_img/75_94/heart_11.png")
h12 = pg.image.load(path+"/poke_img/75_94/heart_12.png")
h13 = pg.image.load(path+"/poke_img/75_94/heart_13.png")
d1 = pg.image.load(path+"/poke_img/75_94/diamond_1.png")
d2 = pg.image.load(path+"/poke_img/75_94/diamond_2.png")
d3 = pg.image.load(path+"/poke_img/75_94/diamond_3.png")
d4 = pg.image.load(path+"/poke_img/75_94/diamond_4.png")
d5 = pg.image.load(path+"/poke_img/75_94/diamond_5.png")
d6 = pg.image.load(path+"/poke_img/75_94/diamond_6.png")
d7 = pg.image.load(path+"/poke_img/75_94/diamond_7.png")
d8 = pg.image.load(path+"/poke_img/75_94/diamond_8.png")
d9 = pg.image.load(path+"/poke_img/75_94/diamond_9.png")
d10 = pg.image.load(path+"/poke_img/75_94/diamond_10.png")
d11 = pg.image.load(path+"/poke_img/75_94/diamond_11.png")
d12 = pg.image.load(path+"/poke_img/75_94/diamond_12.png")
d13 = pg.image.load(path+"/poke_img/75_94/diamond_13.png")
c1 = pg.image.load(path+"/poke_img/75_94/club_1.png")
c2 = pg.image.load(path+"/poke_img/75_94/club_2.png")
c3 = pg.image.load(path+"/poke_img/75_94/club_3.png")
c4 = pg.image.load(path+"/poke_img/75_94/club_4.png")
c5 = pg.image.load(path+"/poke_img/75_94/club_5.png")
c6 = pg.image.load(path+"/poke_img/75_94/club_6.png")
c7 = pg.image.load(path+"/poke_img/75_94/club_7.png")
c8 = pg.image.load(path+"/poke_img/75_94/club_8.png")
c9 = pg.image.load(path+"/poke_img/75_94/club_9.png")
c10 = pg.image.load(path+"/poke_img/75_94/club_10.png")
c11 = pg.image.load(path+"/poke_img/75_94/club_11.png")
c12 = pg.image.load(path+"/poke_img/75_94/club_12.png")
c13 = pg.image.load(path+"/poke_img/75_94/club_13.png")

# font size
font=pg.font.SysFont('Firacode',14)
s_font=pg.font.SysFont('Firacode',10)
l_font=pg.font.SysFont('Firacode',20)
e_font=pg.font.SysFont('Firacode',60)

# contract final tricks
finalTricks = 1

def cov(s):
    t = {
        '黑桃':'s',
        '紅心':'h',
        '方塊':'d',
        '梅花':'c',
        's':'黑桃',
        'h':'紅心',
        'd':'方塊',
        'c':'梅花',
        }
    return t[s]

def num_cov(s):
    t={
        'Ace':1,
        'K':13,
        'Q':12,
        'J':11,
        '10':10,
        '9':9,
        '8':8,
        '7':7,
        '6':6,
        '5':5,
        '4':4,
        '3':3,
        '2':2
    }
    return t[s]

def main():
    #set pointer///////////
    fin = pg.image.load(path+"/poke_img/fin.png")
    finX = 168
    finY = 585
    # player card /dont need to use finger///
    profile = open(path+'/profile.txt','r')
    player_card=load_pro(profile)
    p_card = player_card
    profile.close()
    # com card
    c_played = 0
    # Top card
    top_show=0
    # current turn (0 = com's turn, 1 =player's turn)
    turn = 0
    first = 0

    # set selected card
    selectedCard=back
    # check choosed card
    selected = 0
    p_currentLast = back
    # current ace
    while(os.path.getsize('midfile.txt')==0):
        time.sleep(1)
        wait = l_font.render("Loading...", 1, (255,255,255))
        screen.blit(wait, (468, 320))
        pg.display.update()
        continue
    midfile = open(path+'/midfile.txt','r')
    ace = load_turn(midfile)
    midfile.close()
    midfile = open(path+'/midfile.txt','w')
    midfile.write("")
    midfile.close()
    aceTime = 1

    if ace[1] == 's': contract=font.render("Com bid " + ace[0] + " for spade.", 1, (255,255,255))
    elif ace[1] == 'h': contract=font.render("Com bid " + ace[0] + " for heart.", 1, (255,255,255))
    elif ace[1] == 'd': contract=font.render("Com bid " + ace[0] + " for diamond.", 1, (255,255,255))
    elif ace[1] == 'c': contract=font.render("Com bid " + ace[0] + " for club.", 1, (255,255,255))
    elif ace[0] == '0': contractEnd=font.render("The contract has been completed.", 1, (255,255,255))

    pressS=font.render("Pressing 's' bid the contract for spade.", 1, (255,255,255))
    pressH=font.render("Pressing 'h' bid the contract for heart.", 1, (255,255,255))
    pressD=font.render("Pressing 'd' bid the contract for diamond.", 1, (255,255,255))
    pressC=font.render("Pressing 'c' bid the contract for club.", 1, (255,255,255))
    pressX=font.render("Pressing 'x' pass the contract.", 1, (255,255,255))
    # player card position
    p_card_x = [155, 210, 265, 320, 375, 430, 485, 540, 595, 650, 705, 760, 815]
    p_card_y = 500

    c_card_y =40

    p_last = back
    c_last = '-1'
    flag =1

    playStart = 0
    # Loop
    running = True
    while running:
        tricks = returnTricks()
        profile = open(path+'/profile.txt','r')
        cardLeft = open(path+'/cardLeft.txt','r')
        top_num = cardLeft.read()
        cardLeft.close()
        player_card=load_pro(profile)
        p_card = player_card
        profile.close()
        ace_file = open(path+'/ace_file.txt',"a")
        screen.fill((0, 128, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYUP:
                if (event.key == pg.K_s and aceTime==1):
                    if ace[1] =='s':
                        contract=font.render("Player bid " + str(int(ace[0])+1) + " for spade.", 1, (255,255,255))
                        finalTricks = int(ace[0])+1
                        ace = str(int(ace[0])+1)+'s'
                    else:
                        contract=font.render("Player bid " + ace[0] + " for spade.", 1, (255,255,255))
                        finalTricks = int(ace[0])
                        ace = str(ace[0])+'s'
                    aceTime = 0
                    # print(ace)
                    ace_file.write(ace)
                    ace_file.close()

                if (event.key == pg.K_h and aceTime==1):
                    if (ace[1] == 's' or ace[1] == 'h'):
                        contract=font.render("Player bid " + str(int(ace[0])+1) + " for heart.", 1, (255,255,255))
                        finalTricks = int(ace[0])+1
                        ace = str(int(ace[0])+1)+'h'
                    else:
                        contract=font.render("Player bid " + ace[0] + " for heart.", 1, (255,255,255))
                        finalTricks = int(ace[0])
                        ace = str(ace[0])+'h'
                    aceTime = 0
                    # print(ace)
                    ace_file.write(ace)
                    ace_file.close()

                if (event.key == pg.K_d and aceTime==1):
                    if (ace[1] == 'c'):
                        contract=font.render("Player bid " + ace[0] + " for diamond.", 1, (255,255,255))
                        finalTricks = int(ace[0])
                        ace = str(ace[0])+'d'
                    else:
                        contract=font.render("Player bid " + str(int(ace[0])+1) + " for diamond.", 1, (255,255,255))
                        finalTricks = int(ace[0])+1
                        ace = str(int(ace[0])+1)+'d'
                    aceTime = 0
                    # print(ace)
                    ace_file.write(ace)
                    ace_file.close()

                if (event.key == pg.K_c and aceTime==1):
                    contract=font.render("Player bid " + str(int(ace[0])+1) + " for club.", 1, (255,255,255))
                    finalTricks = int(ace[0])+1
                    ace = str(int(ace[0])+1)+'c'
                    aceTime = 0
                    # print(ace)
                    ace_file.write(ace)
                    ace_file.close()

                if (event.key == pg.K_x and aceTime==1):
                    # print('0')
                    finalTricks = -int(ace[0])
                    aceTime = -1
                    ace = '0'
                    ace_file.write(ace)
                    ace_file.close()
                    turn = 1

                if (event.key == pg.K_LEFT and finX > p_card_x[1]):
                    finX -= 55
                    profile = open(path+'/profile.txt','r')
                    player_card=load_pro(profile)
                    p_card = player_card
                    profile.close()
                    # print(p_card)
                if (event.key == pg.K_RIGHT and finX < p_card_x[len(p_card)-1]):
                    finX += 55
                    profile = open(path+'/profile.txt','r')
                    player_card=load_pro(profile)
                    p_card = player_card
                    profile.close()
                    # print(p_card)
                if (event.key == pg.K_RETURN and turn):
                    selected = finX
                    finX = 168
                    # if first>-1: first -= 1
                    printSelectedCard(selected,p_card,p_card_x)
                    selectedCard = returnSelected(selected,p_card,p_card_x)

        error = open(path+'/error_return.txt','r')
        if error.read()=='+':
            error.close()
            if first>-1: first -= 1
            p_currentLast = selectedCard
            error = open(path+'/error_return.txt','w')
            error.write('')
            error.close()
        ace, aceTime, contract= checkAce(ace, aceTime, contract)
        complay = open(path+'/complay.txt','r')
        c_card =str(load_complay(complay))
        complay.close()

        if (len(c_card) != 0 and c_card[0] !='-'):
            c_played = c_card
            turn = 1
            if first<1: first += 1
            complay = open(path+'/complay.txt','w')
            complay.write('')
            complay.close()

        if top_num=='0':
            flag = 0
            playStart+=1
            if(playStart==1): first=0

        if first==0:
            c_currentLast = c_played
            # p_currentLast = selectedCard

        c_lastLabel = s_font.render(" com last played", 1, (255,255,255))
        screen.blit(c_lastLabel, (p_card_x[10]-15, 200))
        screen.blit(trans(str(c_currentLast)), (p_card_x[10], 215))

        p_lastLabel = s_font.render(" player last played", 1, (255,255,255))
        screen.blit(p_lastLabel, (p_card_x[12]-15, 200))
        screen.blit(p_currentLast, (p_card_x[12], 215))

        c_playedCard(str(c_played), first, p_card_x)
        showSeletedCard(selectedCard,p_card,p_card_x,first)

        p_showCard(p_card,p_card_x,p_card_y,tricks)
        c_showCard(len(p_card), p_card_x, c_card_y,tricks)

        top = open(path+'/top.txt','r')
        topCard = str(load_top(top))
        top.close()

        if topCard[0] !='-':
            top_show = topCard

        if top_num == '':
            cardLeft = open(path+'/cardLeft.txt','r')
            top_num = cardLeft.read()
            cardLeft.close()

        if flag>0:
            showTopCard(str(top_show),p_card_x)
        screen.blit(contract, (710, 320))

        if aceTime == 1:
            screen.blit(pressS, (640, 370))
            screen.blit(pressH, (640, 390))
            screen.blit(pressD, (640, 410))
            screen.blit(pressH, (640, 430))
            screen.blit(pressX, (640, 450))

        if aceTime == -1:
            contractEnd=font.render("The contract has been completed.", 1, (255,255,255))
            screen.blit(contractEnd, (700, 340))
            poolCount=font.render(top_num+" cards left", 1, (255,255,255))
            screen.blit(poolCount, (700, 360))

        if tricks[1] == '0':
            if (int(tricks[0])>= finalTricks+6 and finalTricks>0):
                finish=e_font.render("Player Win!", 1, (220, 0, 0), (255,255,255))
                screen.blit(finish, (340, 280))

            elif(int(tricks[0])>= finalTricks+8 and finalTricks<0):
                finish=e_font.render("Player Win!", 1, (220, 0, 0), (255,255,255))
                screen.blit(finish, (340, 280))

            else:
                finish=e_font.render("Com Win!", 1, (0,0 ,220), (255,255,255))
                screen.blit(finish, (340, 280))

        screen.blit(fin, (finX, finY))

        pg.display.update()


# trans card
def trans(card):
    if(len(card)<2): return back
    if(card[len(card)-1] == 's'):
        if(card[0] == '1' and len(card) == 2): return s1
        if(card[0] == '2'): return s2
        if(card[0] == '3'): return s3
        if(card[0] == '4'): return s4
        if(card[0] == '5'): return s5
        if(card[0] == '6'): return s6
        if(card[0] == '7'): return s7
        if(card[0] == '8'): return s8
        if(card[0] == '9'): return s9
        if(card[0] == '1' and card[1] == '0'): return s10
        if(card[0] == '1' and card[1] == '1'): return s11
        if(card[0] == '1' and card[1] == '2'): return s12
        if(card[0] == '1' and card[1] == '3'): return s13

    elif(card[len(card)-1] == 'h'):
        if(card[0] == '1' and len(card) == 2): return h1
        if(card[0] == '2'): return h2
        if(card[0] == '3'): return h3
        if(card[0] == '4'): return h4
        if(card[0] == '5'): return h5
        if(card[0] == '6'): return h6
        if(card[0] == '7'): return h7
        if(card[0] == '8'): return h8
        if(card[0] == '9'): return h9
        if(card[0] == '1' and card[1] == '0'): return h10
        if(card[0] == '1' and card[1] == '1'): return h11
        if(card[0] == '1' and card[1] == '2'): return h12
        if(card[0] == '1' and card[1] == '3'): return h13

    elif(card[len(card)-1] == 'd'):
        if(card[0] == '1' and len(card) == 2): return d1
        if(card[0] == '2'): return d2
        if(card[0] == '3'): return d3
        if(card[0] == '4'): return d4
        if(card[0] == '5'): return d5
        if(card[0] == '6'): return d6
        if(card[0] == '7'): return d7
        if(card[0] == '8'): return d8
        if(card[0] == '9'): return d9
        if(card[0] == '1' and card[1] == '0'): return d10
        if(card[0] == '1' and card[1] == '1'): return d11
        if(card[0] == '1' and card[1] == '2'): return d12
        if(card[0] == '1' and card[1] == '3'): return d13

    elif(card[len(card)-1] == 'c'):
        if(card[0] == '1' and len(card) == 2): return c1
        if(card[0] == '2'): return c2
        if(card[0] == '3'): return c3
        if(card[0] == '4'): return c4
        if(card[0] == '5'): return c5
        if(card[0] == '6'): return c6
        if(card[0] == '7'): return c7
        if(card[0] == '8'): return c8
        if(card[0] == '9'): return c9
        if(card[0] == '1' and card[1] == '0'): return c10
        if(card[0] == '1' and card[1] == '1'): return c11
        if(card[0] == '1' and card[1] == '2'): return c12
        if(card[0] == '1' and card[1] == '3'): return c13

    else: return back

def checkAce (ace, aceTime, contract):
    if (os.path.getsize('midfile.txt')!=0):
        midfile = open(path+'/midfile.txt','r')
        ace = load_turn(midfile)
        midfile.close()

        if ace[0] == '0':
            aceTime = -1
            midfile = open(path+'/midfile.txt','w')
            midfile.write("")
            midfile.close()
            return ace, aceTime, contract

        if ace[1] == 's': contract=font.render("Com bid " + ace[0] + " for spade.", 1, (255,255,255))
        elif ace[1] == 'h': contract=font.render("Com bid " + ace[0] + " for heart.", 1, (255,255,255))
        elif ace[1] == 'd': contract=font.render("Com bid " + ace[0] + " for diamond.", 1, (255,255,255))
        elif ace[1] == 'c': contract=font.render("Com bid " + ace[0] + " for club.", 1, (255,255,255))

        aceTime = 1
        midfile = open(path+'/midfile.txt','w')
        midfile.write("")
        midfile.close()

    return ace, aceTime, contract

# return choosed card
def printSelectedCard(fingerPos, p_card, p_card_x):
    play=open("play.txt","w")
    for i in range(0,12,1):
        if (p_card_x[i] <fingerPos< p_card_x[i+1]):
            # print(p_card[i])
            play.write(p_card[i])
        if p_card_x[12] <fingerPos:
            # print(p_card[12])
            play.write(p_card[12])
            break

def returnSelected(fingerPos, p_card, p_card_x):
    for i in range(0,12,1):
        if (fingerPos > p_card_x[12]):
            return trans(p_card[12])
        if (p_card_x[i] <fingerPos< p_card_x[i+1]):
            return trans(p_card[i])

def showSeletedCard(selectedCard,p_card,p_card_x,first):
    playerPlayed = s_font.render("player played", 1, (255,255,255))
    screen.blit(playerPlayed, (p_card_x[6]-10, 255))
    if first ==1:
        screen.blit(back, (p_card_x[6]-10, 270))
    else:
        screen.blit(selectedCard, (p_card_x[6]-10, 270))

# show player cards
def p_showCard(card,p_card_x,p_card_y,tricks):
    player = font.render("Player", 1, (255,255,255))
    screen.blit(player, (p_card_x[0]-75, p_card_y+50))
    p_trick = font.render(str(tricks[0])+" Trick(s)", 1, (255,255,255))
    screen.blit(p_trick, (p_card_x[0]-95, p_card_y+70))
    for x in range(0,len(card),1):
        screen.blit(trans(card[x]), (p_card_x[x], p_card_y))

# show com cards
def c_showCard(card,p_card_x,c_card_y,tricks):
    com = font.render("Com", 1, (255,255,255))
    screen.blit(com, (p_card_x[12]+90, c_card_y+5))
    c_trick = font.render(str(13-int(tricks[1])-int(tricks[0]))+" Trick(s)", 1, (255,255,255))
    screen.blit(c_trick, (p_card_x[12]+90, c_card_y+25))
    for x in range(12,12-card,-1):
        screen.blit(back, (p_card_x[x], c_card_y))

# show com output
def c_playedCard(card, first,p_card_x):
    comPlayed = s_font.render(" com played", 1, (255,255,255))
    if first==1:
        screen.blit(trans(card), (p_card_x[4], 270))
        screen.blit(comPlayed, (p_card_x[4]-3, 255))
    else:
        screen.blit(back, (p_card_x[4], 270))
        screen.blit(comPlayed, (p_card_x[4]-3, 255))

# show top card
def showTopCard(card, p_card_x):
    s_font=pg.font.SysFont('Firacode',10)
    currentCard = s_font.render(" current card", 1, (255,255,255))
    screen.blit(trans(card), (p_card_x[2], 270))
    screen.blit(currentCard, (p_card_x[2]-5, 255))

def returnTricks():
    tricks = open(path+'/tricks.txt','r')
    row = tricks.read().split(' ')
    return row

def load_pro(profile):
    return [str(num_cov(row[2:-1]))+cov(row[0:2]) for row in profile.readlines()]

def load_complay(complay):
    row = complay.read()
    if row!= '':
        return row[0:-1]
    else :
        return "-1"

def load_turn(turnfile):
    turn = turnfile.read().split()
    if turn[0] == '0': return turn[0]
    return turn[0]+cov(turn[1])

def load_top(top):
    row = top.read()
    if row!= '':
        return str(num_cov(row[2:-1]))+cov(row[0:2])
    else :
        return '-1'


if __name__ == "__main__":
    win32api.ShellExecute(0, 'open', 'final_bridge.exe', '', '', 1)
    complay = open(path+'/complay.txt','w') #,encoding='utf-8'
    complay.write('')
    complay.close()
    top = open(path+'/top.txt','w')
    top.write('')
    top.close()
    play=open(path+"/play.txt","w")
    play.write('')
    play.close()
    tricks = open(path+'/tricks.txt','w')
    tricks.write('0 13')
    tricks.close()
    left = open(path+'/cardLeft.txt','w')
    left.write('')
    left.close()
    cardLeft = open(path+'/cardLeft.txt','w')
    cardLeft.write('26')
    cardLeft.close()
    error = open(path+'/error_return.txt','w')
    error.write('')
    error.close()
    main()

    top_show=0
    # current turn (0 = com's turn, 1 =player's turn)
    turn = 0
    first = 0

    # set selected card
    selectedCard=back
    # check choosed card
    selected = 0
    p_currentLast = back
    # current ace
    while(os.path.getsize('midfile.txt')==0):
        time.sleep(1)
        wait = l_font.render("Loading...", 1, (255,255,255))
        screen.blit(wait, (468, 320))
        pg.display.update()
        continue
    midfile = open(path+'/midfile.txt','r')
    ace = load_turn(midfile)
    print(ace)
    midfile.close()
    midfile = open(path+'/midfile.txt','w')
    #midfile.write("")
    midfile.close()
    aceTime = 1

    if ace[1] == 's': contract=font.render("Com bid " + ace[0] + " for spade.", 1, (255,255,255))
    elif ace[1] == 'h': contract=font.render("Com bid " + ace[0] + " for heart.", 1, (255,255,255))
    elif ace[1] == 'd': contract=font.render("Com bid " + ace[0] + " for diamond.", 1, (255,255,255))
    elif ace[1] == 'c': contract=font.render("Com bid " + ace[0] + " for club.", 1, (255,255,255))
    elif ace[0] == '0': contractEnd=font.render("The contract has been completed.", 1, (255,255,255))

    pressS=font.render("Pressing 's' bid the contract for spade.", 1, (255,255,255))
    pressH=font.render("Pressing 'h' bid the contract for he.", 1, (255,255,255))
    pressD=font.render("Pressing 'd' bid the contract for diamond.", 1, (255,255,255))
    pressC=font.render("Pressing 'c' bid the contract for club.", 1, (255,255,255))
    pressX=font.render("Pressing 'x' pass the contract.", 1, (255,255,255))
    # player card position
    p_card_x = [155, 210, 265, 320, 375, 430, 485, 540, 595, 650, 705, 760, 815]
    p_card_y = 500

    c_card_y =40

    p_last = back
    c_last = '-1'
    flag =1

    playStart = 0
    # Loop
    running = True
    while running:
        tricks = returnTricks()
        profile = open(path+'/profile.txt','r')
        cardLeft = open(path+'/cardLeft.txt','r')
        top_num = cardLeft.read()
        cardLeft.close()
        player_card=load_pro(profile)
        p_card = player_card
        profile.close()
        ace_file = open(path+'/ace_file.txt',"a")
        screen.fill((0, 128, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYUP:
                if (event.key == pg.K_s and aceTime==1):
                    if ace[1] =='s':
                        contract=font.render("Player bid " + str(int(ace[0])+1) + " for spade.", 1, (255,255,255))
                        finalTricks = int(ace[0])+1
                        ace = str(int(ace[0])+1)+'s'
                    else:
                        contract=font.render("Player bid " + ace[0] + " for spade.", 1, (255,255,255))
                        finalTricks = int(ace[0])
                        ace = str(ace[0])+'s'
                    aceTime = 0
                    # print(ace)
                    ace_file.write(ace)
                    ace_file.close()

                if (event.key == pg.K_h and aceTime==1):
                    if (ace[1] == 's' or ace[1] == 'h'):
                        contract=font.render("Player bid " + str(int(ace[0])+1) + " for heart.", 1, (255,255,255))
                        finalTricks = int(ace[0])+1
                        ace = str(int(ace[0])+1)+'h'
                    else:
                        contract=font.render("Player bid " + ace[0] + " for heart.", 1, (255,255,255))
                        finalTricks = int(ace[0])
                        ace = str(ace[0])+'h'
                    aceTime = 0
                    # print(ace)
                    ace_file.write(ace)
                    ace_file.close()

                if (event.key == pg.K_d and aceTime==1):
                    if (ace[1] == 'c'):
                        contract=font.render("Player bid " + ace[0] + " for diamond.", 1, (255,255,255))
                        finalTricks = int(ace[0])
                        ace = str(ace[0])+'d'
                    else:
                        contract=font.render("Player bid " + str(int(ace[0])+1) + " for diamond.", 1, (255,255,255))
                        finalTricks = int(ace[0])+1
                        ace = str(int(ace[0])+1)+'d'
                    aceTime = 0
                    # print(ace)
                    ace_file.write(ace)
                    ace_file.close()

                if (event.key == pg.K_c and aceTime==1):
                    contract=font.render("Player bid " + str(int(ace[0])+1) + " for club.", 1, (255,255,255))
                    finalTricks = int(ace[0])+1
                    ace = str(int(ace[0])+1)+'c'
                    aceTime = 0
                    #print(ace)
                    ace_file.write(ace)
                    ace_file.close()

                if (event.key == pg.K_x and aceTime==1):
                    # print('0')
                    finalTricks = -int(ace[0])
                    aceTime = -1
                    ace = '0'
                    ace_file.write(ace)
                    ace_file.close()
                    turn = 1

                if (event.key == pg.K_LEFT and finX > p_card_x[1]):
                    finX -= 55
                    profile = open(path+'/profile.txt','r')
                    player_card=load_pro(profile)
                    p_card = player_card
                    profile.close()
                    # print(p_card)
                if (event.key == pg.K_RIGHT and finX < p_card_x[len(p_card)-1]):
                    finX += 55
                    profile = open(path+'/profile.txt','r')
                    player_card=load_pro(profile)
                    p_card = player_card
                    profile.close()
                    # print(p_card)
                if (event.key == pg.K_RETURN and turn):
                    selected = finX
                    finX = 168
                    # if first>-1: first -= 1
                    printSelectedCard(selected,p_card,p_card_x)
                    selectedCard = returnSelected(selected,p_card,p_card_x)

        error = open(path+'/error_return.txt','r')
        if error.read()=='+':
            error.close()
            if first>-1: first -= 1
            p_currentLast = selectedCard
            error = open(path+'/error_return.txt','w')
            error.write('')
            error.close()
        ace, aceTime, contract= checkAce(ace, aceTime, contract)
        complay = open(path+'/complay.txt','r')
        c_card =str(load_complay(complay))
        complay.close()

        if (len(c_card) != 0 and c_card[0] !='-'):
            c_played = c_card
            turn = 1
            if first<1: first += 1
            complay = open(path+'/complay.txt','w')
            complay.write('')
            complay.close()

        if top_num=='0':
            flag = 0
            playStart+=1
            if(playStart==1): first=0

        if first==0:
            c_currentLast = c_played
            # p_currentLast = selectedCard

        c_lastLabel = s_font.render(" com last played", 1, (255,255,255))
        screen.blit(c_lastLabel, (p_card_x[10]-15, 200))
        screen.blit(trans(str(c_currentLast)), (p_card_x[10], 215))

        p_lastLabel = s_font.render(" player last played", 1, (255,255,255))
        screen.blit(p_lastLabel, (p_card_x[12]-15, 200))
        screen.blit(p_currentLast, (p_card_x[12], 215))

        c_playedCard(str(c_played), first, p_card_x)
        showSeletedCard(selectedCard,p_card,p_card_x,first)

        p_showCard(p_card,p_card_x,p_card_y,tricks)
        c_showCard(len(p_card), p_card_x, c_card_y,tricks)

        top = open(path+'/top.txt','r')
        topCard = str(load_top(top))
        top.close()

        if topCard[0] !='-':
            top_show = topCard

        if top_num == '':
            cardLeft = open(path+'/cardLeft.txt','r')
            top_num = cardLeft.read()
            cardLeft.close()

        if flag>0:
            showTopCard(str(top_show),p_card_x)
        screen.blit(contract, (710, 320))

        if aceTime == 1:
            screen.blit(pressS, (640, 370))
            screen.blit(pressH, (640, 390))
            screen.blit(pressD, (640, 410))
            screen.blit(pressH, (640, 430))
            screen.blit(pressX, (640, 450))

        if aceTime == -1:
            contractEnd=font.render("The contract has been completed.", 1, (255,255,255))
            screen.blit(contractEnd, (700, 340))
            poolCount=font.render(top_num+" cards left", 1, (255,255,255))
            screen.blit(poolCount, (700, 360))

        if tricks[1] == '0':
            if (int(tricks[0])>= finalTricks+6 and finalTricks>0):
                finish=e_font.render("Player Win!", 1, (220, 0, 0), (255,255,255))
                screen.blit(finish, (340, 280))

            elif(int(tricks[0])>= finalTricks+8 and finalTricks<0):
                finish=e_font.render("Player Win!", 1, (220, 0, 0), (255,255,255))
                screen.blit(finish, (340, 280))

            else:
                finish=e_font.render("Com Win!", 1, (0,0 ,220), (255,255,255))
                screen.blit(finish, (340, 280))

        screen.blit(fin, (finX, finY))

        pg.display.update()


# trans card
def trans(card):
    if(len(card)<2): return back
    if(card[len(card)-1] == 's'):
        if(card[0] == '1' and len(card) == 2): return s1
        if(card[0] == '2'): return s2
        if(card[0] == '3'): return s3
        if(card[0] == '4'): return s4
        if(card[0] == '5'): return s5
        if(card[0] == '6'): return s6
        if(card[0] == '7'): return s7
        if(card[0] == '8'): return s8
        if(card[0] == '9'): return s9
        if(card[0] == '1' and card[1] == '0'): return s10
        if(card[0] == '1' and card[1] == '1'): return s11
        if(card[0] == '1' and card[1] == '2'): return s12
        if(card[0] == '1' and card[1] == '3'): return s13

    elif(card[len(card)-1] == 'h'):
        if(card[0] == '1' and len(card) == 2): return h1
        if(card[0] == '2'): return h2
        if(card[0] == '3'): return h3
        if(card[0] == '4'): return h4
        if(card[0] == '5'): return h5
        if(card[0] == '6'): return h6
        if(card[0] == '7'): return h7
        if(card[0] == '8'): return h8
        if(card[0] == '9'): return h9
        if(card[0] == '1' and card[1] == '0'): return h10
        if(card[0] == '1' and card[1] == '1'): return h11
        if(card[0] == '1' and card[1] == '2'): return h12
        if(card[0] == '1' and card[1] == '3'): return h13

    elif(card[len(card)-1] == 'd'):
        if(card[0] == '1' and len(card) == 2): return d1
        if(card[0] == '2'): return d2
        if(card[0] == '3'): return d3
        if(card[0] == '4'): return d4
        if(card[0] == '5'): return d5
        if(card[0] == '6'): return d6
        if(card[0] == '7'): return d7
        if(card[0] == '8'): return d8
        if(card[0] == '9'): return d9
        if(card[0] == '1' and card[1] == '0'): return d10
        if(card[0] == '1' and card[1] == '1'): return d11
        if(card[0] == '1' and card[1] == '2'): return d12
        if(card[0] == '1' and card[1] == '3'): return d13

    elif(card[len(card)-1] == 'c'):
        if(card[0] == '1' and len(card) == 2): return c1
        if(card[0] == '2'): return c2
        if(card[0] == '3'): return c3
        if(card[0] == '4'): return c4
        if(card[0] == '5'): return c5
        if(card[0] == '6'): return c6
        if(card[0] == '7'): return c7
        if(card[0] == '8'): return c8
        if(card[0] == '9'): return c9
        if(card[0] == '1' and card[1] == '0'): return c10
        if(card[0] == '1' and card[1] == '1'): return c11
        if(card[0] == '1' and card[1] == '2'): return c12
        if(card[0] == '1' and card[1] == '3'): return c13

    else: return back

def checkAce (ace, aceTime, contract):
    if (os.path.getsize('midfile.txt')!=0):
        midfile = open(path+'/midfile.txt','r')
        ace = load_turn(midfile)
        midfile.close()

        if ace[0] == '0':
            aceTime = -1
            midfile = open(path+'/midfile.txt','w')
            midfile.write("")
            midfile.close()
            return ace, aceTime, contract

        if ace[1] == 's': contract=font.render("Com bid " + ace[0] + " for spade.", 1, (255,255,255))
        elif ace[1] == 'h': contract=font.render("Com bid " + ace[0] + " for heart.", 1, (255,255,255))
        elif ace[1] == 'd': contract=font.render("Com bid " + ace[0] + " for diamond.", 1, (255,255,255))
        elif ace[1] == 'c': contract=font.render("Com bid " + ace[0] + " for club.", 1, (255,255,255))

        aceTime = 1
        midfile = open(path+'/midfile.txt','w')
        midfile.write("")
        midfile.close()

    return ace, aceTime, contract

# return choosed card
def printSelectedCard(fingerPos, p_card, p_card_x):
    play=open("play.txt","w")
    for i in range(0,12,1):
        if (p_card_x[i] <fingerPos< p_card_x[i+1]):
            # print(p_card[i])
            play.write(p_card[i])
        if p_card_x[12] <fingerPos:
            # print(p_card[12])
            play.write(p_card[12])
            break

def returnSelected(fingerPos, p_card, p_card_x):
    for i in range(0,12,1):
        if (fingerPos > p_card_x[12]):
            return trans(p_card[12])
        if (p_card_x[i] <fingerPos< p_card_x[i+1]):
            return trans(p_card[i])

def showSeletedCard(selectedCard,p_card,p_card_x,first):
    playerPlayed = s_font.render("player played", 1, (255,255,255))
    screen.blit(playerPlayed, (p_card_x[6]-10, 255))
    if first ==1:
        screen.blit(back, (p_card_x[6]-10, 270))
    else:
        screen.blit(selectedCard, (p_card_x[6]-10, 270))

# show player cards
def p_showCard(card,p_card_x,p_card_y,tricks):
    player = font.render("Player", 1, (255,255,255))
    screen.blit(player, (p_card_x[0]-75, p_card_y+50))
    p_trick = font.render(str(tricks[0])+" Trick(s)", 1, (255,255,255))
    screen.blit(p_trick, (p_card_x[0]-95, p_card_y+70))
    for x in range(0,len(card),1):
        screen.blit(trans(card[x]), (p_card_x[x], p_card_y))

# show com cards
def c_showCard(card,p_card_x,c_card_y,tricks):
    com = font.render("Com", 1, (255,255,255))
    screen.blit(com, (p_card_x[12]+90, c_card_y+5))
    c_trick = font.render(str(13-int(tricks[1])-int(tricks[0]))+" Trick(s)", 1, (255,255,255))
    screen.blit(c_trick, (p_card_x[12]+90, c_card_y+25))
    for x in range(12,12-card,-1):
        screen.blit(back, (p_card_x[x], c_card_y))

# show com output
def c_playedCard(card, first,p_card_x):
    comPlayed = s_font.render(" com played", 1, (255,255,255))
    if first==1:
        screen.blit(trans(card), (p_card_x[4], 270))
        screen.blit(comPlayed, (p_card_x[4]-3, 255))
    else:
        screen.blit(back, (p_card_x[4], 270))
        screen.blit(comPlayed, (p_card_x[4]-3, 255))

# show top card
def showTopCard(card, p_card_x):
    s_font=pg.font.SysFont('Firacode',10)
    currentCard = s_font.render(" current card", 1, (255,255,255))
    screen.blit(trans(card), (p_card_x[2], 270))
    screen.blit(currentCard, (p_card_x[2]-5, 255))

def returnTricks():
    tricks = open(path+'/tricks.txt','r')
    row = tricks.read().split(' ')
    return row

def load_pro(profile):
    return [str(num_cov(row[2:-1]))+cov(row[0:2]) for row in profile.readlines()]

def load_complay(complay):
    row = complay.read()
    if row!= '':
        return row[0:-1]
    else :
        return "-1"

def load_turn(turnfile):
    turn = turnfile.read().split()
    if turn[0] == '0': return turn[0]
    return turn[0]+cov(turn[1])

def load_top(top):
    row = top.read()
    if row!= '':
        return str(num_cov(row[2:-1]))+cov(row[0:2])
    else :
        return '-1'


if __name__ == "__main__":
    win32api.ShellExecute(0, 'open', 'final_bridge.exe', '', '', 1)
    complay = open(path+'/complay.txt','w') #,encoding='utf-8'
    complay.write('')
    complay.close()
    top = open(path+'/top.txt','w')
    top.write('')
    top.close()
    play=open(path+"/play.txt","w")
    play.write('')
    play.close()
    tricks = open(path+'/tricks.txt','w')
    tricks.write('0 13')
    tricks.close()
    left = open(path+'/cardLeft.txt','w')
    left.write('')
    left.close()
    cardLeft = open(path+'/cardLeft.txt','w')
    cardLeft.write('26')
    cardLeft.close()
    error = open(path+'/error_return.txt','w')
    error.write('')
    error.close()
    main()
