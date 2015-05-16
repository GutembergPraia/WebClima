import threading
import serial
import time

class myThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.modo = 0 # 0 - Rum/1 - Stop/2 - exit
        self.paused = True
        self.ser = serial.Serial('/dev/ttyACM0',9600)
        self.state = threading.Condition()

    def run(self):
        while self.modo<2:
            with self.state:
                if self.paused:
                    self.state.wait() # block until notified
            time.sleep(.1)
            print_time(self.ser)
        self.ser.close()
        self.interrupt_main()

    def resume(self):
        with self.state:
            self.paused = False
            self.state.notify()  # unblock self if waiting

    def pause(self):
        with self.state:
            self.paused = True  # make self block and wait

    def sair(self):
        with self.state:
            self.modo = 2  # make self block and wait

def print_time(ser):
    strLinha = ser.readline()
    print "%s" % (strLinha)

threadLock = threading.Lock()
#threads = []

# Create new threads
thread1 = myThread()

# Start new Threads
thread1.start()

# Add threads to thread list
#threads.append(thread1)

# stop threads to thread list
time.sleep(5)
print" Pause"
thread1.pause()
time.sleep(5)
print" resume"
thread1.resume()
time.sleep(5)
print" Pause"
thread1.pause()
time.sleep(5)
thread1.sair()

print "Exiting Main Thread"
