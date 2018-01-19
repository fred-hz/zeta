from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaBeats_21(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.high = self.context.fetch_data('adj_high')
        self.low = self.context.fetch_data('adj_low')
        self.vol = self.context.fetch_data('volume')

    def compute_day(self, di):
        indicator = np.zeros(len(self.context.ii_list))
        indicator.flat = np.nan
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                tot_vol = 0.
                MFV = 0.
                for i in range(20):
                    if self.high[di-self.delay-i][ii] - self.low[di-self.delay-i][ii] > 1e-5:
                        MFV += self.vol[di-self.delay-i][ii] * (self.cps[di-self.delay-i][ii] - (self.high[di-self.delay-i][ii] + self.low[di-self.delay-i][ii])/2.0)/(self.high[di-self.delay-i][ii] - self.low[di-self.delay-i][ii])
                        tot_vol += self.vol[di - self.delay - i][ii]
                if tot_vol > 1e-5:
                    indicator[ii] = (self.vol[di-self.delay][ii] - self.vol[di-self.delay-1][ii]) * MFV / tot_vol
        util.rank(indicator)
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                self.alpha[ii] = (self.cps[di-self.delay-4][ii] - self.cps[di-self.delay][ii]) / self.cps[di-self.delay-4][ii] * (indicator[ii] - 0.5)

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')
        self.register_dependency('volume')