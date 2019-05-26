import time
## This is actually very VERY bad for implementing in pure Python 
## Because of the overhead. Find another language or make a C-extension :)

## The following is a sorry excuse for a scheduler, but I went for the bare minimum
## of what the requirements specified.
def scheduler(f,seconds):
    time.sleep(seconds * 10**-3)
    return f()
