import threading
import pyautogui
import keyboard
import time
import os

pickaxe = ""

print("Bu program @Flix tarafindan geliştirilmiştir, iyi kullanimlar.\nÇikmak için 'O'-'o' tuşuna basa bilirsiniz.")
screen_width, screen_height = pyautogui.size()
center_x = screen_width // 2
center_y = screen_height // 2

def select_pickaxe():
    global pickaxe
    pickaxes = ["wooden", "tahta", "tas", "stone", "rock", "iron", "demir", "altin", "gold", "golden", "diamond", "elmas", "netherite"]
    pickaxe_input = input("Lütfen Kazma seç: ")
    if pickaxe_input.lower() in pickaxes:
        print(f"{pickaxe_input.lower()} kazma başarıyla seçildi!")
        pickaxe = str(pickaxe_input.lower())
    else:
        print("Geçerli bir kazma seçin, 'tahta, tas, demir, altin, elmas, netherite'.")
        pickaxe = ""
        return select_pickaxe()

select_pickaxe()

def loop():
    while True:
        global pickaxe
            
        if pickaxe == "wooden".lower() or pickaxe == "tahta".lower():
            seconds = 4.6
        elif pickaxe == "stone".lower() or pickaxe == "rock".lower() or pickaxe == "tas".lower():
            seconds = 2.26
        elif pickaxe == "iron".lower() or pickaxe == "demir".lower():
            seconds = 1.6
        elif pickaxe == "gold".lower() or pickaxe == "golden".lower() or pickaxe == "altin".lower():
            seconds = 0.76
        elif pickaxe == "diamond".lower() or pickaxe == "elmas".lower():
            seconds = 1.3
        elif pickaxe == "netherite".lower():
            seconds = 1.06
        else:
            print("Error!")
            os._exit(0)

        pyautogui.moveTo(x=center_x, y=center_y)
        pyautogui.mouseDown()
        pyautogui.press("a")
        time.sleep(seconds)
        pyautogui.press("d")

def q_pressed():
    while True:
        if keyboard.is_pressed("o"):
            print("Program kapatılıyor...")
            os._exit(0) 

thread_q = threading.Thread(target=q_pressed, daemon=True)
thread_q.start()

loop()
