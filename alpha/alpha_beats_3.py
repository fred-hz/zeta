from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaBeats_3(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.high = self.context.fetch_data('adj_high')
        self.low = self.context.fetch_data('adj_low')
        self.open = self.context.fetch_data('adj_open')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = np.zeros(5)
                for i in range(5):
                    if np.where(-np.isnan(self.low[di-self.delay-i-np.arange(5), ii]))[0].size > 0 and np.where(-np.isnan(self.low[di-self.delay-i-np.arange(20), ii]))[0].size > 0:
                        temp[i] = (np.nanargmin(self.low[di-self.delay-i-np.arange(5), ii]) + 1.) / (np.nanargmin(self.low[di-self.delay-i-np.arange(20), ii]) + 1.)
                temp1 = np.nanmean(temp)
                if abs(temp1) > 1e-5:
                    self.alpha[ii] = (temp1 - temp[0])/temp1

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')
        self.register_dependency('adj_open')