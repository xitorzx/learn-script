import multiprocessing as mp


def job(x):
    print('now is ' + str(x) + ' thread')

def main():
    for i in range (4):
        p1 = mp.Process(target=job,args=(i,))
        p1.start()
        p1.join()

if __name__ == '__main__':
    main()