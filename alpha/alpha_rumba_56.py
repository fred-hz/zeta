from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaRumba_56(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.open = self.context.fetch_data('adj_open')
        self.vol = self.context.fetch_data('volume')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                self.alpha[ii] = -util.corr(self.vol[di-self.delay-np.arange(10), ii], self.open[di-self.delay-np.arange(10)-3, ii])

    def dependencies(self):
        self.register_dependency('adj_open')
        self.register_dependency('volume')