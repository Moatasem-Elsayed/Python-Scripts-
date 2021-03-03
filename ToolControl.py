import tkinter as tk
from tkinter import filedialog  
import os
import pyautogui,time

# def callback():
#     name= fd.askopenfilename() 
#     print(name)
    
# errmsg = 'Error!'
# tk.Button(text='Click to Open File', 
#        command=callback).pack(fill=tk.X)
# tk.mainloop()
def ClickNoTab(num):
    for j in range(1, num):
        pyautogui.keyDown('tab')
        pyautogui.keyUp('tab')

def ClickNoTab(num):
    for j in range(1, num):
        pyautogui.keyDown('tab')
        pyautogui.keyUp('tab')

while True:
    flag=False
    inp=input("Please Type Your TypeCard( factory ,config, init, customer): ")
    name= filedialog.askopenfilename() 
    print(name)
    os.startfile(name)
    time.sleep(2)

    if(str(name).__contains__("FactoryAPP.exe")):
        ClickNoTab(5)
        pyautogui.typewrite("GT")
        ClickNoTab(3)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        flag=True
    elif(str(name).__contains__("PrepaidWaterTestTool.exe")):
        if(str(inp).__contains__("con")):
            pyautogui.hotkey('ctrl', 'tab')
            ClickNoTab(6)
            pyautogui.press('enter')
            pyautogui.press('down')
            pyautogui.press('enter')#select configuration card
            ClickNoTab(5)
            pyautogui.press('enter') #create
            time.sleep(3)
            pyautogui.press('enter')
            ClickNoTab(2)
            pyautogui.press('enter')
            time.sleep(3)
            pyautogui.press('enter') #initizlize
            for i in range(1,4):
                pyautogui.hotkey('ctrl', 'tab')
            ClickNoTab(5)
            pyautogui.press('space')
            ClickNoTab(4)
            pyautogui.press('space')
            ClickNoTab(2)
            pyautogui.press('enter')
            time.sleep(3)
            pyautogui.press('enter') #Set
            flag=True
        elif(str(inp).__contains__("in")):
            pyautogui.hotkey('ctrl', 'tab')
            ClickNoTab(10)
            pyautogui.press('enter') #create Customer Card
            time.sleep(3)
            pyautogui.press('enter') #confirm
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'tab')
            ClickNoTab(10)
            pyautogui.typewrite("GT")
            ClickNoTab(3)
            pyautogui.press('enter')
            time.sleep(3)
            pyautogui.press('enter')
            flag=True
        elif(str(inp).__contains__("cus")):
            pyautogui.hotkey('ctrl', 'tab')
            ClickNoTab(10)
            pyautogui.press('enter') #create Customer Card
            time.sleep(3)
            pyautogui.press('enter') #confirm
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'tab')
            ClickNoTab(10)
            pyautogui.typewrite("GT")
            ClickNoTab(3)
            pyautogui.press('enter')
            time.sleep(3)
            pyautogui.press('enter')
            pyautogui.hotkey('ctrl', 'tab')
            ClickNoTab(10)
            pyautogui.typewrite("10")#swgPrice
            ClickNoTab(2)
            pyautogui.typewrite("15")#swgpercent
            ClickNoTab(3)
            pyautogui.typewrite("150")#monthfees
            ClickNoTab(2)
            pyautogui.typewrite("25")#permeeterfees
            ClickNoTab(2)
            pyautogui.typewrite("36")#monthfees:
            ClickNoTab(7)
            pyautogui.typewrite("45") #l1
            ClickNoTab(3)
            pyautogui.typewrite("90")#l2
            ClickNoTab(11)
            pyautogui.typewrite("135")#l3
            ClickNoTab(3)
            pyautogui.typewrite("180")#l4
            ClickNoTab(3)
            pyautogui.typewrite("225")#l5
            ClickNoTab(3)
            pyautogui.typewrite("270")#l6
            ClickNoTab(3)
            pyautogui.typewrite("315")#l7
            ClickNoTab(4)
            pyautogui.typewrite("360")#l8
            ClickNoTab(8)
            pyautogui.typewrite("405")#l9
            ClickNoTab(4)
            pyautogui.typewrite("450")#l10
            ClickNoTab(3)
            pyautogui.typewrite("495")#l11
            ClickNoTab(2)
            pyautogui.typewrite("540")#l12
            ClickNoTab(12)
            pyautogui.typewrite("585")#l13
            ClickNoTab(2)
            pyautogui.typewrite("630")#l14
            ClickNoTab(2)
            pyautogui.typewrite("675")#l15
            ClickNoTab(2)
            pyautogui.typewrite("1000")#l15
            ClickNoTab(18) 
            pyautogui.press('space') #saturday  
            pyautogui.typewrite("1000")#l15
            ClickNoTab(3) 
            pyautogui.press('space') #Thursdays  
            ClickNoTab(2) 
            pyautogui.press('space') #monday  
            ClickNoTab(5) 
            pyautogui.typewrite('50') #monday
            ClickNoTab(2) 
            pyautogui.alert("Please enter your Charge Number within 3 seconds or\nthe defualt value will be set")  
            time.sleep(3)
            ClickNoTab(2)
            pyautogui.typewrite('15') #warnging
            ClickNoTab(13)
            pyautogui.press('enter') #set
            time.sleep(1)
            pyautogui.press('enter') #confirm

            flag=True
    if( flag == True):
        print("You Successfully Write On Card")
        hold=input("Please if you want to process again press Y ?")
        if(hold =='y' or hold =='Y' ):
            continue
        else:
            break

    else:
        print("Please Try Again")
        hold=input("Please if you want to process again press Y ?")
        if(hold =='y' or hold =='Y' ):
            continue
        else:
            break        

        




                



    
