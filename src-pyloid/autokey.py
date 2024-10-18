import utils
import pydirectinput
import time
import pygetwindow

@utils.stoppable(sleep_time=2)
def autokey_job():
    pydirectinput.FAILSAFE = False
    press_arrow_keys()
    click_game_start("自由足球怀旧")
    


def click_game_start(program_title):
    # 获取指定程序的窗口句柄
    program_window = pygetwindow.getWindowsWithTitle(program_title)[0]
    
    print(f"控制的程序窗口: {program_window}")
    
    # 获取指定程序窗口的位置和大小
    window_region = (program_window.left, program_window.top, program_window.width, program_window.height)
    
    # 计算窗口右下角距离右下角 10% 的位置
    click_x = window_region[0] + int(window_region[2] * 0.9)
    click_y = window_region[1] + int(window_region[3] * 0.9)
    
    # 将鼠标移动到窗口右下角距离右下角 10% 的位置
    pydirectinput.moveTo(click_x, click_y)
    
    # 在指定位置执行鼠标点击和键盘按键操作
    pydirectinput.click()  # 执行鼠标点击
    





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