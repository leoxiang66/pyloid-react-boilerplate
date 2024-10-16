from pyloid import Pyloid, PyloidAPI, Bridge, TrayEvent, is_production, get_production_path
import os
import random
import string
from typing import Any

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
        
    @Bridge(result=str)
    def generate_random_string(self):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(16))
        print(random_string)
        return random_string
    
    @Bridge(str,result=bool)
    def copy2clipoard(self,str):
        try:
            app.copy_to_clipboard(str)
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
