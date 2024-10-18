from pyloid import (
    Pyloid,
    PyloidAPI,
    Bridge,
    TrayEvent,
    is_production,
    get_production_path,
)
import os
import uuid
import requests as re
from appdirs import user_data_dir
from autokey import autokey_job

WIDTH = 500
HEIGHT = 400


def get_device_id():
    # 获取设备的MAC地址
    mac_address = hex(uuid.getnode()).replace("0x", "").upper()
    # 将MAC地址格式化为设备ID
    device_id = "-".join(mac_address[i : i + 2] for i in range(0, 11, 2))
    return device_id


VERSION = "0.1.0"
app = Pyloid(app_name=f"FST 按键精灵 v{VERSION}", single_instance=True)

if is_production():
    app.set_icon(os.path.join(get_production_path(), "icons/icon.png"))
    app.set_tray_icon(os.path.join(get_production_path(), "icons/icon.png"))
else:
    app.set_icon("src-pyloid/icons/icon.png")
    app.set_tray_icon("src-pyloid/icons/icon.png")


############################## Tray ################################
def on_double_click():
    print("Tray icon was double-clicked.")


app.set_tray_actions(
    {
        TrayEvent.DoubleClick: on_double_click,
    }
)
app.set_tray_menu_items(
    [
        {"label": "Show Window", "callback": app.show_and_focus_main_window},
        {"label": "Exit", "callback": app.quit},
    ]
)
####################################################################

############################## Bridge ##############################


class custom(PyloidAPI):
    @Bridge(result=bool)
    def start(self):
        try:
            self.stop_func = autokey_job()
            print("start ...")
            return True
        except:
            return False
    
    @Bridge(result=bool)
    def stop(self):
        try:
            self.stop_func()
            print("stop ...")
            return True
        except:
            return False
        
    
    @Bridge(str, result=bool)
    def store_key(self, key):
        try:
            app_data_dir = user_data_dir("FSTAutokey")
            os.makedirs(app_data_dir, exist_ok=True)
            file_path = os.path.join(app_data_dir, ".secret.txt")

            # 将密钥写入文件
            with open(file_path, "w") as file:
                file.write(key)

            return True
        except Exception as e:
            print(f"Error occurred while storing the key: {str(e)}")
            return False
    
    @Bridge(result=str)
    def load_key(self):
        try:
            app_data_dir = user_data_dir("FSTAutokey")
            file_path = os.path.join(app_data_dir, ".secret.txt")

            # 检查文件是否存在
            if os.path.exists(file_path):
                # 从文件中读取密钥
                with open(file_path, "r") as file:
                    key = file.read().strip()
                return key
            else:
                return ""
        except Exception as e:
            print(f"Error occurred while loading the key: {str(e)}")
            return ""

    @Bridge(result=str)
    def print_info(self):
        print("button clicked")

    @Bridge(str, result=int)
    def verify_key(self, key):
        did = get_device_id()

        dev_url = "http://127.0.0.1:8000"
        prod_url = "https://leoxiang66-io-server-1.onrender.com"
        response = re.post(
            f"{prod_url}/verify_key",
            json={"key": key, "did": did},
            headers={"Content-Type": "application/json"},
        )
        response = response.json()["code"]
        return response


####################################################################


if is_production():
    # production
    window = app.create_window(
        title=f"FST 按键精灵 v{VERSION}",
        js_apis=[custom()],
        width=WIDTH,
        height=HEIGHT
    )
    window.load_file(os.path.join(get_production_path(), "build/index.html"))
else:
    window = app.create_window(
        title=f"FST 按键精灵 v{VERSION} dev",
        js_apis=[custom()],
        dev_tools=True,
         width=WIDTH,
        height=HEIGHT
    )
    window.load_url("http://localhost:5173")

window.show_and_focus()

app.run()  # run
