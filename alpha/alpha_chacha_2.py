from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaChacha_2(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.vol = self.context.fetch_data('volume')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = np.nanstd(self.vol[di-self.delay-np.arange(20), ii])
                if temp > 1e-5:
                    self.alpha[ii] = np.nanstd(self.vol[di-self.delay-np.arange(20), ii] * np.sign(self.cps[di-self.delay-np.arange(20), ii] - self.cps[di-self.delay-np.arange(20)-1, ii])) / temp

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('volume')