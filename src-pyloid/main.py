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
import leosheet as ls
import secrets_

ls.secret_holder.set_secrets(secrets_.secrets)


def get_device_id():
    # 获取设备的MAC地址
    mac_address = hex(uuid.getnode()).replace("0x", "").upper()
    # 将MAC地址格式化为设备ID
    device_id = "-".join(mac_address[i : i + 2] for i in range(0, 11, 2))
    return device_id


app = Pyloid(app_name="activator", single_instance=True)
WIDTH = 600
HEIGHT = 300

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
    @Bridge(str, result=str)
    def print_info(self, msg):
        print(msg)

    @Bridge(str, result=int)
    def bindDeviceID(self, key):
        try:
            did = get_device_id()
            dataset = ls.get_whole_dataset()
            rows = []
            for row in dataset:
                rows.append(row)

            for i in range(len(rows)):
                k = str(rows[i][0])
                d = rows[i][1]
                
                if key == k:
                    if d is None:
                        # 修改现有行的device_id值
                        query = f"UPDATE SHEET SET device_id='{did}' WHERE key='{key}'"
                        ls.run_query(query)
                        return 1  # 激活成功
                    else:   
                        return -1 # 密钥已使用, 不进行任何操作
                    
            else:
                return -2 # 密钥无效   
        except Exception as e:
            print(e)
            return 0  # 激活失败


####################################################################


if is_production():
    # production
    window = app.create_window(
        title="激活器", js_apis=[custom()], width=WIDTH, height=HEIGHT
    )
    window.load_file(os.path.join(get_production_path(), "build/index.html"))
else:
    window = app.create_window(
        title="激活器",
        js_apis=[custom()],
        dev_tools=True,
        width=WIDTH,
        height=HEIGHT,
    )
    window.load_url("http://localhost:5173")

window.show_and_focus()

app.run()  # run
