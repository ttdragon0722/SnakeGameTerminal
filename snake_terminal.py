import os,random    
from pytimedinput import timedInput
from colorama import Fore, Back, Style

os.system("cls")
WIDTH = 48
HEIGHT = 18
CELLS = []
for i in range(HEIGHT):
    for j in range(WIDTH):
        CELLS.append((j,i))

snake = [(11,5),(10,5),(9,5)]
point = (int,int)

moves = {"up":(0,-1),"down":(0,1),"left":(-1,0),"right":(1,0)}
moving = moves["right"]

score = 0

def map_update():
    for i in CELLS:
        if i in snake:
            print(Style.RESET_ALL + "",end="")  
            print(Fore.GREEN + Style.BRIGHT + "x"+Style.RESET_ALL,end="")
        elif i[0] in (0,WIDTH-1) or i[1] in (0,HEIGHT-1):
            print(Back.RED + "*",end="")
        elif i == point:
            print(Style.RESET_ALL + "",end="")
            print(Fore.CYAN + Style.BRIGHT +"a",end="")
        else:
            print(Style.RESET_ALL + " ",end="")


        #*換行*
        if i[0] == WIDTH-1:
            print(Style.RESET_ALL + "",end="")
            print("")

def snake_update():
    next_head = (snake[0][0]+moving[0],snake[0][1]+moving[1])
    snake.pop(-1)
    snake.insert(0,next_head)

def point_collision():
    global score
    if snake[0] == point:
        new_point()
        score +=1
        snake.append(snake[-1])

def new_point():
    global point
    for body in snake:
        point = (random.randint(1,WIDTH-2),random.randint(1,HEIGHT-2))
        if body == point:
            new_point()
new_point()

def out():
    global game_mode
    if snake[0][0] == 0 or snake[0][0] == WIDTH-1 or snake[0][1] == 0 or snake[0][1] == HEIGHT-1:
        game_mode = "over"

def selfcollision():
    global game_mode
    for body in snake[1::]:
        if body == snake[0]:
            game_mode = "over"
        else:
            pass

game_mode = "ready"

while True :
    
    if game_mode == "ready":
        map_update()
        print(Style.RESET_ALL + "",end="")
        commond = input("input"+Fore.YELLOW +" go "+Style.RESET_ALL+"to start the game!  \ninput"+Fore.YELLOW +" quit "+Style.RESET_ALL+"to quit the game! \n\nHelp:\nuse"+Fore.YELLOW +" w a s d "+Style.RESET_ALL+"to move\nyou can press"+Fore.YELLOW +" q "+Style.RESET_ALL+"to quit the game.")
        if commond == "go":
            game_mode = "gaming"
        if commond == "quit":
            print(Fore.MAGENTA + Style.BRIGHT + "BYEBYE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + Style.RESET_ALL)
            break
        os.system("cls")

    if game_mode == "gaming":
        os.system("cls")
        print(Fore.YELLOW + str(score))
        print(Style.RESET_ALL + "",end="")
        map_update()
        snake_update()
        point_collision()
        out()

        text,_= timedInput(timeout=0.3)
        
        match text:
            case 'w' :moving = moves["up"]
            case 'a' :moving = moves["left"]
            case 's' :moving = moves["down"]
            case 'd' :moving = moves["right"]
            case 'q' :
                print(Fore.MAGENTA + Style.BRIGHT + "BYEBYE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + Style.RESET_ALL)
                break

    if game_mode == "over":
        os.system("cls")
        map_update()
        print(Style.RESET_ALL + "",end="")
        commond = input(Fore.MAGENTA+Style.BRIGHT+"HAHA YOU LOSE!!"+Style.RESET_ALL+"\nInput"+Fore.YELLOW+" go "+Style.RESET_ALL+"to restart\n or input"+Fore.YELLOW +" quit "+Style.RESET_ALL+"to quit the game!")
        if commond == "go":
            new_point()
            moving = moves["right"]
            snake = [(11,5),(10,5),(9,5)]
            score = 0
            game_mode = "gaming"
        elif commond == "quit":
            print(Fore.MAGENTA + Style.BRIGHT + "BYEBYE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + Style.RESET_ALL)
            break