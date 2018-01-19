from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaRumba_27(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.open = self.context.fetch_data('adj_open')
        self.low = self.context.fetch_data('adj_low')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = np.zeros(20)
                for i in range(20):
                    if self.cps[di-self.delay-i-1][ii] > self.cps[di-self.delay-i-2][ii]:
                        temp[i] = self.cps[di-self.delay-i-1][ii] - self.cps[di-self.delay-i-2][ii]
                self.alpha[ii] = util.corr(temp, self.cps[di-self.delay-np.arange(20), ii] - self.open[di-self.delay-np.arange(20), ii])

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_open')
        self.register_dependency('adj_low')
