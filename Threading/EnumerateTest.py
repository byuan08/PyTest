import threading
import time
import random
import logging

logging.basicConfig(level = logging.DEBUG, format = '(%(threadName)-9s) %(message)s')

def f():
	t = threading.currentThread()
	#print(t.getName())
	r = random.randint(1,10)
	logging.debug('sleeping %s seconds',r)
	time.sleep(r)
	logging.debug('ending')
	return

if __name__ == '__main__':
	for i in range(3):
		t1 = threading.Thread(target = f)
		t1.setDaemon(True)
		t1.start()


main_thread = threading.current_thread()
for t in threading.enumerate():
	#logging.debug('This thread is %s', t.getName())
	if t is main_thread:
		continue
	logging.debug('joining %s', t.getName())
	t.join()
		