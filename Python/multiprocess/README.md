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

###Caution###
Target function can't have return value, so...use pool!!
```

<h3 id='pool'>Pool</h3>

```

```

***
<h2 id="tkx" align=center> Thanks </h2>

## Thanks to [Morvan][1] and all other internet resources.

[1]:https://morvanzhou.github.io/ "Morvan"