import multiprocessing as mp

def job1(x,y):
    return x**y
def job2(x):
    return x**2

def main():
    pool = mp.Pool()
    res = []

    for i in range (3):
        for j in range (5):
            res = pool.apply(job1,args=(i,j,)) #sync thread
            print ('job1 ' + str(res))
    
    pool.close()
if __name__=='__main__':
    main()