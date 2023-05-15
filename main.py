from PIL.Image import open
from PIL import UnidentifiedImageError
from pyperclip import copy
from webbrowser import open_new
import sys
from requests import get
from pyautogui import alert, confirm, locateOnScreen, rightClick, leftClick
from time import sleep
from keyboard import is_pressed


def rSalad(staticPositions):
    while True:
        meatPosition = locateOnScreen(imageData["meat"], confidence=0.7)
        eggsPosition = locateOnScreen(imageData["eggs"], confidence=0.7)
        vegetablePosition = locateOnScreen(imageData["vegetable"], confidence=0.7)
        if meatPosition and eggsPosition and vegetablePosition:
            rightClick(meatPosition[0], meatPosition[1])
            rightClick(eggsPosition[0], eggsPosition[1])
            rightClick(vegetablePosition[0], vegetablePosition[1])
            rightClick(staticPositions["fire"][0], staticPositions["fire"][1])
            rightClick(staticPositions["knife"][0], staticPositions["knife"][1])
            leftClick(staticPositions["start"][0], staticPositions["start"][1])
            sleep(5)
        else:
            ranOut()


def stew(staticPositions):
    while True:
        meatPosition = locateOnScreen(imageData["meat"], confidence=0.7)
        vegetablePosition = locateOnScreen(imageData["vegetable"], confidence=0.7)
        if meatPosition and vegetablePosition:
            rightClick(meatPosition[0], meatPosition[1])
            rightClick(vegetablePosition[0], vegetablePosition[1])
            rightClick(staticPositions["fire"][0], staticPositions["fire"][1])
            rightClick(staticPositions["water"][0], staticPositions["water"][1])
            leftClick(staticPositions["start"][0], staticPositions["start"][1])
            sleep(5)
        else:
            ranOut()


def vSmoothie(staticPositions):
    while True:
        vegetablePosition = locateOnScreen(imageData["vegetable"], confidence=0.7)
        if vegetablePosition:
            rightClick(vegetablePosition[0], vegetablePosition[1])
            rightClick(staticPositions["water"][0], staticPositions["water"][1])
            rightClick(staticPositions["whisk"][0], staticPositions["whisk"][1])
            leftClick(staticPositions["start"][0], staticPositions["start"][1])
            sleep(5)
        else:
            ranOut()


def fSmoothie(staticPositions):
    while True:
        fruitPosition = locateOnScreen(imageData["fruit"], confidence=0.7)
        if fruitPosition:
            rightClick(fruitPosition[0], fruitPosition[1])
            rightClick(staticPositions["water"][0], staticPositions["water"][1])
            rightClick(staticPositions["whisk"][0], staticPositions["whisk"][1])
            leftClick(staticPositions["start"][0], staticPositions["start"][1])
            sleep(5)
        else:
            ranOut()


def vSalad(staticPositions):
    while True:
        vegetablePosition = locateOnScreen(imageData["vegetable"], confidence=0.7)
        if vegetablePosition:
            rightClick(vegetablePosition[0], vegetablePosition[1])
            rightClick(staticPositions["knife"][0], staticPositions["knife"][1])
            leftClick(staticPositions["start"][0], staticPositions["start"][1])
            sleep(5)
        else:
            ranOut()


def fSalad(staticPositions):
    while True:
        fruitPosition = locateOnScreen(imageData["fruit"], confidence=0.7)
        if fruitPosition:
            rightClick(fruitPosition[0], fruitPosition[1])
            rightClick(staticPositions["knife"][0], staticPositions["knife"][1])
            leftClick(staticPositions["start"][0], staticPositions["start"][1])
            sleep(5)
        else:
            ranOut()


def sEggs(staticPositions):
    while True:
        eggsPosition = locateOnScreen(imageData["eggs"], confidence=0.7)
        if eggsPosition:
            rightClick(eggsPosition[0], eggsPosition[1])
            rightClick(staticPositions["fire"][0], staticPositions["fire"][1])
            leftClick(staticPositions["start"][0], staticPositions["start"][1])
            sleep(5)
        else:
            ranOut()


def ranOut():
    alert(text="You ran out of the required ingredients.", button="Ok")
    main()


def main():
    dish = confirm(text="Choose the dish:", buttons=["Russian salad[5]", "Stew[3]", "Vegetable smoothie[2]",
                                                     "Fruit smoothie[2]", "Vegetable salad", "Fruit salad",
                                                     "Scrambled eggs"])
    if dish == None:
        sys.exit()
    while True:
        if is_pressed("e"):
            sleep(0.5)
            staticPositions = {
                "fire": locateOnScreen(imageData["fire"], confidence=0.7),
                "knife": locateOnScreen(imageData["knife"], confidence=0.7),
                "start": locateOnScreen(imageData["start"], confidence=0.7),
                "water": locateOnScreen(imageData["water"], confidence=0.7),
                "whisk": locateOnScreen(imageData["whisk"], confidence=0.7)
            }
            match dish:
                case "Russian salad[5]":
                    rSalad(staticPositions)
                case "Stew[3]":
                    stew(staticPositions)
                case "Vegetable smoothie[2]":
                    vSmoothie(staticPositions)
                case "Fruit smoothie[2]":
                    fSmoothie(staticPositions)
                case "Vegetable salad":
                    vSalad(staticPositions)
                case "Fruit salad":
                    fSalad(staticPositions)
                case "Scrambled eggs":
                    sEggs(staticPositions)


if __name__ == "__main__":
    print("Loading image data...")
    try:
        imageData = {
            "eggs": open(get(
                "https://github.com/H9z3f/CookingScript/blob/main/images/eggs.png?raw=true",
                stream=True
            ).raw),
            "fire": open(get(
                "https://github.com/H9z3f/CookingScript/blob/main/images/fire.png?raw=true",
                stream=True
            ).raw),
            "fruit": open(get(
                "https://github.com/H9z3f/CookingScript/blob/main/images/fruit.png?raw=true",
                stream=True
            ).raw),
            "knife": open(get(
                "https://github.com/H9z3f/CookingScript/blob/main/images/knife.png?raw=true",
                stream=True
            ).raw),
            "meat": open(get(
                "https://github.com/H9z3f/CookingScript/blob/main/images/meat.png?raw=true",
                stream=True
            ).raw),
            "start": open(get(
                "https://github.com/H9z3f/CookingScript/blob/main/images/start.png?raw=true",
                stream=True
            ).raw),
            "vegetable": open(get(
                "https://github.com/H9z3f/CookingScript/blob/main/images/vegetable.png?raw=true",
                stream=True
            ).raw),
            "water": open(get(
                "https://github.com/H9z3f/CookingScript/blob/main/images/water.png?raw=true",
                stream=True
            ).raw),
            "whisk": open(get(
                "https://github.com/H9z3f/CookingScript/blob/main/images/whisk.png?raw=true",
                stream=True
            ).raw),
        }
    except UnidentifiedImageError:
        choice = confirm(text="The script is outdated.\n"
                              "Please download the latest version from the link:\n"
                              "https://github.com/H9z3f/CookingScript/raw/main/CookingScript.exe",
                         buttons=["Open", "Copy"])
        match choice:
            case "Open":
                open_new("https://github.com/H9z3f/CookingScript/raw/main/CookingScript.exe")
            case "Copy":
                copy("https://github.com/H9z3f/CookingScript/raw/main/CookingScript.exe")
        sys.exit()
    else:
        alert(text="Choose the dish you are interested in.\n"
                   "Get close to the stove and press the 'e' key.\n"
                   "To change the recipe or stop the operation press the 'esc' key.", button="Start")
        main()
