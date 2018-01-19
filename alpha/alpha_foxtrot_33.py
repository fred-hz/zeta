from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaFoxtrot_33(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.high = self.context.fetch_data('adj_high')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = np.zeros(10)
                for i in range(10):
                    temp[i] = util.mabsdv(self.cps[di-self.delay-i-np.arange(5), ii])
                self.alpha[ii] = -util.corr(temp, self.high[di-self.delay-np.arange(10), ii]-self.cps[di-self.delay-np.arange(10), ii])

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
