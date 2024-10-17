from pyloid import Pyloid, PyloidAPI, Bridge, TrayEvent, is_production, get_production_path
import os

VERSION = "0.1.0"
app = Pyloid(app_name=f"FST 按键精灵 v{VERSION}", single_instance=True)

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
    @Bridge(result=str)
    def print_info(self):
        print("button clicked")
    
    @Bridge(str,result=int)
    def verify_key(self,key):
        
####################################################################


if (is_production()):
    # production
    window = app.create_window(
        title=f"FST 按键精灵 v{VERSION}",
        js_apis=[custom()],
    )
    window.load_file(os.path.join(get_production_path(), "build/index.html"))
else:
    window = app.create_window(
        title=f"FST 按键精灵 v{VERSION} dev",
        js_apis=[custom()],
        dev_tools=True,
    )
    window.load_url("http://localhost:5173")

window.show_and_focus()

app.run()  # run
