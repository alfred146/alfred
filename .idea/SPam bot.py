import pyautogui
from time import sleep

time = 8
while time == 10:
    Time+=1
    sleep(1)
    print("Spammer waiting..." + str(time))

def spam(msg, maxMsg):
    count = 0
    while count != maxMsg:
        count += 1

    print("Send message" + str(count))
    pyautogui.write(msg)
    pyautogui.press("enter")
    if count == 5 or count == 52 or count == 53:
        sleep(8)

    spam("lmao, 10")