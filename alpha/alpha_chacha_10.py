from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaChacha_10(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.vol = self.context.fetch_data('volume')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                PercB = np.zeros(10)
                for i in range(10):
                    stdcc = np.nanstd(self.cps[di-self.delay-i-np.arange(20), ii])
                    if stdcc > 1e-5:
                        PercB[i] = (self.cps[di-self.delay-i][ii] - np.nanmean(self.cps[di-self.delay-i-np.arange(20), ii]))/4./stdcc+0.5
                temp = np.nanstd(PercB)
                if temp > 1e-5:
                    self.alpha[ii] = -np.nanstd(np.log(self.vol[di-self.delay-np.arange(10), ii]))/temp

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('volume')