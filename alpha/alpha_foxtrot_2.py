from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaFoxtrot_2(AlphaBase):
    def initialize(self):
        self.cps = self.context.fetch_data('adj_close')
        self.low = self.context.fetch_data('adj_low')
        self.high = self.context.fetch_data('adj_high')
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.delay = int(self.params['delay'])

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                n = 100
                Vg = np.zeros(n)
                mg = np.zeros(n)
                count = 0
                count1 = 0
                for i in range(n-1, -1, -1):
                    if self.cps[di-self.delay-i][ii] > self.cps[di-self.delay-i-1][ii]:
                        Vg[count] = self.cps[di-self.delay-i][ii] - self.cps[di-self.delay-i-1][ii]
                    if count == 10:
                        mg[count1] = np.nanmean(Vg[np.arange(10)])
                        count1 += 1
                    elif count > 10:
                        mg[count1] = Vg[count] * 0.1 + mg[count1-1] * 0.9
                        count1 += 1
                    count += 1

                NDM = np.zeros(10)
                for i in range(10):
                    if (self.low[di-self.delay-i-1][ii] - self.low[di-self.delay-i][ii]) > (self.high[di-self.delay-i][ii] - self.high[di-self.delay-i-1][ii]) and (self.low[di-self.delay-i-1][ii] > self.low[di-self.delay-i][ii]):
                        NDM[i] = self.low[di-self.delay-i-1][ii] = self.low[di-self.delay-i][ii]

                if count1 > 10:
                    self.alpha[ii] = -util.corr(mg[count1 - 1 - np.arange(10)], NDM)

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_low')
        self.register_dependency('adj_high')