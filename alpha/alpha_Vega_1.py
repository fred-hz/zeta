from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaVega_1(AlphaBase):
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
                MFV = np.zeros(10)
                for i in range(10):
                    if self.high[di-self.delay-i][ii] - self.low[di-self.delay-i][ii] > 1e-5:
                        MFV[i] = self.vol[di-self.delay-i][ii] * (self.cps[di-self.delay-i][ii] - (self.high[di-self.delay-i][ii] + self.low[di-self.delay-i][ii])/2.0)/(self.high[di-self.delay-i][ii] - self.low[di-self.delay-i][ii])
                    else:
                        MFV[i] = np.nan
                temp = util.wmean(MFV)
                up = np.sum(MFV > temp)
                down = np.sum(MFV < temp)
                if up + down > 0.5:
                    self.alpha[ii] = (up - down) / (down + up)

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')
        self.register_dependency('volume')
