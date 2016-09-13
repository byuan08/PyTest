import threading
import time
import logging
import subprocess

subprocess.call('clear')

logging.basicConfig(level = logging.DEBUG, format = '[%(threadName)s], %(message)s')

def wait_for_event(event):
	logging.debug('wait_for_event starting')
	event_is_set = event.wait()
	logging.debug('wait_for_event ending')

def wait_for_event_timeout(event,t):
	while not event.isSet():
		logging.debug('wait_for_event_timeout starting')
		event_is_set = event.wait(t)
		logging.debug('event set: %s ', event_is_set)
		if event_is_set:
			logging.debug('event is set. processing event')
		else:
			logging.debug('event not set yet, still waiting')
		

if __name__ == '__main__':
	e = threading.Event()
	t1 = threading.Thread(name = 'blocking', target = wait_for_event, args = (e,))
	t2 = threading.Thread(name = 'non-blocking', target = wait_for_event_timeout, args = (e,3))

	t1.start()
	t2.start()
	logging.debug('waiting before calling event.set()')
	time.sleep(3)
	e.set()
	logging.debug('event is set')
