from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaChacha_16(AlphaBase):
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
                ADL = np.zeros(100)
                count = 0
                for i in range(99, -1, -1):
                    if np.isnan(self.high[di-self.delay-i][ii]) or np.isnan(self.low[di-self.delay-i][ii]) or np.isnan(self.cps[di-self.delay-i][ii]) or np.isnan(self.vol[di-self.delay-i][ii]):
                        continue
                    if self.high[di-self.delay-i][ii] - self.low[di-self.delay-i][ii] > 1e-5:
                        if count == 0:
                            ADL[count] = 2 * self.vol[di-self.delay-i][ii] * (self.cps[di-self.delay-i][ii] - (self.high[di-self.delay-i][ii] + self.low[di-self.delay-i][ii])/2.0)/(self.high[di-self.delay-i][ii] - self.low[di-self.delay-i][ii])
                        else:
                            ADL[count] = 2 * self.vol[di - self.delay - i][ii] * (self.cps[di - self.delay - i][ii] - (
                            self.high[di - self.delay - i][ii] + self.low[di - self.delay - i][ii]) / 2.0) / (
                                         self.high[di - self.delay - i][ii] - self.low[di - self.delay - i][ii]) + ADL[count-1]
                        count += 1
                if count < 10:
                    continue
                temp = np.nanstd(ADL[count-1-np.arange(10)])
                if temp > 1e-5:
                    self.alpha[ii] = - np.nanstd(self.vol[di-self.delay-np.arange(10), ii]) / temp

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')
        self.register_dependency('volume')