import time
import progressbar

progressbar.streams.wrap_stderr()
with progressbar.ProgressBar(redirect_stdout=True) as bar:
    for i in range(10):
        time.sleep(0.1)
        bar.update(i)