import threading
import time

def foo():
	thread_name = threading.currentThread().getName()
	print('hello world ',thread_name)

t1 = threading.Timer(3.0,foo)
t1.setName('Timer 1')
t1.start()
t2 = threading.Timer(3,foo)
t2.setName('Timer 2')
t2.start()