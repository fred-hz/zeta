from data_manager.dm_base import DataManagerBase
import numpy as np
import re, os


class DataManagerComboAlpha(DataManagerBase):
    def __init__(self, params, context):
        super(DataManagerComboAlpha, self).__init__(params=params, context=context)
        # Fetch data from context and identify values to variables

    def initialize(self):
        self.ii_list = self.context.ii_list
        self.di_list = self.context.di_list

    def provide_data(self):
        di_size = len(self.context.di_list)
        ii_size = len(self.context.ii_list)

        self.equal_weight = np.ndarray((di_size, ii_size), dtype=float)
        self.equal_weight.flat = np.nan
        self.diff_weight = np.ndarray((di_size, ii_size), dtype=float)
        self.diff_weight.flat = np.nan
        self.fitness_weight = np.ndarray((di_size, ii_size), dtype=float)
        self.fitness_weight.flat = np.nan

        self.register_data('equal_weight', self.equal_weight)
        self.register_data('diff_weight', self.diff_weight)
        self.register_data('fitness_weight', self.fitness_weight)

    def compute_day(self, di):
        pass

    def dependencies(self):
        # Do not need dependencies in DataManagerBaseData
        pass

    def caches(self):
        self.register_cache('equal_weight')
        self.register_cache('diff_weight')
        self.register_cache('fitness_weight')

    def freshes(self):
        self.register_fresh('equal_weight')
        self.register_fresh('diff_weight')
        self.register_fresh('fitness_weight')
