from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaBeats_34(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.high = self.context.fetch_data('adj_high')
        self.open = self.context.fetch_data('adj_open')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = (self.cps[di-self.delay-np.arange(5), ii] - self.open[di-self.delay-np.arange(5), ii]) * (self.high[di-self.delay-np.arange(5), ii] - self.cps[di-self.delay-np.arange(5), ii])
                tmp = np.nanmean(temp)
                if abs(tmp) > 1e-5:
                    self.alpha[ii] = (temp[0] - tmp) / tmp

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
        self.register_dependency('adj_open')