from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaFoxtrot_21(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.vol = self.context.fetch_data('volume')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                Vl = np.zeros(10)
                stdvv = np.zeros(10)
                for i in range(10):
                    if self.cps[di-self.delay-i][ii] < self.cps[di-self.delay-i-1][ii]:
                        Vl[i] = self.cps[di-self.delay-i-1][ii] - self.cps[di-self.delay-i][ii]
                    stdvv[i] = np.nanstd(self.vol[di-self.delay-i-np.arange(20), ii])
                self.alpha[ii] = -util.corr(Vl, stdvv)

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('volume')
