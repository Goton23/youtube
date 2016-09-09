import webbrowser
import time


url = "https://www.youtube.com/watch?v=2Pc36KAeLdY"
counter = 10

while True:
    webbrowser.open_new_tab(url + 'doc/')

    time.sleep(5)

