import utils
import pydirectinput
import time

@utils.stoppable(sleep_time=2)
def press_arrow_keys():
    # 按下方向下键 2 秒
    pydirectinput.keyDown('down')
    time.sleep(2)
    pydirectinput.keyUp('down')
    
    # 按下 's' 键 2 秒
    pydirectinput.keyDown('s')
    time.sleep(2)
    pydirectinput.keyUp('s')

    # 按下方向上键 2 秒
    pydirectinput.keyDown('up')
    time.sleep(2)
    pydirectinput.keyUp('up')