import threading
from worker import Worker

def main():
    # This initializes ''thread1'' as an instance of our Worker Thread
    thread1 = Worker()
    thread2 = Worker()
    # This is the code needed to run our newly created thread
    thread1.start()
    thread2.start()

if __name__ == "__main__":
  main()
