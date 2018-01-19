from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaBeats_31(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.high = self.context.fetch_data('adj_high')
        self.low = self.context.fetch_data('adj_low')
        self.vol = self.context.fetch_data('volume')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = np.zeros(5)
                for i in range(5):
                    if np.where(-np.isnan(self.low[di-self.delay-i-np.arange(5), ii]))[0].size == 0:
                        continue
                    temp1 = np.nanargmin(self.low[di-self.delay-i-np.arange(5), ii])
                    if self.high[di-self.delay-i][ii] - self.low[di-self.delay-i][ii] > 1e-5:
                        temp[i] = temp1 * (self.cps[di-self.delay-i][ii] - (self.high[di-self.delay-i][ii] + self.low[di-self.delay-i][ii])/2.0)/(self.high[di-self.delay-i][ii] - self.low[di-self.delay-i][ii]) * self.vol[di-self.delay-i][ii]
                tmp = np.nanmean(temp)
                if abs(tmp) > 1e-5:
                    self.alpha[ii] = (tmp - temp[0]) / tmp

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')
        self.register_dependency('volume')