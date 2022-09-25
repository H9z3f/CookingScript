import pyautogui as pag
import keyboard as kb
from time import sleep
from PIL import Image
import requests as req


def rSalad(defPos):
    while True:
        mPos = los(defPos["meat"], confidence=0.7)
        ePos = los(defPos["eggs"], confidence=0.7)
        vPos = los(defPos["vegetable"], confidence=0.7)
        if mPos and ePos and vPos:
            mt(mPos[0], mPos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            mt(ePos[0], ePos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            mt(vPos[0], vPos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            mt(defPos["knife"][0], defPos["knife"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            mt(defPos["fire"][0], defPos["fire"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            pag.leftClick(x=defPos["start"][0], y=defPos["start"][1])
            sleep(5)
        else:
            pag.alert(text="You ran out of the required ingredients.", button="Ok")
            main()


def stew(defPos):
    while True:
        mPos = los(defPos["meat"], confidence=0.7)
        vPos = los(defPos["vegetable"], confidence=0.7)
        if mPos and vPos:
            mt(mPos[0], mPos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            mt(vPos[0], vPos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            mt(defPos["water"][0], defPos["water"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            mt(defPos["fire"][0], defPos["fire"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            pag.leftClick(x=defPos["start"][0], y=defPos["start"][1])
            sleep(5)
        else:
            pag.alert(text="You ran out of the required ingredients.", button="Ok")
            main()


def vSmoothie(defPos):
    while True:
        vPos = los(defPos["vegetable"], confidence=0.7)
        if vPos:
            mt(vPos[0], vPos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            mt(defPos["water"][0], defPos["water"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            mt(defPos["whisk"][0], defPos["whisk"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            pag.leftClick(x=defPos["start"][0], y=defPos["start"][1])
            sleep(5)
        else:
            pag.alert(text="You ran out of the required ingredients.", button="Ok")
            main()


def fSmoothie(defPos):
    while True:
        fPos = los(defPos["fruit"], confidence=0.7)
        if fPos:
            mt(fPos[0], fPos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            mt(defPos["water"][0], defPos["water"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            mt(defPos["whisk"][0], defPos["whisk"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            pag.leftClick(x=defPos["start"][0], y=defPos["start"][1])
            sleep(5)
        else:
            pag.alert(text="You ran out of the required ingredients.", button="Ok")
            main()


def vSalad(defPos):
    while True:
        vPos = los(defPos["vegetable"], confidence=0.7)
        if vPos:
            mt(vPos[0], vPos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            mt(defPos["knife"][0], defPos["knife"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            pag.leftClick(x=defPos["start"][0], y=defPos["start"][1])
            sleep(5)
        else:
            pag.alert(text="You ran out of the required ingredients.", button="Ok")
            main()


def fSalad(defPos):
    while True:
        fPos = los(defPos["fruit"], confidence=0.7)
        if fPos:
            mt(fPos[0], fPos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            mt(defPos["knife"][0], defPos["knife"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            pag.leftClick(x=defPos["start"][0], y=defPos["start"][1])
            sleep(5)
        else:
            pag.alert(text="You ran out of the required ingredients.", button="Ok")
            main()


def sEggs(defPos):
    while True:
        ePos = los(defPos["eggs"], confidence=0.7)
        if ePos:
            mt(ePos[0], ePos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            mt(defPos["fire"][0], defPos["fire"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.5)
            pag.leftClick(x=defPos["start"][0], y=defPos["start"][1])
            sleep(5)
        else:
            pag.alert(text="You ran out of the required ingredients.", button="Ok")
            main()


def main():
    pag.alert(text="Choose the dish you are interested in.\nGet close to the stove and press the 'e' key.\n"
                   "To change the recipe or stop the operation press 'esc'.", button="Start")
    dish = pag.confirm(text="Choose the dish", buttons=["Russian salad[5]", "Stew[3]", "Vegetable smoothie[2]",
                                                        "Fruit smoothie[2]", "Vegetable salad", "Fruit salad",
                                                        "Scrambled eggs"])
    if dish is None:
        return 0
    while True:
        if kb.is_pressed("e"):
            sleep(0.5)
            defPos = {
                "knife": los(Image.open(req.get(
                    "https://github.com/H9z3f/CookingScript/blob/main/images/knife.png?raw=true",
                    stream=True
                ).raw), confidence=0.7),
                "whisk": los(Image.open(req.get(
                    "https://github.com/H9z3f/CookingScript/blob/main/images/whisk.png?raw=true",
                    stream=True
                ).raw), confidence=0.7),
                "fire": los(Image.open(req.get(
                    "https://github.com/H9z3f/CookingScript/blob/main/images/fire.png?raw=true",
                    stream=True
                ).raw), confidence=0.7),
                "water": los(Image.open(req.get(
                    "https://github.com/H9z3f/CookingScript/blob/main/images/water.png?raw=true",
                    stream=True
                ).raw), confidence=0.7),
                "start": los(Image.open(req.get(
                    "https://github.com/H9z3f/CookingScript/blob/main/images/start.png?raw=true",
                    stream=True
                ).raw), confidence=0.7),
                "meat": Image.open(req.get(
                    "https://github.com/H9z3f/CookingScript/blob/main/images/meat.png?raw=true",
                    stream=True
                ).raw),
                "eggs": Image.open(req.get(
                    "https://github.com/H9z3f/CookingScript/blob/main/images/eggs.png?raw=true",
                    stream=True
                ).raw),
                "vegetable": Image.open(req.get(
                    "https://github.com/H9z3f/CookingScript/blob/main/images/vegetable.png?raw=true",
                    stream=True
                ).raw),
                "fruit": Image.open(req.get(
                    "https://github.com/H9z3f/CookingScript/blob/main/images/fruit.png?raw=true",
                    stream=True
                ).raw)
            }
            match dish:
                case "Stew[3]":
                    stew(defPos)
                case "Vegetable smoothie[2]":
                    vSmoothie(defPos)
                case "Fruit smoothie[2]":
                    fSmoothie(defPos)
                case "Russian salad[5]":
                    rSalad(defPos)
                case "Vegetable salad":
                    vSalad(defPos)
                case "Fruit salad":
                    fSalad(defPos)
                case "Scrambled eggs":
                    sEggs(defPos)


los = pag.locateOnScreen
mt = pag.moveTo
dt = pag.dragTo
if __name__ == "__main__":
    main()
