from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaFoxtrot_29(AlphaBase):
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
                temp1 = np.zeros(10)
                temp2 = np.zeros(10)
                for i in range(10):
                    temp1[i] = util.mabsdv(self.vol[di-self.delay-i-np.arange(5), ii])
                    if self.high[di-self.delay-i][ii] + self.cps[di-self.delay-i][ii] + self.low[di-self.delay-i][ii] < self.high[di-self.delay-i-1][ii] + self.cps[di-self.delay-i-1][ii] + self.low[di-self.delay-i-1][ii]:
                        temp2[i] = (self.high[di-self.delay-i][ii] + self.cps[di-self.delay-i][ii] + self.low[di-self.delay-i][ii]) * self.vol[di-self.delay-i][ii]
                self.alpha[ii] = -util.corr(temp1, temp2)

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')
        self.register_dependency('volume')