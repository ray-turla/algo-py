import time


"""
  This utility decorator measures the time of a method.
  CREDITS TO Nikita Tonkoskur - https://stackoverflow.com/users/9631956/nikita-tonkoskur
  Reference feed - https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
"""
def timeit(method):
    def timed(*args, **kwargs):
        ts = time.perf_counter()
        result = method(*args, **kwargs)
        te = time.perf_counter()
        if 'log_time' in kwargs:
            name = kwargs.get('log_name', method.__name__.upper())
            kwargs['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.22f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed