import yappi

class YappiProfile(object):
    """ Wrapper class that represents Yappi profiling backend with API matching
        the cProfile.
    """
    def __init__(self):
        self.stats = None

    def runcall(self, func, *args, **kw):
        self.enable()
        try:
            return func(*args, **kw)
        finally:
            self.disable()

    def enable(self):
        yappi.start()

    def disable(self):
        yappi.stop()

    def create_stats(self):
        self.stats = yappi.convert2pstats(yappi.get_func_stats()).stats

