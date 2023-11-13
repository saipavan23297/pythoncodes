import multiprocessing
import time
def printcube(num):
    print("cube", num*num*num)
    time.sleep(100)
def printsquare(num):
    print("sqaure", num*num)
    time.sleep(100)

if __name__=="__main__":
    p1=multiprocessing.Process(target=printcube, args=(10,))
    p2=multiprocessing.Process(target=printsquare, args=(10,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("done")


'''
def myfunction(x):
    print(x)
if __name__ == "__main__":
    processes = []
    for i in range(5):
        process = multiprocessing.Process(target=myfunction, args=(i,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

'''