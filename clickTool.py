import pyautogui
import time

quantity = int(input("Enter click count: "))
intervalTime = float(input("Enter interval: "))
print("Open Application to click on!")
time.sleep(5)

while (quantity != 0):

    pyautogui.click(clicks=1, interval=intervalTime)

    quantity -= 1
print("Click has finished!")
