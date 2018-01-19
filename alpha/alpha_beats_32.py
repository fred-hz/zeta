from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaBeats_32(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.high = self.context.fetch_data('adj_high')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = np.zeros(5)
                for i in range(5):
                    temp1 = np.nanstd(self.cps[di-self.delay-i-np.arange(20), ii])
                    if temp1 > 1e-5 and self.high[di-self.delay-i][ii] - self.cps[di-self.delay-i][ii] > 1e-5:
                        temp[i] = (self.cps[di-self.delay-i][ii] - np.nanmean(temp1)) / temp1 / (self.high[di-self.delay-i][ii] - self.cps[di-self.delay-i][ii])
                tmp = np.nanmean(temp)
                if abs(tmp) > 1e-5:
                    self.alpha[ii] = (tmp - temp[0]) / tmp

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')