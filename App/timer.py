import time

class Timer:

    def __init__(self):
        self._start_time = 0
        self._time = 0


    def is_timer_reset(self):
        return self._start_time == 0


    def start_timer(self):
        #timer was already started
        if(self._start_time != 0):
            return -1

        self._start_time = time.time()
        return 0


    def stop_time(self):
        #have not started the timer
        if(self._start_time == 0):
            return -1

        self._time = time.time() - self._start_time
        return self._time


    def get_time(self):
        return self._time

    
    def reset_timer(self):
        self._start_time = 0
        self._time = 0

    
    def time_function(self, func):
        if not self.is_timer_reset():
            self.reset_timer()
        
        self.start_timer()
        func()
        self.stop_time()

        return self._time
        