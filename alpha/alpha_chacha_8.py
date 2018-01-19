from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaChacha_8(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.high = self.context.fetch_data('adj_high')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                n = 20
                EMAhh = np.zeros(n)
                EMA2hh = np.zeros(n)
                DEMAhh = np.zeros(n)
                for i in range(n-1, -1, -1):
                    if i == n-1:
                        EMAhh[i] = self.high[di-self.delay-i][ii]
                        EMA2hh[i] = self.high[di-self.delay-i][ii]
                    else:
                        EMAhh[i] = (self.high[di - self.delay - i][ii] + EMAhh[i+1]) * 0.5
                        EMA2hh[i] = (EMAhh[i] + EMA2hh[i+1]) * 0.5
                        DEMAhh[i] = 2 * EMAhh[i] - EMA2hh[i]

                mhh5 = np.zeros(10)
                for i in range(10):
                    mhh5[i] = np.nanmax(self.high[di-self.delay-i-np.arange(5), ii])
                temp2 = np.nanstd(mhh5)
                if temp2 > 1e-5:
                    self.alpha[ii] = np.nanstd(DEMAhh[np.arange(10)]) / temp2

    def dependencies(self):
        self.register_dependency('adj_high')