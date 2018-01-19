from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaChacha_13(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.high = self.context.fetch_data('adj_high')
        self.cps = self.context.fetch_data('adj_close')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp1 = np.zeros(10)
                temp2 = np.zeros(10)
                for i in range(10):
                    temp1[i] = np.nanmax(self.high[di-self.delay-i-np.arange(5), ii])
                    temp2[i] = np.nanstd(self.cps[di - self.delay - i - np.arange(20), ii])
                temp = np.nanstd(temp1)
                if temp > 1e-5:
                    self.alpha[ii] = np.nanstd(temp2) / temp

    def dependencies(self):
        self.register_dependency('adj_high')
        self.register_dependency('adj_close')