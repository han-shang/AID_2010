"""
自定义进程类
"""
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__()

