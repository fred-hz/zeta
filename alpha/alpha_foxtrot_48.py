from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaFoxtrot_48(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.low = self.context.fetch_data('adj_low')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                ZB = np.zeros(20)
                deltall = np.zeros(20)
                for i in range(20):
                    stdcc = np.nanstd(self.cps[di-self.delay-i-np.arange(20), ii])
                    if stdcc > 1e-5:
                        ZB[i] = (self.cps[di-self.delay-i][ii] - np.nanmean(self.cps[di-self.delay-i-np.arange(20),ii]))/stdcc
                    else:
                        ZB[i] = 0.
                    deltall[i] = self.low[di-self.delay-i][ii] - self.low[di-self.delay-i-1][ii]
                self.alpha[ii] = util.corr(ZB[np.arange(5)], deltall[np.arange(5)]) - util.corr(ZB, deltall)

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_low')