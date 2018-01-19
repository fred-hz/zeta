from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaBlackrock_3(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.cps = self.context.fetch_data('adj_close')
        self.vol = self.context.fetch_data('volume')
        self.alpha = self.context.alpha

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                self.alpha[ii] = -np.nanstd(self.vol[di-self.delay-np.arange(20),ii])

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('volume')
