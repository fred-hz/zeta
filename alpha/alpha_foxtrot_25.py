from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaFoxtrot_25(AlphaBase):
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
                n = 10
                Vl = np.zeros(n)
                PMF = np.zeros(n)
                for i in range(n-1, -1, -1):
                    if self.cps[di-self.delay-i-1][ii] > self.cps[di-self.delay-i][ii]:
                        Vl[i] = self.cps[di-self.delay-i-1][ii] - self.cps[di-self.delay-i][ii]
                    if self.high[di-self.delay-i][ii]+self.low[di-self.delay-i][ii]+self.cps[di-self.delay-i][ii] > self.high[di-self.delay-i-1][ii]+self.low[di-self.delay-i-1][ii]+self.cps[di-self.delay-i-1][ii]:
                        PMF[i] = (self.high[di-self.delay-i][ii]+self.low[di-self.delay-i][ii]+self.cps[di-self.delay-i][ii]) * self.vol[di-self.delay-i][ii]
                self.alpha[ii] = -util.corr(Vl, PMF)

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')
        self.register_dependency('volume')