import utils
import pydirectinput
import time
import pygetwindow

@utils.stoppable(sleep_time=2)
def autokey_job():
    pydirectinput.FAILSAFE = False
    key_combos()
    click_game_start("自由足球怀旧")
    

def mouse_click(x,y):
    # 将鼠标移动到窗口右下角距离右下角 10% 的位置
    pydirectinput.moveTo(x, y)
    
    # 在指定位置执行鼠标点击和键盘按键操作
    pydirectinput.click()  # 执行鼠标点击
    
    time.sleep(2)

def click_game_start(program_title):
    # 获取指定程序的窗口句柄
    program_window = pygetwindow.getWindowsWithTitle(program_title)[0]
    
    print(f"控制的程序窗口: {program_window}")
    
    # 获取指定程序窗口的位置和大小
    window_region = (program_window.left, program_window.top, program_window.width, program_window.height)
    
    # 点击开始  
    mouse_click(
        window_region[0] + int(window_region[2] * 0.9),
        window_region[1] + int(window_region[3] * 0.9)
    )
    
    
    # 选择队友
    mouse_click(
        window_region[0] + int(window_region[2] * 0.6),
        window_region[1] + int(window_region[3] * 0.3)
    )
    
    press_key('down',time_=1)
    
    mouse_click(
        window_region[0] + int(window_region[2] * 0.7),
        window_region[1] + int(window_region[3] * 0.3)
    )
    
    press_key('down',time_=1)
    
    mouse_click(
        window_region[0] + int(window_region[2] * 0.8),
        window_region[1] + int(window_region[3] * 0.3)
    )
    
    press_key('up',time_=1)
    
    
    mouse_click(
        window_region[0] + int(window_region[2] * 0.6),
        window_region[1] + int(window_region[3] * 0.95)
    )
    
    mouse_click(
        window_region[0] + int(window_region[2] * 0.5),
        window_region[1] + int(window_region[3] * 0.78)
    )

def press_key(key:str, time_=2):
    pydirectinput.keyDown(key)
    time.sleep(time_)
    pydirectinput.keyUp(key)

def key_combos():
    # 按下方向下键 2 秒
    press_key('down')
    
    # 按下 's' 键 2 秒
    press_key('s')

    # 按下方向上键 2 秒
    press_key('up')