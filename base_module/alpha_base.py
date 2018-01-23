from abc import(
    ABCMeta,
    abstractmethod
)
import numpy as np

class AlphaBase(object):
    __metaclass__ = ABCMeta

    def __init__(self, params):
        self.params = params

    
