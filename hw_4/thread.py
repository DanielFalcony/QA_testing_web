"""
Не привязано к проекту, просто демонстрация многопоточного режима
"""

from threading import Thread
from time import sleep


def script(text, pause):
    for i in range(5):
        print(text)
        sleep(pause)


tread1 = Thread(target=script, args=("first", 1))
tread2 = Thread(target=script, args=("second", 2))
tread3 = Thread(target=script, args=("third", 3))

tread1.start()
tread2.start()
tread3.start()
tread1.join()
tread2.join()
tread3.join()
