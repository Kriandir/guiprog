import threading
import wx

class Worker(threading.Thread):
    # Our workers constructor, note the super() method which is vital if we want this
    # to function properly
    def __init__(self):
        super(Worker, self).__init__()
        self.stop = False



    def run(self):
        i = 0
        while i <1000000:

            if self.stop:
                print 'weugrwiuer'
                return
            i+=1
            print(i)

        print 'HWOHWOWH'
        return
    #     self.closewindows()
    #
    # def closewindows(self):
    #     self.frame.DestroyandContinue()
    #     print 'test'
