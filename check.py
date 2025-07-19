import threading
import time

semaphores = threading.BoundedSemaphore(value=3)

def access(thread_number):
    print(f"{thread_number} trying to get acccess")
    semaphores.acquire()
    print(f"{thread_number} has gained the access")
    time.sleep(10)
    print(f"{thread_number} released the access\n")
    semaphores.release()

for thead_number in range (1,11):
    t= threading.Thread(target=access,args=(thead_number,))
    t.start()
    time.sleep(0.5)
    