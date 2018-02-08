import multiprocessing as mp

def job1(x):
    return x*x

def main():
    pool = mp.Pool(processes=3) #processes: Define the max cores
    res = pool.map(job1,range(101))
    #map can get all value automatically.
    print (res)
if __name__ == '__main__':
    main()