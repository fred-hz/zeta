from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaFoxtrot_45(AlphaBase):
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
                deltall = self.low[di-self.delay-np.arange(20), ii] - self.low[di-self.delay-np.arange(20)-1, ii]
                mom = self.high[di-self.delay-np.arange(20), ii] - self.cps[di-self.delay-np.arange(20), ii]
                self.alpha[ii] = util.corr(deltall, mom) - util.corr(deltall[np.arange(5)], mom[np.arange(5)])

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')