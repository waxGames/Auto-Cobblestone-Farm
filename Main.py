import threading
import pyautogui
import keyboard
import time
import json
import os

pick_time = ""
lang = ""

def lang_select():
    global lang
    lang_selec = input("Pls select langs[tr, en, ru]: ")
    lang_ = lang_selec.lower()
    if lang_ == "ru":
        lang = "ru"
    elif lang_ == "en":
        lang = "en"
    elif lang_ == "tr":
        lang = "tr"
    else:
        print("Please select valid lang.")
        return lang_select()
    
lang_select()

with open(f"langs/{lang}.json", "r", encoding="utf-8") as file:
    lang_data = json.load(file)

print(lang_data["creator_message"])
screen_width, screen_height = pyautogui.size()
center_x = screen_width // 2
center_y = screen_height // 2

def select_pickaxe():
    global pick_time
    with open("pickaxes.json", "r", encoding="utf-8") as file:
        pick_data = json.load(file)

    pickaxes = pick_data[lang]

    while True:
        pickaxe_input = input("Lütfen Kazma seç: ").lower()
        for pick in pickaxes:
            if pickaxe_input in pick["type"]:
                pick_time = pick["time"]
                return

        print(lang_data["error_1"])


select_pickaxe()

def loop():
    while True:
        global pick_time
        pyautogui.moveTo(x=center_x, y=center_y)
        pyautogui.mouseDown()
        pyautogui.press("a")
        time.sleep(pick_time)
        pyautogui.press("d")

def q_pressed():
    while True:
        if keyboard.is_pressed("o"):
            print(lang_data["program"])
            os._exit(0) 

thread_q = threading.Thread(target=q_pressed, daemon=True)
thread_q.start()

loop()
