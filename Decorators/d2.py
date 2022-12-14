import time

def timer(fun):
    def wrapper():
        start =time.time()
        fun()
        print('time taken by function',fun.__name__,time.time()-start,'secs')
    return wrapper
@timer
def hello():
    print('hello world')
    time.sleep(0.5)

hello()