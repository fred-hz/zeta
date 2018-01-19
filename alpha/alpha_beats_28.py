from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaBeats_28(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.low = self.context.fetch_data('adj_low')

    def compute_day(self, di):
        indicator = np.zeros(len(self.context.ii_list))
        indicator.flat = np.nan
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                if np.where(-np.isnan(self.low[di - self.delay - np.arange(20), ii]))[0].size == 0:
                    continue
                indicator[ii] = np.nanargmin(self.low[di-self.delay-np.arange(20), ii])
        util.rank(indicator)
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = np.nanmean(self.cps[di-self.delay-np.arange(5), ii])
                if abs(temp) > 1e-5:
                    self.alpha[ii] = (temp - self.cps[di-self.delay][ii]) / temp * (indicator - 0.5)

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_low')