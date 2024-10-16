from pyloid import Pyloid, PyloidAPI, Bridge, TrayEvent, is_production, get_production_path
import os
import uuid

def get_device_id():
    # 获取设备的MAC地址
    mac_address = hex(uuid.getnode()).replace('0x', '').upper()
    # 将MAC地址格式化为设备ID
    device_id = '-'.join(mac_address[i:i+2] for i in range(0, 11, 2))
    return device_id

app = Pyloid(app_name="skey_generator", single_instance=True)
WIDTH = 600
HEIGHT = 300

if (is_production()):
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
    def print_info(self,msg):
        print(msg)
        
    
    @Bridge(str,result=bool)
    def bindDeviceID(self,key):
        try:
            did = get_device_id()
            return True
        except Exception as e:
            print(e)
            return False
        
        
    
    
####################################################################


if (is_production()):
    # production
    window = app.create_window(
        title="单点登录密钥生成器",
        js_apis=[custom()],
        width=WIDTH,
        height=HEIGHT
    )
    window.load_file(os.path.join(get_production_path(), "build/index.html"))
else:
    window = app.create_window(
        title="单点登录密钥生成器",
        js_apis=[custom()],
        dev_tools=True,
        width=WIDTH,
        height=HEIGHT
    )
    window.load_url("http://localhost:5173")

window.show_and_focus()

app.run()  # run
