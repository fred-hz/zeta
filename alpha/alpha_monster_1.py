from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaMonster_1(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.open = self.context.fetch_data('adj_open')
        self.high = self.context.fetch_data('adj_high')
        self.low = self.context.fetch_data('adj_low')

    def compute_day(self, di):
        indicator = np.zeros(len(self.context.ii_list))
        indicator.flat = np.nan
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp1 = np.zeros(20)
                temp2 = np.zeros(20)
                temp2.flat = np.nan
                for i in range(20):
                    temp1[i] = self.open[di-self.delay-i][ii] - self.open[di-self.delay-i-1][ii]
                    mhh10 = np.nanmax(self.high[di-self.delay-i-np.arange(10), ii])
                    mll10 = np.nanmin(self.low[di - self.delay - i - np.arange(10), ii])
                    if mhh10 - mll10 > 1e-5:
                        temp2[i] = (self.cps[di-self.delay-i][ii]-mll10) / (mhh10-mll10) * 100
                indicator[ii] = util.corr(temp1, temp2)
        util.rank(indicator)
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                if self.cps[di-self.delay-4][ii] > 1e-5:
                    self.alpha[ii] = (self.cps[di-self.delay][ii] - self.cps[di-self.delay-4][ii]) / self.cps[di-self.delay-4][ii] * (indicator[ii] - 0.5)

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_open')
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')