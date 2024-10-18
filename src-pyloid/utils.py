import threading
import time
import pygetwindow


def stoppable(sleep_time=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            stop_event = threading.Event()

            def inner():
                while not stop_event.is_set():
                    func(*args, **kwargs)
                    time.sleep(sleep_time)

            thread = threading.Thread(target=inner)
            thread.start()

            def stop():
                stop_event.set()
                thread.join()

            return stop

        return wrapper

    return decorator


def get_all_windows_title():
    # 获取所有可见窗口的标题
    window_titles = pygetwindow.getAllTitles()
    window_titles = [title for title in window_titles if title.strip()]
    return window_titles


