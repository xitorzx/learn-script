<h1 align="center">IMG to Hex code and save as *.csv file</h1>



* [Introduction](#overview)
    * [Done](#done)
* [Finished work](#now)
    * [PY files](#py)
* [Note](#note)
    * [unDone](#undone)
* [Expect work](#expect)
* [Environment](#env)
* [Thank](#thx)

***
<h2 id="overview" align="center">Introduction</h2>

```
It's a work transform img to hex code.
And with google spreadsheet user-define ISA.
You may create a photo with google sheet on your own.
```
<h3 id="done">Done</h3>

```
1. Every functional work tuck into jpgtohex.py
Now you can use it to compress any photo into below 100x100 pixels 
(because I used thumbnail instead of resize function).

And then turn rgb color into hex code and save into example.csv file.
```



<h2 id="now" align="center">Finished Work</h2>
<h3 id="py">Python Files</h3>

```
1. jpgtohex.py
2. compress.py
3. aitkinson.py

From now on, I only use jpgtohex.py as main python file. 
All the others file are just test some function work. So I mainly introduce jpgtohex.py

As what I write above, I transform the photo into 'RGB' type to prevent some mistakes.

```


<h2 id="note" align="center" >Note</h2>
<h3 id="undone">Undone work</h3>

expect to add:
```
**Change (Save) the google user-define ISA**

1. Flexible Renamer and auto-compress img to 300pixel *.jpg files.

2.I've add define function called search() to flexibly 
   seach the current path and find out all image file. Then doing the image processing.

3. I could use glob() to do large numners of image files processing

4. the csv file should be printed out, add number to remember the file 
    or just as the name of the image but *.csv file format.

```
<h2 id="expect" align="center">Expect work</h3>

```
Now I finish the phototype of this work. I'd like to change some code from user-define ISA. 
Unlimit the upload photo size.

And also, I need some time to read the google user-define ISA and js. 
I think the author's work is a nice prototye to learn.

```

<h2 id='env' align='center'>Environment</h2>

```
1. python 3.5.2
2. PIL
3. glob
4. csv
5. google drive
```
<h2 id='thx'> Thanks </h2>

Thanks to [Amit Agarwal][1] and all others Internet source.

[1]:https://www.labnol.org/software/turn-images-into-pixel-art/12978/ "Amit Agarwal"
