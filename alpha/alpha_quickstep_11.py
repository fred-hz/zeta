from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaQuickstep_11(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.ret = self.context.fetch_data('return')
        self.vol = self.context.fetch_data('volume')
        self.tov = self.context.fetch_data('turnover')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                value1 = np.zeros(20)
                for i in range(20):
                    value1[i] = np.nansum(self.ret[di-self.delay-i-np.arange(40), ii] * self.vol[di-self.delay-i-np.arange(40), ii])
                self.alpha[ii] = util.corr(value1, self.tov[di-self.delay-np.arange(20), ii]) - util.corr(value1[np.arange(5)], self.tov[di-self.delay-np.arange(5), ii])

    def dependencies(self):
        self.register_dependency('return')
        self.register_dependency('volume')
        self.register_dependency('turnover')