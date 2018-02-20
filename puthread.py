import threading
import wx


class finishthreads():
    def __init__(self,thread):
        jack = "friend"
        self.thread = thread


    def jointhread(self):
        self.thread.join()
