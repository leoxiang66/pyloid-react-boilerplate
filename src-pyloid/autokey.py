import utils
import pyautogui
import time

@utils.stoppable(sleep_time=2)
def press_arrow_keys():
    # 按下方向下键 2 秒
    pyautogui.keyDown('down')
    time.sleep(2)
    pyautogui.keyUp('down')
    
    pyautogui.keyDown('s')
    time.sleep(2)
    pyautogui.keyUp('s')

    # 按下方向上键 2 秒
    pyautogui.keyDown('up')
    time.sleep(2)
    pyautogui.keyUp('up')