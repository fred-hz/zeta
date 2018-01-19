from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaBeats_19(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.open = self.context.fetch_data('adj_open')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = np.zeros(5)
                for i in range(5):
                    if abs(self.open[di-self.delay-i][ii] - self.open[di-self.delay-i-1][ii]) > 1e-3:
                        if self.cps[di-self.delay-i][ii] < self.cps[di-self.delay-i-1][ii]:
                            temp[i] = (self.cps[di-self.delay-i-1][ii] - self.cps[di-self.delay-i][ii]) / (self.open[di-self.delay-i][ii] - self.open[di-self.delay-i-1][ii])
                tmp = np.nanmean(temp)
                if abs(tmp) > 1e-3:
                    self.alpha[ii] = (temp[0] - tmp) / tmp

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_open')