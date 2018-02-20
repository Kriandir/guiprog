import multiprocessing
from worker import Worker

# def worker(procnum, return_dict):
#     '''worker function'''
#     print str(procnum) + ' represent!'
#     return_dict[procnum] = procnum


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=Worker, args=(i,return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    print return_dict.values()
