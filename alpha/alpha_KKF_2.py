from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaKKF_2(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.high = self.context.fetch_data('adj_high')
        self.low = self.context.fetch_data('adj_low')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = self.high[di-self.delay-np.arange(22), ii] - self.low[di-self.delay-np.arange(22), ii]
                self.alpha[ii] = np.nanpercentile(temp, 50) - np.nanmean(temp)

    def dependencies(self):
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')