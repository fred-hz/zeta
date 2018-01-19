from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaFactors_DAREC(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.DAREC = self.context.fetch_data('DAREC')
        self.alpha = self.context.alpha

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                self.alpha[ii] = self.DAREC[di-self.delay][ii]

    def dependencies(self):
        self.register_dependency('DAREC')
