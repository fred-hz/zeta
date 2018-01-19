from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaVega_8(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.high = self.context.fetch_data('adj_high')
        self.low = self.context.fetch_data('adj_low')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = np.zeros(20)
                for i in range(20):
                    if self.cps[di-self.delay-i][ii] > self.cps[di-self.delay-i-1][ii]:
                        temp[i] = self.cps[di-self.delay-i][ii] - self.cps[di-self.delay-i-1][ii]
                tmp = util.corr(temp, np.arange(20))
                if abs(tmp) > 1e-5:
                    tr = np.maximum(self.high[di-self.delay-np.arange(20), ii], self.cps[di-self.delay-1-np.arange(20), ii]) - np.minimum(self.low[di-self.delay-np.arange(20), ii], self.cps[di-self.delay-1-np.arange(20), ii])
                    self.alpha[ii] = -util.corr(tr, np.arange(20)) / tmp

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')