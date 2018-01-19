from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaQuickstep_9(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.high = self.context.fetch_data('adj_high')
        self.low = self.context.fetch_data('adj_low')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                Vl1 = (self.low[di-self.delay-np.arange(20), ii] + self.high[di-self.delay-np.arange(20), ii] + self.cps[di-self.delay-np.arange(20), ii]) / 3.
                Vl2 = np.maximum(self.high[di-self.delay-np.arange(20), ii], self.cps[di-self.delay-1-np.arange(20), ii]) - np.minimum(self.low[di-self.delay-np.arange(20), ii], self.cps[di-self.delay-1-np.arange(20), ii])
                self.alpha[ii] = util.corr(Vl1, Vl2) - util.corr(Vl1[np.arange(5)], Vl2[np.arange(5)])

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')