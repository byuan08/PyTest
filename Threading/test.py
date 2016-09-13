import threading
import time
import logging

logging.basicConfig(level = logging.DEBUG, format = '[%(levelname)s] (%(threadName)s) %(message)s')

def f(id, sleep):
	logging.debug('Starting thread')
	time.sleep(sleep)
	print('The name of this thead is:',threading.currentThread().getName())
	logging.debug('Exiting thread')

def d(id,sec):
	logging.debug('starting daemon thread')
	while(sec>0):
		time.sleep(1)
		#logging.debug(sec, 'sec')
		print(sec, 'seconds')
		sec -= 1
	logging.debug('exiting daemon thread')


if __name__ == '__main__':
	t1 = threading.Thread(target = f, args = (1,1))
	t2 = threading.Thread(name = 'daemon', target = d, args = (2,5))
	t2.setDaemon(True)


t1.start()
t2.start()
t1.join() #join() blocks the caller's exection
logging.debug('joining %s thread', t1.getName())
t2.join(3)
logging.debug('joining %s thread', t2.getName())
#t2.join(7)
print('Daemon thread isAlive',t2.isAlive())
