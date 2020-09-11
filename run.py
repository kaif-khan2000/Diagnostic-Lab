import os
import webbrowser
import threading
def runserver():
    os.system("python manage.py runserver")
def openbrowser():
    webbrowser.open("http://localhost:8000")
t1 = threading.Thread(target=runserver,args=())
t2 = threading.Thread(target=openbrowser,args=())
t1.start()
t2.start()