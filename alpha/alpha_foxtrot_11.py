from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaFoxtrot_11(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.low = self.context.fetch_data('adj_low')
        self.cps = self.context.fetch_data('adj_close')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = np.zeros(10)
                for i in range(10):
                    if self.cps[di-self.delay-i][ii] > self.cps[di-self.delay-i-1][ii]:
                        temp[i] = self.cps[di-self.delay-i][ii] - self.cps[di-self.delay-i-1][ii]
                self.alpha[ii] = util.corr(temp, self.low[di-self.delay-np.arange(10), ii] - self.low[di-self.delay-np.arange(10)-1, ii])

    def dependencies(self):
        self.register_dependency('adj_low')
        self.register_dependency('adj_close')