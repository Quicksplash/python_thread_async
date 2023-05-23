import threading
import time

def getAllJson():
    time.sleep(50)
    print(f"{threading.current_thread().name}")



def runThreath():
    for i in range(5):
        thr = threading.Thread(target=getAllJson, args = () , name =  f"th- { i }")
        thr.start()

def start():
    runThreath()

start()

for i in range(100):
    time.sleep(1)
    print("активынй потоки", threading.active_count())
    print("конкрентный потоки" , threading.enumerate())

# Проверить метод join для синхронизации потоков