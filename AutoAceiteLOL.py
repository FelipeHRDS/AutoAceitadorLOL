import requests
import pyautogui
import cv2
import time


TOKEN = "TOKEN DO SEU BOT NO TELEGRAM"
CHAT_ID = "SEU CHAT ID"


def notificacao_partida(texto):
    requests.get(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": texto
        }
    )



while True:
    try:
        botaoaceitarfila = pyautogui.locateOnScreen("buttonlol.png", confidence=0.7)
                
        if botaoaceitarfila != None:
            pyautogui.click(pyautogui.center(botaoaceitarfila))
            notificacao_partida("Partida encontrada")
            break
    except pyautogui.ImageNotFoundException:
        time.sleep(1)


time.sleep(30)

while True:
    try:
        botaochampselect = pyautogui.locateOnScreen("champselect.png", confidence=0.5)
        
        if botaochampselect != None:
            notificacao_partida("Sua vez de pickar")
            break
    except pyautogui.ImageNotFoundException:
            time.sleep(1)





