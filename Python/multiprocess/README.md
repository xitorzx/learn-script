<h1 align=center>Multiprocess</h1>


```
training for multiprocessing
```
* [Introduction](#overview)
    * [Add Process](#add)
    * [Pool](#pool)
* [Thanks](#tkx)

***

<h2 id='overview' align=center> Introduction </h2>

```

This work is used for reminding the script of multiprocess in Python.

import multiprocessing as mp

```

<h3 id='add'>Add Process</h3>

```
View add_process.py file.
Usage:
1. p1 = mp.Process(target=job,(var,))
2. p1.start()
3. p1.join()

#Caution# Target function can't have return value

if adding Queue:
1. q = mp.Queue()
2. p1 = mp.Process(target=job,(q,var,))
# at the job fuction:
3. q.put(res)
# at main function:
4. q.get()

* * *
More complex than using Pool
```

<h3 id='pool'>Pool</h3>

```
pool can collect all files return.

1. p1 = mp.Pool() #in () you can define the max processes
2. p1.map(job,(var,))

```

***
<h2 id="tkx" align=center> Thanks </h2>

## Thanks to [Morvan][1] and all other internet resources.
## Thanks to [Python script][2].(Version 3.5)
[1]:https://morvanzhou.github.io/ "Morvan"
[2]:https://docs.python.org/3.5/library/multiprocessing.html#module-multiprocessing "Python script"