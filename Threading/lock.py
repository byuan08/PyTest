import threading
import time
import logging

# lock = threading.Lock()
# lock.release()
# try:
# 	#lock.acquire()
# 	#lock.release()
# 	a = 1
# except:
# 	print('error')

lock = threading.RLock()
a = lock.acquire()
b = lock.acquire(0)
print('a = ', a)
print('b = ', b)