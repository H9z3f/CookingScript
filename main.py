import pyautogui as pag
import keyboard as kb
from time import sleep
from PIL import Image
import requests as req


def rSalad(defPos, imgData):
    while True:
        mPos = los(imgData["meat"], confidence=0.7)
        ePos = los(imgData["eggs"], confidence=0.7)
        vPos = los(imgData["vegetable"], confidence=0.7)
        if mPos and ePos and vPos:
            mt(mPos[0], mPos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            mt(ePos[0], ePos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            mt(vPos[0], vPos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            mt(defPos["knife"][0], defPos["knife"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            mt(defPos["fire"][0], defPos["fire"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            pag.leftClick(x=defPos["start"][0], y=defPos["start"][1])
            sleep(5)
        else:
            pag.alert(text="You ran out of the required ingredients.", button="Ok")
            main()


def stew(defPos, imgData):
    while True:
        mPos = los(imgData["meat"], confidence=0.7)
        vPos = los(imgData["vegetable"], confidence=0.7)
        if mPos and vPos:
            mt(mPos[0], mPos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            mt(vPos[0], vPos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            mt(defPos["water"][0], defPos["water"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            mt(defPos["fire"][0], defPos["fire"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            pag.leftClick(x=defPos["start"][0], y=defPos["start"][1])
            sleep(5)
        else:
            pag.alert(text="You ran out of the required ingredients.", button="Ok")
            main()


def vSmoothie(defPos, imgData):
    while True:
        vPos = los(imgData["vegetable"], confidence=0.7)
        if vPos:
            mt(vPos[0], vPos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            mt(defPos["water"][0], defPos["water"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            mt(defPos["whisk"][0], defPos["whisk"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            pag.leftClick(x=defPos["start"][0], y=defPos["start"][1])
            sleep(5)
        else:
            pag.alert(text="You ran out of the required ingredients.", button="Ok")
            main()


def fSmoothie(defPos, imgData):
    while True:
        fPos = los(imgData["fruit"], confidence=0.7)
        if fPos:
            mt(fPos[0], fPos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            mt(defPos["water"][0], defPos["water"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            mt(defPos["whisk"][0], defPos["whisk"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            pag.leftClick(x=defPos["start"][0], y=defPos["start"][1])
            sleep(5)
        else:
            pag.alert(text="You ran out of the required ingredients.", button="Ok")
            main()


def vSalad(defPos, imgData):
    while True:
        vPos = los(imgData["vegetable"], confidence=0.7)
        if vPos:
            mt(vPos[0], vPos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            mt(defPos["knife"][0], defPos["knife"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            pag.leftClick(x=defPos["start"][0], y=defPos["start"][1])
            sleep(5)
        else:
            pag.alert(text="You ran out of the required ingredients.", button="Ok")
            main()


def fSalad(defPos, imgData):
    while True:
        fPos = los(imgData["fruit"], confidence=0.7)
        if fPos:
            mt(fPos[0], fPos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            mt(defPos["knife"][0], defPos["knife"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            pag.leftClick(x=defPos["start"][0], y=defPos["start"][1])
            sleep(5)
        else:
            pag.alert(text="You ran out of the required ingredients.", button="Ok")
            main()


def sEggs(defPos, imgData):
    while True:
        ePos = los(imgData["eggs"], confidence=0.7)
        if ePos:
            mt(ePos[0], ePos[1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
            mt(defPos["fire"][0], defPos["fire"][1])
            dt(defPos["knife"][0], defPos["knife"][1] - 150, 0.25)
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
                "knife": los(data["knife"], confidence=0.7),
                "whisk": los(data["whisk"], confidence=0.7),
                "fire": los(data["fire"], confidence=0.7),
                "water": los(data["water"], confidence=0.7),
                "start": los(data["start"], confidence=0.7)
            }
            match dish:
                case "Stew[3]":
                    stew(defPos, data)
                case "Vegetable smoothie[2]":
                    vSmoothie(defPos, data)
                case "Fruit smoothie[2]":
                    fSmoothie(defPos, data)
                case "Russian salad[5]":
                    rSalad(defPos, data)
                case "Vegetable salad":
                    vSalad(defPos, data)
                case "Fruit salad":
                    fSalad(defPos, data)
                case "Scrambled eggs":
                    sEggs(defPos, data)


if __name__ == "__main__":
    los = pag.locateOnScreen
    mt = pag.moveTo
    dt = pag.dragTo
    data = {
        "knife": Image.open(req.get(
            "https://github.com/H9z3f/CookingScript/blob/main/images/knife.png?raw=true",
            stream=True
        ).raw),
        "whisk": Image.open(req.get(
            "https://github.com/H9z3f/CookingScript/blob/main/images/whisk.png?raw=true",
            stream=True
        ).raw),
        "fire": Image.open(req.get(
            "https://github.com/H9z3f/CookingScript/blob/main/images/fire.png?raw=true",
            stream=True
        ).raw),
        "water": Image.open(req.get(
            "https://github.com/H9z3f/CookingScript/blob/main/images/water.png?raw=true",
            stream=True
        ).raw),
        "start": Image.open(req.get(
            "https://github.com/H9z3f/CookingScript/blob/main/images/start.png?raw=true",
            stream=True
        ).raw),
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
    main()
