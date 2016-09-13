import threading
import time
import logging

logging.basicConfig(level = logging.DEBUG,format = '(%(threadName)-9s) %(message)s')

class MyThread(threading.Thread):
	def __init__(self, args=(), kwargs=None):
		super().__init__()
		self.args = args
		self.kwargs = kwargs
		return
		# in order to pass args and kwargs up to the level threading.Thread, superclass's
		# constructor needs to be called, and args, and kwargs need to be explicitly passed
		# to super class

	def run(self):
		logging.debug('running with %s and %s', self.args,self.kwargs)
		return


if __name__ == '__main__':
	t1 = MyThread(args = (1,), kwargs = {'a':1,'b':2})
	t1.start()


