from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaMarauder_18(AlphaBase):
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
                n = 20
                value1 = np.zeros(n)
                for i in range(n-1, -1, -1):
                    if i == n-1:
                        value1[i] = util.EffiRatio(self.cps[di-self.delay-i-np.arange(5), ii]) * self.cps[di-self.delay-i][ii]
                    else:
                        tmp = util.EffiRatio(self.cps[di-self.delay-i-np.arange(5), ii])
                        value1[i] = 0.5 * tmp * self.cps[di-self.delay-i][ii] + (1 - 0.5 * tmp) * value1[i+1]

                temp2 = np.zeros(20)
                for i in range(20):
                    temp = np.zeros(22)
                    for j in range(22):
                        temp[j] = max(self.high[di-self.delay-i-j][ii], self.cps[di-self.delay-i-j-1][ii]) - min(self.low[di-self.delay-i-j][ii], self.cps[di-self.delay-i-j-1][ii])
                    tmp = np.nanstd(temp)
                    if tmp > 1e-5:
                        temp2[i] = (temp[0] - np.nanmean(temp))/tmp
                self.alpha[ii] = util.corr(value1, temp2) - util.corr(value1[np.arange(5)], temp2[np.arange(5)])

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')
        self.register_dependency('volume')
