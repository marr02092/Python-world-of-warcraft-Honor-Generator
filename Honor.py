import pygame, time, pyautogui,random,subprocess,os
from pygame.locals import *

error=0

#functions

#releases the spirit of the dead character
def freespirit():
    time.sleep(0.5)
    switchtowindow("Generator1")
    time.sleep(0.25)
    pyautogui.moveTo(510,190)
    pyautogui.click()
    time.sleep(2.5)
    #checking for error
    if pyautogui.pixelMatchesColor(450,150,(255,255,255))is True:
        os.system("start WoWShortcut.exe.lnk")
        time.sleep(8)
        pyautogui.write("username")
        time.sleep(0.2)
        pyautogui.press("tab")
        pyautogui.write("password")
        time.sleep(0.2)
        pyautogui.press("enter")
        error=1
    time.sleep(1)
    

def killit():
    time.sleep(0.5)
    switchtowindow("Honor maker")
    time.sleep(0.25)
    pyautogui.click(500,500)
    time.sleep(0.2)
    pyautogui.press("space")
    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(0.3)
    for i in range(0,5):
        pyautogui.press("num2")
        time.sleep(2)

    #checking for error
    if pyautogui.pixelMatchesColor(450,150,(255,255,255))is True:
        os.system("start WoWShortcut.exe.lnk")
        time.sleep(8)
        pyautogui.write("febrero02092")
        time.sleep(0.2)
        pyautogui.press("tab")
        pyautogui.write("marr02092978580")
        time.sleep(0.2)
        pyautogui.press("enter")
        error=1
    
#this function is in charge of changing between game windows
def switchtowindow(window):

    if window=="Honored":
        subprocess.call("cscript switchtohonored.vbs")
        time.sleep(0.35)
        pyautogui.click(500,500)
    elif window=="Generator1":
        subprocess.call("cscript switchtogenerator1.vbs")
        time.sleep(0.35)
        pyautogui.click(500,500)
    else:
        print("No window with that name")
    time.sleep(0.25)
    #checking for error
    if pyautogui.pixelMatchesColor(450,150,(255,255,255))is True:
        os.system("start WoWShortcut.exe.lnk")
        time.sleep(8)
        pyautogui.write("UserName")
        time.sleep(0.2)
        pyautogui.press("tab")
        pyautogui.write("password")
        time.sleep(0.2)
        pyautogui.press("enter")
        error=1
        
    

def logout():
    time.sleep(0.25)
    pyautogui.press("f10")
    time.sleep(0.5)
    pyautogui.press("space")
    time.sleep(3)
    pyautogui.press("esc")
    time.sleep(0.1)
    pyautogui.moveTo(510,410)
    pyautogui.click()
    time.sleep(3)
    #checking for error
    if pyautogui.pixelMatchesColor(450,150,(255,255,255))is True:
        os.system("start WoWShortcut.exe.lnk")
        time.sleep(8)
        pyautogui.write("UserName")
        time.sleep(0.2)
        pyautogui.press("tab")
        pyautogui.write("Password")
        time.sleep(0.2)
        pyautogui.press("enter")
        error=1

def enter_and_teleport():
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.3)
    #this waits until the loading screen is gone and then presses ESCAPE
    while True:
        #checking for error
        if pyautogui.pixelMatchesColor(450,150,(255,255,255))is True:
            os.system("start WoWShortcut.exe.lnk")
            time.sleep(8)
            pyautogui.write("UserName")
            time.sleep(0.2)
            pyautogui.press("tab")
            pyautogui.write("Password")
            time.sleep(0.2)
            pyautogui.press("enter")
            error=1

        print("in loading screen")
        if not pyautogui.pixelMatchesColor(870,231,(173,160,131)):
            break
        
        
        
    time.sleep(10)
    print("Closing Video")
    pyautogui.press("esc")
    time.sleep(1.5)
    print("teleporting")
    pyautogui.press("f9")
    time.sleep(3)
    pyautogui.press("space")
    time.sleep(0.5)

def delete_char():
    pyautogui.click(500,500)
    time.sleep(1)
  
    pyautogui.moveTo(810,722)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.write("delete")
    time.sleep(0.2)
    pyautogui.press("enter")
    #checking for error
    if pyautogui.pixelMatchesColor(450,150,(255,255,255))is True:
        os.system("start WoWShortcut.exe.lnk")
        time.sleep(8)
        pyautogui.write("UserName")
        time.sleep(0.2)
        pyautogui.press("tab")
        pyautogui.write("Password")
        time.sleep(0.2)
        pyautogui.press("enter")

def create_char():
    
    def click_till_write_name():    
        time.sleep(2)
        pyautogui.moveTo(880,620)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(180,217)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(85,525)
        pyautogui.click()

    def delete_name():
        print("deleting name")
        time.sleep(0.1)
        pyautogui.press("esc")
        time.sleep(0.2)
        pyautogui.press("esc")
        time.sleep(1)
        
#this function generates random names until it finds one that's not in use
    def write_name():
        name=[]
            
        def generate_random_letter():
            return chr(random.randint(97,122))
        #generating random name
        current=0
        while len(name)<12:
            if len(name)>0:
                letter=generate_random_letter()
                if letter != str(name[current-1]):
                    name.append(letter)
                    current=current+1
                    #print(current)
            else:
                name.append(generate_random_letter())
                current=current+1
            #print(name)
        name="".join(map(str,name))
        time.sleep(0.1)
        pyautogui.write(name)
        #pyautogui.write("pepe")
        time.sleep(0.1)
        pyautogui.press("enter")

    while True:
        click_till_write_name()
        write_name()
        time.sleep(3)
        print(pyautogui.pixelMatchesColor(463,394,(105, 1, 1)))
        if  (pyautogui.pixelMatchesColor(463,394,(105, 1, 1)) is False)and(pyautogui.pixelMatchesColor(463,394,(105, 0, 0))is False)and(pyautogui.pixelMatchesColor(463,394,(106, 0, 0))is False)and(pyautogui.pixelMatchesColor(463,394,(106, 1, 1))is False) :
            print(" name is available :D")
            break
        print("name used")
        time.sleep(0.2)
        delete_name()
        time.sleep(0.2)
        if (pyautogui.pixelMatchesColor( 819, 91,( 153, 119, 0)) is True):
            print("this thing is crazy, said it's used but created it")
            break
    
        
    

#pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('python')
pygame.mouse.set_visible(1)



#this part is the order everything is done and where functions are called
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == K_0:
                pygame.quit()
            if event.key == K_9:
                for i in range(0,101):
                    print("doing the number ", i)
                    switchtowindow("Generator1")
                    time.sleep(0.5)
                    pyautogui.click(500,500)
                    delete_char()
                    if error==2:
                        break
                    if error==1:
                        error=0
                        continue
                    create_char()
                    if error==1:
                        error=0
                        continue
                    enter_and_teleport()
                    if error==1:
                        error=0
                        continue
                    killit()
                    if error==1:
                        error=0
                        continue
                    freespirit()
                    if error==1:
                        error=0
                        continue
                    logout()
                    if error==1:
                        error=0
                        continue
                    if pyautogui.pixelMatchesColor(1000,300,(172,90,126))is True:
                        i=101
                    
         
                
                
                
                
                
                

