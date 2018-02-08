import multiprocessing as mp

def job(q,a,b):
    res=0
    for i in range(100):
        res+=a+b
    q.put(res)

def job2(q):
    res=500
    q.put(res)
def job3(a,b):
    
    res = a*b
    print ('job3: '+ str(res))
    
def main():
    q=mp.Queue()

    p1 = mp.Process(target=job,args=(q,5,7))
    p1.start()
    p1.join()

    p2 = mp.Process(target=job2,args=(q,))
    p2.start()
    p2.join()

    p3 = mp.Process(target=job3,args=(3,4,))
    p3.start()
    p3.join()

    res1 = q.get()
    res2 = q.get()

    print ('job1: '+str(res1))
    print ('job2: '+str(res2))

if __name__ == '__main__':
    main()